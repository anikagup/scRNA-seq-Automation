## About This Repository
Hi! We are Anika, Tara, and Erik, 3 biomedical engineering seniors at USC. This repository is our senior design project: an automated sc-RNA sequencing web application designed for researchers who have no coding experience. Please feel free to contact us at anikagup@usc.edu (Anika), taranate@usc.edu (Tara), and noyman@usc.edu (Erik), with any questions, comments, or concerns!

## To Run App Through Docker
1. Download the Docker Desktop from here: https://www.docker.com/products/docker-desktop/
2. Install Git here from: https://git-scm.com/downloads
3. Clone the Github repository in the local computer’s terminal/command prompt by running each command once, separately: 
git clone https://github.com/anikagup/scRNA-seq-Automation.git
cd scRNA-seq-Automation
4. Start the app by running: docker-compose up --build
5. Paste this link in your browser to run the app: http://localhost:8000
6. Upload a supported .h5ad, .csv, .h5, .loom, or .fastq file.
7. Click Run Analysis to start preprocessing and visualization.
8. Adjust QC parameters and click Reprocess to regenerate figures.
9. Enter a gene you know is in your dataset and click Generate UMAP to view expression patterns.
10. Download the Processed CSV or DEG List using the provided buttons.
11. To stop the app when you are done, first Press Ctrl C, then run 
docker-compose down

Important notes:
1.  Check that no virtual environment (venv) of any kind is running, you want to see the name of your computer as the first thing in the terminal 
2. docker-compose build --no-cache # build and save space
3. docker-compose up -d # to run app after build
4. If met with errors, paste "docker-compose logs frontend" into terminal and evaluate output 

