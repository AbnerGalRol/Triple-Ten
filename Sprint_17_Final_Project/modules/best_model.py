import pandas as pd

from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.utils import shuffle

from catboost import CatBoostClassifier
import lightgbm as lgb

import tensorflow as tf
from tensorflow import keras

# Creamos una semilla
random_state = 12345

def model_selection(features_train, features_test, target_train, target_test):

    # Creamos un modelo Dummy

    model_dumy = DummyClassifier(strategy='most_frequent')
    model_dumy.fit(features_train, target_train)
    dummy_pred = model_dumy.predict(features_test)
    dummy_roc_auc = roc_auc_score(target_test,dummy_pred)

    # Usamos GridSearchCV para probar diferentes hyperparametros y encontrar el mejor modelo de árbol de decisión 

    param_grid = {
        'max_depth':[None,2,5,10],
        'min_samples_split':[2,5],
        'min_samples_leaf':[1,2]
    }

    grid_search = GridSearchCV(
        estimator=DecisionTreeClassifier(
            random_state = random_state),
            param_grid=param_grid, 
            cv=5,
            scoring='roc_auc')

    grid_search.fit(features_train, target_train)

    best_params_tree = grid_search.best_params_
    best_score_tree = grid_search.best_score_

    best_model_tree = grid_search.best_estimator_
    predict_tree = best_model_tree.predict(features_test)

    # Usamos GridSearchCV para probar diferentes hyperparametros y encontrar el mejor modelo de bosque aleatorio 

    param_grid = {
        'n_estimators':[50,100,150],
        'max_depth':[None,3,5,7,9,11],
        'min_samples_split': [2, 5, 10]
    }

    grid_search = GridSearchCV(
        estimator=RandomForestClassifier(
            random_state = random_state), 
            param_grid=param_grid, 
            cv=5, 
            scoring='roc_auc')

    grid_search.fit(features_train, target_train)

    best_params_rf = grid_search.best_params_
    best_score_rf = grid_search.best_score_

    best_model_rf = grid_search.best_estimator_
    predict_forest = best_model_rf.predict(features_test)

    # Usamos GridSearchCV para probar diferentes hyperparametros y encontrar el mejor modelo de regresión logística

    param_grid = {
        'penalty': ['l1', 'l2'],
        'C': [0.001, 0.01, 0.1, 1, 10, 100],
    }

    grid_search = GridSearchCV(
        estimator=LogisticRegression(
            class_weight = 'balanced', max_iter = 5000, solver = 'liblinear'), 
            param_grid=param_grid, 
            cv=5, 
            scoring='roc_auc')

    grid_search.fit(features_train, target_train)

    best_params_LR = grid_search.best_params_

    best_score_LR = grid_search.best_score_

    best_model_LR = grid_search.best_estimator_
    predict_lr = best_model_LR.predict(features_test)

    # Creamos un modelo lightgbm

    train_data = lgb.Dataset(features_train,label=target_train)
    test_data = lgb.Dataset(features_test,label=target_test)
    params = {
        'objective': 'binary',  
        'metric': 'binary_logloss', 
        'boosting_type': 'gbdt',
        'num_leaves': 31,
        'learning_rate': 0.05,
        'feature_fraction': 0.9
    }
    num_round = 100
    bts = lgb.train(params, train_data, num_round, valid_sets=[test_data])
    lgb_predict = bts.predict(features_test,num_iteration=bts.best_iteration)
    lgb_score = roc_auc_score(target_test,lgb_predict)

    # Usamos GridSearchCV para probar diferentes hyperparametros y encontrar el mejor modelo CatBoost

    param_grid = {
        'learning_rate': [0.01, 0.1, 0.2],
        'depth': [4, 6, 8],
        'n_estimators': [50, 100, 200],
    }

    grid_search = GridSearchCV(
        estimator=CatBoostClassifier(verbose=0),
            param_grid=param_grid, 
            cv=5, 
            scoring='roc_auc')

    grid_search.fit(features_train, target_train)

    best_params_CB = grid_search.best_params_
    best_score_CB = grid_search.best_score_

    best_model_CB = grid_search.best_estimator_
    predict_cb = best_model_CB.predict(features_test)

    # Creamos un modelo de redes neuronales sencillo 

    model_NN = keras.Sequential()
    model_NN.add(keras.layers.Dense(units=64, activation='relu'))
    model_NN.add(keras.layers.Dense(units=32, activation='relu'))
    model_NN.add(keras.layers.Dense(units=1, activation='sigmoid'))
    model_NN.compile(optimizer='adam', loss=tf.keras.losses.sparse_categorical_crossentropy, metrics=['accuracy'])
    model_NN.fit(
        features_train, target_train, epochs=10, batch_size=32, validation_data=(features_test, target_test))
    neu_net_predict = model_NN.predict(features_test)
    neu_net_score = roc_auc_score(target_test,neu_net_predict)  

    scores = {
        'Dummy Classifier': dummy_roc_auc,
        'Decision Tree': best_score_tree,
        'Random Forest': best_score_rf,
        'Logistic Regression': best_score_LR,
        'CatBoost': best_score_CB,
        'Neural Network': neu_net_score
    }

    # Seleccionar el mejor modelo basado en el puntaje AUC-ROC
    best_model_name = max(scores, key=scores.get)
    best_model = None
    best_model_score = None
 
    if best_model_name == 'Dummy Classifier':
            best_model = model_dumy  
            best_model_score = dummy_roc_auc 
    elif best_model_name == 'Decision Tree':
            best_model = best_model_tree
            best_model_score = best_score_tree
    elif best_model_name == 'Random Forest':
            best_model = best_model_rf
            best_model_score = best_score_rf
    elif best_model_name == 'Logistic Regression':
            best_model = best_model_LR
            best_model_score = best_score_LR
    elif best_model_name == 'CatBoost':
            best_model = best_model_CB
            best_model_score = best_score_CB
    elif best_model_name == 'Neural Network':
            best_model = model_NN 
            best_model_score = neu_net_score

    return best_model, best_model_name, best_model_score 