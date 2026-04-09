import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor

data = pd.read_csv('data/processed_data.csv')

X = data[['Sector1Time','Sector2Time','Sector3Time','temperature','season_points']]
y = data['LapTime']

model = GradientBoostingRegressor()
model.fit(X,y)

importance = model.feature_importances_

features = X.columns

plt.bar(features, importance)

plt.title("Feature Importance for Lap Time Prediction")
plt.xlabel("Feature")
plt.ylabel("Importance")

plt.show()