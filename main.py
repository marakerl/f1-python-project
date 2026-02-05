import fastf1 
import os 
import numpy as np

#RACE
year = 2025
gp = 'Monza'
identifier = 'R'
driver = 'LAN'

# SETUP CACHE (The Safety Check)
cache_dir = 'cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)
    print(f"Created missing directory: {cache_dir}")
fastf1.Cache.enable_cache(cache_dir)



session = fastf1.get_session(year, gp, identifier)
session.load(telemetry=True, laps=True)

fastestlap = session.laps.pick_fastest()

telemetry = fastestlap.get_telemetry()

# The 'Time' column is cumulative from the start of the session.
# We subtract the time at the very first row to make the lap start at 0.0 seconds.
telemetry['RelativeTime'] = (telemetry['Time'] - telemetry['Time'].iloc[0]).dt.total_seconds()

#print(telemetry[['Time', 'RelativeTime']].head())
'''
target_time = 30.0 #sec

difference = np.abs(telemetry['RelativeTime']-target_time) #Vad är distansen från alla relativetime till targettime 

best_index = difference.argmin() #Index på närmaste raden 

row_at_10s = telemetry.iloc[best_index] #Närmaste raden


print(f"At {target_time}s, speed was: {row_at_10s['Speed']} km/h")

print(f"Is the driver braking: {row_at_10s['Brake']}")'''



start_of_lap = telemetry.iloc[:100].copy()

speed_delta = np.diff(start_of_lap['Speed']*(5/18))

time_delta = np.diff(start_of_lap['RelativeTime'])

acc_values = speed_delta/time_delta

acc_padded = np.insert(acc_values,0,0)

start_of_lap['acc'] = acc_padded

mask = start_of_lap['acc'] < 0

negAcc = start_of_lap[mask]

print(negAcc[['Speed','acc', 'RelativeTime', 'Brake']]) 





''' mask_300 = (telemetry['Speed'] > 300) & (telemetry['nGear'] < 8)

fast_rows = telemetry[mask_300]

print(f"Total rows in telemetry:  {len(telemetry)}")
print(f"Total rows where speed > 300 and gear 1:  {len(fast_rows)}")

if not fast_rows.empty:
    print(fast_rows[['Time', 'Speed', 'nGear']])
else:
    print("No rows found! (An F1 car isn't usually in 1st gear above 300 km/h)")

'''
