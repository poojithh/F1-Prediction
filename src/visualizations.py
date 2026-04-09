import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/processed_data.csv')

plt.hist(data['LapTime'], bins=50)

plt.title("Lap Time Distribution")
plt.xlabel("Lap Time (seconds)")
plt.ylabel("Frequency")

plt.savefig("results/lap_time_distribution.png")

plt.show()

# Driver Average Pace Comparision
driver_avg = data.groupby('Driver')['LapTime'].mean().sort_values()

plt.figure()


driver_avg.plot(kind='bar')

plt.title("Average Driver Lap Time")
plt.xlabel("Driver")
plt.ylabel("Average Lap Time (seconds)")

plt.savefig("results/driver_average_pace.png")

plt.show()

#Sector Time Contribution

sector_data = data[['Sector1Time','Sector2Time','Sector3Time']].mean()

plt.figure()

sector_data.plot(kind='bar')

plt.title("Average Sector Times")
plt.xlabel("Track Sector")
plt.ylabel("Time (seconds)")

plt.savefig("results/sector_time_comparison.png")

plt.show()