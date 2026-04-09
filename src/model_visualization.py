import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

data = pd.read_csv('data/processed_data.csv')

X = data[['Sector1Time','Sector2Time','Sector3Time','temperature','season_points']]
y = data['LapTime']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = GradientBoostingRegressor()
model.fit(X_train,y_train)

predictions = model.predict(X_test)

plt.scatter(y_test, predictions)

plt.xlabel("Actual Lap Time")
plt.ylabel("Predicted Lap Time")

plt.title("Model Prediction vs Actual")

plt.savefig("results/model_prediction_vs_actual.png")

plt.show()