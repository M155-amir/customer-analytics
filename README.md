# customer-analytics
Big Data assignment - CSCI461

# Project Description
This project builds a complete data pipeline for a car sales dataset using Python and Docker.

The pipeline performs:
 Data ingestion
 Data preprocessing
 Data analytics
 Data visualization
 K-Means clustering

# Project Structure

car-sales-project/
│
├── Dockerfile
├── ingest.py
├── preprocess.py
├── analytics.py
├── visualize.py
├── cluster.py
├── summary.sh
├── README.md
├── data_raw.csv
├── data_preprocessed.csv
├── clusters.txt
├── insight1.txt
├── insight2.txt
├── insight3.txt
└── results/

# Docker Build Command 
docker build -t car-sales-project

# Docker Run Command
docker run -it car-sales-project

# Running the container 
python ingest.py data/cars.csv

# ecxution flow 
ingest.py
    ↓
preprocess.py
    ↓
analytics.py
    ↓
visualize.py
    ↓
cluster.py

# steps description

# ingest.py
Reads the original CSV file
Saves it as data_raw.csv

# preprocess.py
Cleans missing values
Removes duplicates
Encodes categorical data
Scales numerical features
Creates price categories
Saves output as data_preprocessed.csv

# analytics.py
Generates insights about price, mileage, year, body type, and engine type
Saves results into insight text files

# visualize.py
Creates plots such as histogram, heatmap, and pairplot
Saves the image as summary_plot.png

# cluster.py
Applies K-Means clustering
Groups cars into 3 clusters
Saves cluster counts into clusters.txt

# example for cluster output
Cluster 0: 1200 samples
Cluster 1: 950 samples
Cluster 2: 780 samples

# Example Insights
Insight 1:
1500 out of 4345 cars fall into the medium price category

Insight 2:
There is a negative correlation between mileage and price

Insight 3:
Newer cars tend to be more expensive

# Example Docker Workflow
docker build -t pipeline-project .
docker run -it pipeline-project
python ingest.py data/cars.csv

# Required Python Libraries 
pip install pandas numpy matplotlib seaborn scikit-learn scipy requests

# screenshoots for project 
attached with files 

# Team members 
Nour Yehia Abdalfattah 231001884
Malak amir Ibrahim 231001120
Bavly Ramy Samir 231000910 

