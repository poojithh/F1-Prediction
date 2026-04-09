import pandas as pd

# Load collected race data
data = pd.read_csv('data/race_data.csv')

# Convert sector times to seconds
data['Sector1Time'] = pd.to_timedelta(data['Sector1Time']).dt.total_seconds()
data['Sector2Time'] = pd.to_timedelta(data['Sector2Time']).dt.total_seconds()
data['Sector3Time'] = pd.to_timedelta(data['Sector3Time']).dt.total_seconds()

# Example engineered features
data['temperature'] = 30
data['season_points'] = data.groupby('Driver').cumcount()
data['wet_performance_factor'] = 0.5

# Save processed dataset
data.to_csv('data/processed_data.csv', index=False)

print("Feature engineering complete. Processed dataset saved.")