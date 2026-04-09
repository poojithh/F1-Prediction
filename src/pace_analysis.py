import fastf1
import pandas as pd
import matplotlib.pyplot as plt

fastf1.Cache.enable_cache('cache')

session = fastf1.get_session(2024, 'Australian Grand Prix', 'R')
session.load()

laps = session.laps[['Driver','LapTime']].dropna()
laps['LapTime'] = laps['LapTime'].dt.total_seconds()

drivers = laps['Driver'].unique()[:5]

for driver in drivers:
    driver_laps = laps[laps['Driver'] == driver]
    plt.plot(driver_laps['LapTime'], label=driver)

plt.title("Driver Pace Comparison - Australian GP")
plt.xlabel("Lap Number")
plt.ylabel("Lap Time (seconds)")
plt.legend()

plt.show(