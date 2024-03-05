import pandas as pd
from procesamiento import procesamiento
from best_model import model_selection

contract = pd.read_csv(r'data/contract.csv')
personal = pd.read_csv(r'data/personal.csv')
internet = pd.read_csv(r'data/internet.csv')
phone = pd.read_csv(r'data/phone.csv')

features_train_ohe, features_test_ohe, target_train_ohe, target_test_ohe = procesamiento(contract,personal,internet,phone)

besto_model, besto_model_name, best_model_score = model_selection(features_train_ohe, features_test_ohe, target_train_ohe, target_test_ohe)

print("Best Model:", besto_model_name)
print("Best Model Score (AUC-ROC):", best_model_score)