import os
import pandas as pd

def reorderColumn(df, column, position):
    col = df.pop(column)
    df.insert(position, col.name, col)
    return df

def readyDataFrameForSQLLoad():
    df = pd.read_csv('data\movies.csv')
    df = reorderColumn(df, 'side_genre', 8)
    df.to_csv('data\movies_clean.csv', index = True, header=True) 
