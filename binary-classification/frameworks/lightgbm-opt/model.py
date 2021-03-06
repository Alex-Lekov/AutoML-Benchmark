import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_c
import time
import datetime
import json
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score, log_loss, accuracy_score
from datasets import all_datasets_ls
from datasets import preproc_data
from alexautoml import *
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from tqdm import tqdm
import sys


print('START')

MODEL_NAME = 'lightgbm-opt'
TIME_LIMIT = 3600 # 1h
CV = 5 

for DATASET_NAME in all_datasets_ls:
    metrics = []
    # ./automl-benchmark/binary-classification/datasets/{DATASET_NAME}/features.json
    with open(f'./datasets/{DATASET_NAME}/features.json') as f:
        features = json.load(f)

    print('LOAD DATASET')
    data = pd.read_csv(f'./datasets/{DATASET_NAME}/{DATASET_NAME}.csv')
    print('Dataset: ', DATASET_NAME, data.shape,)

    print('PREPROC DATASET')
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
    # for feature in X.columns:
    #     if X[feature].nunique(dropna=False) < 3:
    #         X[feature] = X[feature].astype('category').cat.codes

    # One Hot Encoding
    # if len(cat_features) > 0:
    #     encoder = OneHotEncoder(cols=cat_features, drop_invariant=True) 
    #     X = encoder.fit_transform(X)

    skf = StratifiedKFold(n_splits=CV, shuffle=True, random_state=42)

    for count, (train_idx, test_idx) in enumerate(skf.split(X, y)):
        print(f'START FOLD {count}')
        RANDOM_SEED = count
        EXPERIMENT = count
        np.random.seed(RANDOM_SEED)

        #shuffle columns for more randomization experiment
        columns_tmp = list(X.columns.values)
        np.random.shuffle(columns_tmp)
        X = X[columns_tmp]

        # Split
        X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
        X_test, y_test = X.iloc[test_idx], y.iloc[test_idx]
        #print(DATASET_NAME, X_train.shape, X_test.shape)

        # Auto_ml
        START_EXPERIMENT = time.time()

        data = DataBunch(X_train=X_train, 
                y_train=y_train,
                X_test=X_test,
                cat_features=cat_features,
                clean_and_encod_data=True,
                cat_encoder='HelmertEncoder',
                clean_nan=True,
                random_state=RANDOM_SEED,
                )
              
        model = LightGBMClassifier(databunch=data, metric='auc', random_state=RANDOM_SEED)

        s = model.opt(timeout=TIME_LIMIT, verbose=1)           

        y_test_predict_proba, _ = model.fit_predict()
        #y_test_predict = automl.predict(X_test)

        print('AUC: ', roc_auc_score(y_test, y_test_predict_proba))

        END_EXPERIMENT = time.time()

        #preds = pd.DataFrame(predictions)
        #preds['Y'] = y_test.reset_index(drop=True)
        #preds.to_csv(f'./result/predicts/{DATASET_NAME}_{MODEL_NAME}_predict_proba_exp_{EXPERIMENT}.csv', index=False,)

        metrics.append({
            'AUC': round(roc_auc_score(y_test, y_test_predict_proba),4),
            'log_loss': round(log_loss(y_test, y_test_predict_proba),4),
            'Accuracy': round(accuracy_score(y_test, y_test_predict_proba>0.5),4),
            'Time_min': (END_EXPERIMENT - START_EXPERIMENT)//60,
            'Time': datetime.datetime.now(),
        })
        pd.DataFrame(metrics).to_csv(f'./result/{DATASET_NAME}_{MODEL_NAME}_metrics.csv', index=False,)


