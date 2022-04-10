# 2. Recommendations with IBM

## Introduction
In the Project Workspace, I used my skills to analyze the interactions that users have with articles on the IBM Watson Studio platform, and make recommendations to them about new articles.

## Libraries
Python 3.9.7
```
pandas==1.3.3
numpy==1.22.3
matplotlib==3.4.3
```

## Project Structures

```
|- app/
  |- run.py: The flask webapp
|- data/
  |- process_data.py: ETL module. It is used to process data and store cleaned data into sqlite database 
  |- disaster_messages.csv: Input data
  |- disaster_cateogires.csv: Input data
  |- DisasterResponse.db: Processed data 
|- models/
  |- train_classifier.py: Load data, train classifier and save into pickle model
  |- classifier.pkl: Trained model
```

## Licensing, Authors, Acknowledgements
Credit to [Udacity](https://www.udacity.com/) Instructors for providing the guidance and data