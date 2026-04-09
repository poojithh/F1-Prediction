import fastf1
import pandas as pd

fastf1.Cache.enable_cache('cache')

def get_race_data(year, race):
    session = fastf1.get_session(year, race, 'R')
    session.load()

    laps = session.laps[['Driver','LapTime','Sector1Time','Sector2Time','Sector3Time']]
    laps = laps.dropna()

    laps['LapTime'] = laps['LapTime'].dt.total_seconds()

    return laps

race1 = get_race_data(2024, 'Australian Grand Prix')
race2 = get_race_data(2024, 'Bahrain Grand Prix')
race3 = get_race_data(2024, 'Miami Grand Prix')

data = pd.concat([race1, race2, race3])

data.to_csv('data/race_data.csv', index=False)

print("Race data saved")
