# import libraries
import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):

    # load messages dataset
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)

    # create a dataframe of all category columns
    categories = categories['categories'].str.split(";", expand=True)

    columnsName = categories.iloc[0,:]
    category_colnames = columnsName.apply(lambda x: x[0:-2])

    # rename the columns of `categories`
    categories.columns = category_colnames

    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].apply(lambda x: x[-1:])
        
        # convert column from string to numeric
        categories[column] = pd.Series(categories[column], dtype="Int64")

    # return merged (messages & categories) datasets based on index
    return pd.merge(messages, categories, left_index=True, right_index=True)

def clean_data(df):
    """
    The function will make all column categories are binary values, and it will remove the duplicates in the dataframe
    
    Parameters the function takes:
    df (dataframe): The dataset that contains the messages and categories
    
    Returns:
    df (dataframe): The cleaned dataset
    """
    # Data Cleaning by making related column binary values
    df['related']=df['related'].map(lambda x: 1 if x == 2 else x)

    # remove all duplicates in dataset and 
    return df.drop_duplicates()


def save_data(df, database_filename):
    """
    The function will saves the data in SQLite database
    
    Parameters the function takes:
    df (dataframe): A cleaned dataset
    database_filename (str): The name of the database file to be created - should end in .db.  
    
    Returns:
    The database file with the above specified name
    """
    # save dataset in SQlist file
    df.to_sql('disasterResponseDatabase',
     create_engine('sqlite:///{}'.format(database_filename)), if_exists='replace', index=False)  


def main():
    # The main function will takes all data needed from the command line.
    # Then transform raw data into a cleaned data saved in database file.
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)
        
        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')

if __name__ == '__main__':
    main()