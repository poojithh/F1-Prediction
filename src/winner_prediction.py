import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('data/processed_data.csv')

# Simplified winner feature
data['Winner'] = data.groupby('Driver')['LapTime'].transform('mean') == data['LapTime'].min()

X = data[['Sector1Time','Sector2Time','Sector3Time','temperature','season_points']]
y = data['Winner']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = RandomForestClassifier()
model.fit(X_train,y_train)

pred = model.predict(X_test)

accuracy = accuracy_score(y_test,pred)

print("Winner Prediction Accuracy:", accuracy)