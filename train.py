from numpy.testing import verbose
import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report



df = pd.read_csv("processed_data/clean_train.csv")

x = df.drop(['Loan_ID', 'Loan_Status'], axis =1)
y = df['Loan_Status']

x_train, x_temp, y_train, y_temp = train_test_split(x, y, test_size=0.2, random_state=42)

x_val, x_test, y_val, y_test = train_test_split(x_temp, y_temp, test_size=0.5, random_state=42)

model =XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
model.fit(x_train, y_train, eval_set=[(x_val, y_val)], verbose=False)

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"--- 模型訓練完成 ---")
print(f"測試集準確度 (Accuracy): {accuracy:.2%}")
print("\n--- 詳細分類報告 ---")
print(classification_report(y_test, y_pred))

os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/loan_model_v1.pkl')
print("模型已儲存至 models/loan_model_v1.pkl")