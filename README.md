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

0. Check that no virtual environment (venv) of any kind is running, you want to see the name of your computer as the first thing in the terminal 
1. docker-compose build --no-cache 
2. docker-compose up -d 
3. Paste "http://localhost:8000/" into browser and upload file to test 
4. If met with errors, paste "docker-compose logs frontend" into terminal and evaluate output 
5. To run code in Docker temporary environment, paste "docker exec -it scrna-frontend bash" into terminal and run "shiny run UI/app.py"


# scRNA-seq-Automation

pip install -r requirements.txt

python src/main.py

shiny run UI/app.py

docker-compose build --no-cache
after this, you need to run "docker-compose up -d" to actually start the docker
and when leaving VSCode, run "docker-compose down"  # To run in background

git add <file>        # After resolving
git commit -m "<message>" # Finish merge
git push origin main   # Push if needed

git status # to see what files you have made changes to

### Not needed anymore 
# for xg boost, libomp: first,
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" # takes about five mins
# add to path (for M chip mac)
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
# then
brew install libomp