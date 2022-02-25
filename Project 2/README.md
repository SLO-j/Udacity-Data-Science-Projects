# DSND-P2

## Disaster Response Pipeline Project

This project made to analyze disaster data from [appen](https://appen.com/) by building a model with an API that classifies disaster messages.

### Project Components:

There are three components you'll need to complete for this project.

1. [ETL Pipeline](#ETL_Pipeline)
2. [ML Pipeline](#ML_Pipeline)
3. [Flask Web App](#Flask_Web_App)
4. [Instructions](#Instructions)

## ETL Pipeline <a name="ETL_Pipeline"></a>

In a Python script, `process_data.py`, you will find data cleaning pipeline that:

- Load `messages` and `categories` datasets
- Merge the two datasets
- Clean the data
- Store it in a SQLite database

## ML Pipeline <a name="ML_Pipeline"></a>

In a Python script, `train_classifier.py`, you will find data a machine learning pipeline that:

- Load data from the SQLite database
- Split the dataset into `training 80%` and `test 20%` sets
- Build a text processing and machine learning pipeline
- Train and tunes a model using `GridSearchCV`
- Output results on the test set
- Export the final model as a `pickle file`

## Flask Web App <a name="Flask_Web_App"></a>

- Modify file paths for database and model
- Add data visualizations using Plotly in the web app.

### Instructions:<a name="Instructions"></a>

1. Run the following commands in the project's root directory to set up your database and model.

   - To run ETL pipeline that cleans data and stores in database
     `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
   - To run ML pipeline that trains classifier and saves
     `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
   `python run.py`

3. Go to http://0.0.0.0:3001/
