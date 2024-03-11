import pandas as pd
from upsample_func import upsample

from sklearn.dummy import DummyClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from catboost import CatBoostClassifier
import lightgbm as lgb

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense

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

    best_score_tree = grid_search.best_score_

    best_model_tree = grid_search.best_estimator_
    predict_tree = best_model_tree.predict(features_test)
    tree_roc_auc = roc_auc_score(target_test,predict_tree)

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

    best_score_rf = grid_search.best_score_

    best_model_rf = grid_search.best_estimator_
    predict_forest = best_model_rf.predict(features_test)
    rforest_roc_auc = roc_auc_score(target_test,predict_forest)


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

    best_score_LR = grid_search.best_score_

    best_model_LR = grid_search.best_estimator_
    predict_lr = best_model_LR.predict(features_test)
    LR_roc_auc = roc_auc_score(target_test,predict_lr)


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

    best_score_CB = grid_search.best_score_

    best_model_CB = grid_search.best_estimator_
    predict_cb = best_model_CB.predict(features_test)
    CB_roc_auc = roc_auc_score(target_test,predict_cb)

    # Creamos un modelo de redes neuronales sencillo 

    model_NN = Sequential()
    model_NN.add(Dense(units=32, activation='relu'))
    model_NN.add(Dense(units=1, activation='sigmoid'))
    model_NN.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model_NN.fit(
        features_train.values, target_train.values, epochs=5, batch_size=32, validation_data=(features_test.values, target_test.values))
    neu_net_predict = model_NN.predict(features_test.values)
    neu_net_score = roc_auc_score(target_test,neu_net_predict)  

    #Upsample
    features_upsample, target_upsample = upsample(features_train, target_train, 10)

    features_train_u, features_test_u, target_train_u, target_test_u = train_test_split(
    features_upsample, target_upsample, test_size = 0.2, random_state=random_state)

    # Dummy upsample
    model_dumy_u = DummyClassifier(strategy='most_frequent')
    model_dumy_u.fit(features_train_u, target_train_u)
    dummy_pred_u = model_dumy.predict(features_test_u)
    dummy_roc_auc_u = roc_auc_score(target_test_u,dummy_pred_u)

    # Decission Three Upsample

    param_grid = {
        'max_depth':[None,3,5,7,9,11],
        'min_samples_split':[2,4,6,8],
        'min_samples_leaf':[2,4,6]
    }

    grid_search = GridSearchCV(
        estimator=DecisionTreeClassifier(
            random_state = random_state),
            param_grid=param_grid, 
            cv=5,
            scoring='roc_auc')

    grid_search.fit(features_train_u, target_train_u)

    best_score_tree_u = grid_search.best_score_

    best_model_tree_u = grid_search.best_estimator_
    predict_tree_u = best_model_tree.predict(features_test_u)
    tree_roc_auc_u = roc_auc_score(target_test_u,predict_tree_u)


    # Random Forest Upsample

    param_grid = {
        'n_estimators':[20,40,50,100],
        'max_depth':[None,3,5,7,9,11],
        'min_samples_split': [2, 5, 10]
    }

    grid_search = GridSearchCV(
        estimator=RandomForestClassifier(
            random_state = random_state), 
            param_grid=param_grid, 
            cv=5, 
            scoring='roc_auc')

    grid_search.fit(features_train_u, target_train_u)

    best_score_rfu = grid_search.best_score_

    best_model_rfu = grid_search.best_estimator_
    predict_forestu = best_model_rf.predict(features_test_u)
    rforest_roc_auc_u = roc_auc_score(target_test_u,predict_forestu)


    # Logistic Regression Upsample

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

    grid_search.fit(features_train_u, target_train_u)

    best_score_LRu = grid_search.best_score_

    best_model_LRu = grid_search.best_estimator_
    predict_lr_u = best_model_LR.predict(features_test_u)
    LR_roc_auc_u = roc_auc_score(target_test_u,predict_lr_u)


    # Lightgbm Upsample

    train_data_u = lgb.Dataset(features_train_u,label=target_train_u)
    test_data_u = lgb.Dataset(features_test_u,label=target_test_u)
    params = {
        'objective': 'binary',  
        'metric': 'binary_logloss', 
        'boosting_type': 'gbdt',
        'num_leaves': 31,
        'learning_rate': 0.05,
        'feature_fraction': 0.9
    }
    num_round = 100
    bts_u = lgb.train(params, train_data_u, num_round, valid_sets=[test_data_u])
    lgb_predict_u = bts.predict(features_test_u,num_iteration=bts.best_iteration)
    lgb_score_u = roc_auc_score(target_test_u,lgb_predict_u)

    # CatBoost Upsample

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

    grid_search.fit(features_train_u, target_train_u)

    best_score_CBu = grid_search.best_score_

    best_model_CBu = grid_search.best_estimator_
    predict_cb_u = best_model_CB.predict(features_test_u)
    CB_score_u = roc_auc_score(target_test_u,predict_cb_u)


    # Neural Network Upsample 

    model_NN_u = Sequential()
    model_NN_u.add(Dense(units=32, activation='relu'))
    model_NN_u.add(Dense(units=1, activation='sigmoid'))
    model_NN_u.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model_NN_u.fit(
        features_train_u.values, target_train_u.values, epochs=5, batch_size=32, validation_data=(features_test_u.values, target_test_u.values))
    neu_net_predict_u = model_NN.predict(features_test_u.values)
    neu_net_score_u = roc_auc_score(target_test_u,neu_net_predict_u)



    scores = {
        'Dummy Classifier': dummy_roc_auc,
        'Decision Tree': tree_roc_auc,
        'Random Forest': rforest_roc_auc,
        'Logistic Regression': LR_roc_auc,
        'LightGBM': lgb_score,
        'CatBoost': CB_roc_auc,
        'Neural Network': neu_net_score,
        'Dummy Classifier Upsample' : dummy_roc_auc_u,
        'Decision Tree Upsample': tree_roc_auc_u,
        'Random Forest Upsample': rforest_roc_auc_u,
        'Logistic Regression Upsample': LR_roc_auc_u,
        'LightGBM Upsample': lgb_score_u,
        'CatBoost Upsample': CB_score_u,
        'Neural Network Upsample': neu_net_score_u,
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
    elif best_model_name == 'LightGBM':
            best_model = bts
            best_model_score = lgb_score
    elif best_model_name == 'CatBoost':
            best_model = best_model_CB
            best_model_score = best_score_CB
    elif best_model_name == 'Neural Network':
            best_model = model_NN 
            best_model_score = neu_net_score
    elif best_model_name == 'Dummy Classifier Upsample':
            best_model = model_dumy_u
            best_model_score = dummy_roc_auc_u
    elif best_model_name == 'Decision Tree Upsample':
            best_model = best_model_tree_u
            best_model_score = best_score_tree_u
    elif best_model_name == 'Random Forest Upsample':
            best_model = best_model_rfu
            best_model_score = best_score_rfu
    elif best_model_name == 'Logistic Regression Upsample':
            best_model = best_model_LRu
            best_model_score = best_score_LRu
    elif best_model_name == 'LightGBM Upsample':
            best_model = bts_u
            best_model_score = lgb_score_u
    elif best_model_name == 'CatBoost Upsample':
            best_model = best_model_CBu
            best_model_score = best_score_CBu
    elif best_model_name == 'Neural Network Upsample':
            best_model = model_NN_u
            best_model_score = neu_net_score_u
        

    return best_model, best_model_name, best_model_score 