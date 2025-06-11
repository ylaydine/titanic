"""
Load, preprocess, prepare, and save the Titanic dataset.
"""

import pandas as pd

def load_data():
    """
    Load the Titanic dataset from a CSV file.
    
    Returns:
        DataFrame: The loaded Titanic dataset.
    """
    
    global_path = "./data/"
    file_train = "train.csv"
    file_test = "test.csv"
    path_train = global_path+file_train
    path_test = global_path+file_test
    X_train = pd.read_csv(path_train)
    X_test = pd.read_csv(path_test)
    return X_train, X_test
       
def clean_data(df):
    """
    clean the Titanic dataset.
    
    Args:
        df (DataFrame): The Titanic dataset.
        
    Returns:
        DataFrame: The preprocessed Titanic dataset.
    """
    pass


def prepare_data(df:pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]: 
    """
    Prepare the Titanic dataset for training.
    
    Args:
        df (DataFrame): The preprocessed Titanic dataset.
        
    Returns:
        tuple: A tuple containing [X,y] the features DataFrame and the target Series.
    """
    pass