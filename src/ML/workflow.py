import pandas as pd
import numpy as np
from anndata import AnnData
from scipy.sparse import csr_matrix, hstack
from joblib import load

def align_anndata_to_genes(adata: AnnData, expected_genes: list) -> AnnData:
    """Ensure adata includes all genes in expected_genes, in correct order, with missing ones filled with zeros."""
    current_genes = adata.var_names
    present_genes = current_genes.intersection(expected_genes)
    missing_genes = [g for g in expected_genes if g not in current_genes]

    # Build sparse matrix for missing genes
    zero_matrix = csr_matrix((adata.n_obs, len(missing_genes)))

    # Combine existing and missing
    X_existing = adata[:, present_genes].X
    X_combined = hstack([X_existing, zero_matrix])

    # Reorder columns to match expected gene order
    all_genes = list(present_genes) + missing_genes
    gene_order_idx = [all_genes.index(g) for g in expected_genes]
    X_final = X_combined.tocsr()[:, gene_order_idx]

    # Return aligned AnnData
    aligned = AnnData(X=X_final, obs=adata.obs.copy())
    aligned.var_names = expected_genes
    return aligned, missing_genes

def predict_labels(adata, ML_data, confidence_threshold=0.9):
    # Load trained gene list (from feature importances CSV)
    HVG_list = pd.read_csv("src/ML/XGB_classifier_V3_gene_names.csv").iloc[0].tolist()
    
    # Align ML_data to expected gene list
    ML_aligned, missing_genes = align_anndata_to_genes(ML_data, HVG_list)

    # Load XGBoost classifier
    classifier = load('src/ML/XGB_classifier_V3.joblib')

    # Predict using aligned data
    X_input = ML_aligned.X.toarray() if hasattr(ML_aligned.X, "toarray") else ML_aligned.X
    
    #Get index of missing genes
    missing_gene_indices = [ML_aligned.var_names.get_loc(gene) for gene in missing_genes]
    
    # Set missing genes to NaN
    X_input[:, missing_gene_indices] = np.nan
    
    #predict usig aligned data
    predictions = classifier.predict(X_input)

    # Get probabilities for each class
    probability = classifier.predict_proba(X_input)

    confidence_scores = np.max(probability, axis=1)

    # Map numeric predictions to labels
    label_dict = {
        0: 'Non Epithelial',
        1: 'Non Cancer Related',
        2: 'Early (Stage I/II)',
        3: 'Advanced (Stage III/IV)'
    }

    raw_labels = [label_dict[p] for p in predictions]

    # Step 4: Apply confidence threshold
    final_labels = [
        raw_label if confidence >= confidence_threshold else "Unknown"
        for raw_label, confidence in zip(raw_labels, confidence_scores)
    ]

    # Add predictions to output AnnData object
    adata.obs["Classifier_predictions"] = raw_labels
    adata.obs["Classifier_prediction_probablility"] = confidence_scores
    adata.obs["Classifier_FINAL"] = final_labels


    return adata