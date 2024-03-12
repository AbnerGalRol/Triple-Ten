# Beta Bank

Beta Bank's customers are leaving, gradually, every month. Bankers have discovered that it's cheaper to retain existing customers than to attract new ones.

We need to predict if a customer will leave the bank soon. You have data on customers' past behavior and contract terminations with the bank.

Create a model with the highest possible F1 score. To pass the review, you need an F1 score of at least 0.59. Check the F1 score for the test set.

Additionally, you should measure the AUC-ROC metric and compare it with the F1 score.

## Project Instructions

Download and prepare the data. Explain the procedure.

Examine class balance. Train the model without considering class imbalance. Briefly describe your findings.

Improve the model's quality. Make sure to use at least two approaches to correct class imbalance. Use training and validation sets to find the best model and parameter set. Train different models on the training and validation sets. Find the best one. Briefly describe your findings.

Perform the final test.

## Data Description

You can find the data in the /datasets/Churn.csv file. Download the dataset.

Features

RowNumber: index string
CustomerId: unique customer identifier
Surname: last name
CreditScore: credit score
Geography: country of residence
Gender: gender
Age: age
Tenure: period over which a customer's fixed-term deposit has matured (years)
Balance: account balance
NumOfProducts: number of banking products used by the customer
HasCrCard: whether the customer has a credit card (1 - yes; 0 - no)
IsActiveMember: customer activity (1 - yes; 0 - no)
EstimatedSalary: estimated salary
