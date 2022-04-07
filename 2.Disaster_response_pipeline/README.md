# 2. Disaster Response Pipeline Project

## Introduction
In the Project Workspace, I applied my data engineering skills to create a machine learning pipeline to categorize these events so that you can send the messages to an appropriate disaster relief agency by using data from [Appen](https://appen.com/).

## Libraries
Python 3.9.7
```
pandas==1.3.3
nltk==3.7
scikit-learn==1.0.2
SQLAlchemy==1.4.35
plotly==5.7.0
Flask==2.1.1
```

## Instructions

1. Run the following commands in the project's root directory to set up your database and model.
- To run ETL pipeline that cleans data and stores in database
```
python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
```

- To run ML pipeline that trains classifier and saves 
```
python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
```

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Go to http://0.0.0.0:3000

