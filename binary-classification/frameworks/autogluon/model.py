import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import time
import datetime
import json
import os 
import shutil
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score, log_loss, accuracy_score
from datasets import all_datasets_ls
from datasets import preproc_data

from autogluon import TabularPrediction as task
from autogluon.utils.tabular.metrics import roc_auc


print('START')

MODEL_NAME = 'autogluon'
TIME_LIMIT = 3600 # 1h
CV = 5
eval_metric = 'roc_auc'
PATH = "AutogluonModels"
random_seed = 42

for DATASET_NAME in all_datasets_ls:
    # DATASET_NAME = 'credit-g'
    metrics = []
    # ./automl-benchmark/binary-classification/datasets/{DATASET_NAME}/features.json
    with open(f'./datasets/{DATASET_NAME}/features.json') as f:
        features = json.load(f)
    print('='*75)
    print(features)
    
    print('='*40, 'LOAD DATASET', '='*40)
    data = pd.read_csv(f'./datasets/{DATASET_NAME}/{DATASET_NAME}.csv')
    print('Dataset: ', DATASET_NAME, data.shape,)
    print('PREPROC DATASET')
    X, y = preproc_data(data, features)

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
        #os.mkdir('AutogluonModels')
        X_train['target'] = y_train
        label_column = 'target'
        train_data = task.Dataset(df = X_train)
        
        predictor = task.fit(train_data=train_data, 
                             label=label_column, 
                             eval_metric=eval_metric, 
                             verbosity=1, 
                             auto_stack=True, 
                             save_space=True,
                             cache_data=False,
                             time_limits=TIME_LIMIT,
                             random_seed=random_seed)
        
        results = predictor.fit_summary()
        
        test_data = task.Dataset(df = X_test)
        y_test_predict_proba = predictor.predict_proba(test_data)

        print('AUC: ', roc_auc_score(y_test, y_test_predict_proba))
        END_EXPERIMENT = time.time()
        print('Total sec: ', (END_EXPERIMENT - START_EXPERIMENT))

        #preds = pd.DataFrame(predictions)
        #preds['Y'] = y_test.reset_index(drop=True)
        #preds.to_csv(f'./result/predicts/{DATASET_NAME}_{MODEL_NAME}_predict_proba_exp_{EXPERIMENT}.csv', index=False,)

        metrics.append({
            'AUC': round(roc_auc_score(y_test, y_test_predict_proba),4),
            'log_loss': round(log_loss(y_test, y_test_predict_proba),4),
            'Accuracy': round(accuracy_score(y_test, (y_test_predict_proba>0.5)),4),
            'Time_min': (END_EXPERIMENT - START_EXPERIMENT)//60,
            'Time': datetime.datetime.now(),
        })
        pd.DataFrame(metrics).to_csv(f'./result/{DATASET_NAME}_{MODEL_NAME}_metrics.csv', index=False,)

        # Clean PATH
        #shutil.rmtree(PATH)
        for filename in os.listdir(PATH):
            filepath = os.path.join(PATH, filename)
            try:
                shutil.rmtree(filepath)
            except OSError:
                os.remove(filepath)
        #os.mkdir('AutogluonModels') 


