import fastf1
from matplotlib import pyplot as plt
import numpy as np
import os

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
session.load()

# 2. Get the Fastest Lap of the Winner
# We use pick_fastest() to get the single best lap of the whole race
drivers_laps = session.laps.pick_drivers(f'{driver}')
fastest_lap = drivers_laps.pick_fastest()
