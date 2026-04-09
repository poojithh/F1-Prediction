import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

data = pd.read_csv('data/processed_data.csv')

X = data[['Sector1Time','Sector2Time','Sector3Time','temperature','season_points','wet_performance_factor']]
y = data['LapTime']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = GradientBoostingRegressor()
model.fit(X_train,y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test,predictions)

print("Model MAE:", mae)