import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score

data = pd.read_csv('/Users/zacharynemnijones/Desktop/glass.csv')

def threshold_analysis(column):
    X = data[[column]]
    y = data['Type']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
    model.fit(X_train_scaled, y_train)
    probabilities = model.predict_proba(X_test_scaled)
    
    thresholds = np.arange(0.1, 1.0, 0.1)
    results = []
    for t in thresholds:
        y_pred_custom = (probabilities >= t).astype(int)
        y_pred_custom = np.argmax(y_pred_custom, axis=1) + 1  # assuming class labels start at 1
        accuracy = accuracy_score(y_test, y_pred_custom)
        precision = precision_score(y_test, y_pred_custom, average='macro', zero_division=0)
        recall = recall_score(y_test, y_pred_custom, average='macro', zero_division=0)
        results.append((t, accuracy, precision, recall))
    
    return results

threshold_results_al = threshold_analysis('Al')

print("Threshold results for 'Al':", threshold_results_al)

for col in data.columns.drop('Type'):
    print(f"Threshold results for {col}:", threshold_analysis(col))

X_all_features = data.drop('Type', axis=1)
y_all_features = data['Type']

X_train_full, X_test_full, y_train_full, y_test_full = train_test_split(X_all_features, y_all_features, test_size=0.2, random_state=42)

from sklearn.pipeline import make_pipeline
pipeline = make_pipeline(StandardScaler(), LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000))
pipeline.fit(X_train_full, y_train_full)

y_pred_full = pipeline.predict(X_test_full)
full_accuracy = accuracy_score(y_test_full, y_pred_full)
full_precision = precision_score(y_test_full, y_pred_full, average='macro', zero_division=0)
full_recall = recall_score(y_test_full, y_pred_full, average='macro', zero_division=0)

print("Full model performance:")
print("Accuracy:", full_accuracy)
print("Precision:", full_precision)
print("Recall:", full_recall)
