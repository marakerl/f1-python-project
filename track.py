import fastf1 
import fastf1.plotting
import os 
import numpy as np
import matplotlib
matplotlib.use('TkAgg') # Or 'Qt5Agg' if you have PyQt installed
import matplotlib.pyplot as plt
import time


#RACE
year = 2025
gp = 'manza'
identifier = 'R'
driver1 = 'NOR'
driver2 = 'VER'

# SETUP CACHE (The Safety Check)
cache_dir = 'cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)
    print(f"Created missing directory: {cache_dir}")
fastf1.Cache.enable_cache(cache_dir)



session = fastf1.get_session(year, gp, identifier)
session.load(telemetry=True, laps=True)

#get fastest laps
lap_driver1 = session.laps.pick_drivers(driver1).pick_fastest()
lap_driver2 = session.laps.pick_drivers(driver2).pick_fastest()

#Get telemetry of the driver for fastest lap
telemetry_driver1 = lap_driver1.get_telemetry()
telemetry_driver2 = lap_driver2.get_telemetry()

#figure
fig, ax = plt.subplots(figsize=(8,8))

#
color1 = fastf1.plotting.get_driver_color(driver1, session=session)
color2 = fastf1.plotting.get_driver_color(driver2, session=session)

#Dots for driver
dot_driver1, = ax.plot([],[], color=color1, marker='o', label=driver1)
dot_driver2, = ax.plot([],[], color=color2, marker='o', label=driver2)

telemetry_driver1['RelativeTime'] = (telemetry_driver1['Time'] - telemetry_driver1['Time'].iloc[0]).dt.total_seconds()
telemetry_driver2['RelativeTime'] = (telemetry_driver2['Time'] - telemetry_driver2['Time'].iloc[0]).dt.total_seconds()

ax.plot(telemetry_driver1['X'], telemetry_driver1['Y'], color= 'black', alpha = 0.3)

ax.legend()

max_time = min(telemetry_driver1['RelativeTime'].max(), telemetry_driver2['RelativeTime'].max())

for current_time in np.arange(0,max_time,0.1):

    idx_driver1 = np.abs(telemetry_driver1['RelativeTime'] - current_time).argmin()
    idx_driver2 = np.abs(telemetry_driver2['RelativeTime'] - current_time).argmin()

    dot_driver1.set_data([telemetry_driver1['X'].iloc[idx_driver1]],[telemetry_driver1['Y'].iloc[idx_driver1]])
    dot_driver2.set_data([telemetry_driver2['X'].iloc[idx_driver2]],[telemetry_driver2['Y'].iloc[idx_driver2]])

    plt.draw()
    plt.pause(0.001)

    print(f"Car moved to row {idx_driver1} at {telemetry_driver1['RelativeTime'].iloc[idx_driver1]}s")
    print(f"Car moved to row {idx_driver2} at {telemetry_driver2['RelativeTime'].iloc[idx_driver2]}s")

plt.show()

