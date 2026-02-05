import fastf1
from matplotlib import pyplot as plt
import numpy as np
import os

#RACE
year = 2025
gp = 'Silverstone'
identifier = 'R'
driver = 'LAN'


fastf1.Cache.enable_cache(cache_dir)
session = fastf1.get_session(year, gp, identifier)
session.load()

# 2. Get the Fastest Lap of the Winner
# We use pick_fastest() to get the single best lap of the whole race
drivers_laps = session.laps.pick_drivers(f'{driver}')
fastest_lap = session.laps.pick_fastest()


# 3. Get Telemetry (Distance, Time, Speed, X, Y)
# get_telemetry() gives us the high-frequency car data
telemetry = fastest_lap.get_telemetry()
x = telemetry['X']
y = telemetry['Y']
speed = telemetry['Speed']

# Create the Visualization
plt.figure(figsize=(10, 10))

# Plot the X and Y coordinates
# We use a white line on a dark background for that "F1 Tech" look
plt.plot(telemetry['X'], telemetry['Y'], color='white', linewidth=2)

# 5. Final Styling
plt.title(f"Track Layout: {session.event['EventName']} {session.event['EventDate'].year}\n"
          f"Fastest Lap by {fastest_lap['Driver']}", color='white')

# IMPORTANT: axis('equal') prevents the track from looking stretched or squashed
plt.axis('equal') 

# Make it look "Pro" with a dark background
plt.gca().set_facecolor('grey')
plt.gcf().set_facecolor('grey')
plt.axis('off') # Hide the grid lines and numbers

plt.savefig(f'track.png', dpi=300)
print(f"Track map saved as track.png")

