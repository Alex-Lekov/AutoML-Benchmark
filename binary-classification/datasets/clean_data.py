import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import json
from category_encoders import OneHotEncoder


def preproc_data(data, features):
    '''
    Simple preproc data:* LabelEncoded target
                        * One Hot Encoding cat_features
                        * Clean Nans as .median()
                        * split data on X, y

    data: pd.DataFrame()
    cat_features: list() # categorical variables in df
    '''
    # LabelEncoded Target
    for i in features.items():
        if 'target' in i:
            target_col = i[0]
            data[target_col] = data[target_col].astype('category').cat.codes  
    
    y = data[target_col]
    X = data.drop([target_col], axis=1)

    cat_features = []
    for feature in features.items():
        if ('categorical' in feature) and (X[feature[0]].nunique(dropna=False) > 2):
            cat_features.append(feature[0])

    # LabelEncoded Binary Features
    for feature in X.columns:
            if (X[feature].nunique(dropna=False) < 3):
                X[feature] = X[feature].astype('category').cat.codes
                if len(cat_features) > 0:
                    if feature in cat_features:
                        cat_features.remove(feature)

    # One Hot Encoding
    if len(cat_features) > 0:
        encoder = OneHotEncoder(cols=cat_features, drop_invariant=True) 
        X = encoder.fit_transform(X)

    # Nans
    nan_columns = list(X.columns[X.isnull().sum() > 0])
    if nan_columns:
        for nan_column in nan_columns:
            X[nan_column+'isNAN'] = pd.isna(X[nan_column]).astype('uint8')
        X[nan_columns].fillna(X[nan_columns].median(), inplace=True)

    return(X, y)