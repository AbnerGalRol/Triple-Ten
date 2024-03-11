import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

def procesamiento(contract,personal,internet,phone):

    datasets = [contract,personal,internet,phone]

    # Cambiamos el formato de los nombres de las columnas a minúsculas para manipular mejor los datos
    for i in datasets:
        i.columns = [j.lower() for j in i.columns]

    # Convertimos la columna begindate a el formato datetime
    contract['begindate'] = pd.to_datetime(contract['begindate'])

    # Convertimos los datos de la columna a números y llenamos con NaN's aquellos que no podemos cambiar
    contract.totalcharges = pd.to_numeric(contract['totalcharges'],errors='coerce')
    # Elimínanos las observaciones con NaN's
    contract.dropna(inplace=True)

    # Unimos todos nuestros datasets en uno solo
    final_df = contract.merge(personal,how='inner').merge(internet,how='left').merge(phone,how='left')

    # Llenamos los valores ausentes en las respectivas columnas
    fillna_columns = list(internet.drop(columns=['customerid','internetservice']).columns)
    final_df[['multiplelines','internetservice']] = final_df[['multiplelines','internetservice']].fillna('NA')
    final_df[fillna_columns] = final_df[fillna_columns].fillna('No')

    # Cambiamos todos los datos de fechas en la columna `enddate` a 'Si'.
    final_df.enddate = final_df.enddate.apply(lambda x: 'Yes' if x != 'No' else 'No')

    # Usamos el método OHE para codificar nuestras columnas categóricas.
    ohe_columns = final_df.drop(columns=['customerid','begindate','seniorcitizen','monthlycharges','totalcharges']).columns
    final_df_ohe = pd.get_dummies(final_df,columns=ohe_columns,drop_first=True,dtype=int)

    # Creamos una semilla
    random_state = 12345
    
    # Dividimos nuestros datos en target y features
    features_ohe = final_df_ohe.drop(columns=['enddate_Yes','customerid','begindate'])
    target_ohe = final_df_ohe.enddate_Yes

    # Dividimos nuestros datasets en entrenamiento y prueba
    features_train_ohe, features_test_ohe, target_train_ohe, target_test_ohe = train_test_split(
        features_ohe, target_ohe, test_size=0.2,random_state=random_state)
    
    return features_train_ohe, features_test_ohe, target_train_ohe, target_test_ohe