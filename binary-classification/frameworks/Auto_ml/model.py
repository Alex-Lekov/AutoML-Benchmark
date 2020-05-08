import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import time
import datetime
import json
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score, log_loss, accuracy_score
from datasets import all_datasets_ls
from datasets import preproc_data
from cash_ml import Predictor
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1" 

print('START')

MODEL_NAME = 'Auto_ml'
CV = 5 # end repeat

for DATASET_NAME in all_datasets_ls:
    # DATASET_NAME = 'credit-g'
    metrics = []
    # ./automl-benchmark/binary-classification/datasets/{DATASET_NAME}/features.json
    with open(f'./datasets/{DATASET_NAME}/features.json') as f:
        features = json.load(f)

    print('LOAD DATASET')
    data= pd.read_csv(f'./datasets/{DATASET_NAME}/{DATASET_NAME}.csv')

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
        X_train['target'] = y_train
        column_descriptions = {'target': 'output',}

        START_EXPERIMENT = time.time()
        print(f'START FIT ON FOLD {count}')
        automl = Predictor(type_of_estimator='classifier', column_descriptions=column_descriptions)
        automl.train(X_train, 
                    model_names = [
                        'LogisticRegression',
                        'RandomForestClassifier',
                        'ExtraTreesClassifier',
                        'RidgeClassifier',
                        'SGDClassifier',
                        'LinearSVC',
                        'DeepLearningClassifier', 
                        'LGBMClassifier', 
                        'CatBoostClassifier', 
                        'XGBClassifier',
                        ], # chose all Classifiers
                    #optimize_final_model=True,   # falls with an error :(
                    #feature_learning=True, 
                    #fl_data=X_test.copy(),
                    ml_for_analytics=False, 
                    verbose=False,)

        print(f'PREDICT ON FOLD {count}')
        predictions = automl.predict_proba(X_test)
        print('AUC: ', roc_auc_score(y_test, predictions[:,1]))
        y_test_predict_proba = predictions[:,1]
        y_test_predict = automl.predict(X_test)

        END_EXPERIMENT = time.time()

        #preds = pd.DataFrame(predictions)
        #preds['Y'] = y_test.reset_index(drop=True)
        # preds.to_csv(f'./result/predicts/{DATASET_NAME}_{MODEL_NAME}_predict_proba_exp_{EXPERIMENT}.csv', index=False,)

        metrics.append({
            'AUC': round(roc_auc_score(y_test, y_test_predict_proba),4),
            'log_loss': round(log_loss(y_test, y_test_predict_proba),4),
            'Accuracy': round(accuracy_score(y_test, y_test_predict),4),
            'Time_min': (END_EXPERIMENT - START_EXPERIMENT)//60,
            'Time': datetime.datetime.now(),
        })
        pd.DataFrame(metrics).to_csv(f'./result/{DATASET_NAME}_{MODEL_NAME}_metrics.csv', index=False,)


