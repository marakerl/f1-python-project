import fastf1 
import os 

#SETUP CACHE
# We create a folder for data so we don't download it twice
if not os.path.exists('cashe'):
    os.makedirs('cashe') 

#SELECT SESSION
#Year, Location, Session ('R' = Race, 'Q' = Qualifyinf) 
year = 2025
location = 'Silverstone'
session_type = 'R' 

print(f"Requesting data for {year} {location}...")

#LOAD DATA
session = fastf1.get_session(year, location, session_type)
session.load()

# PRINT SUMMARY
print("\n--- Session Loaded Successfully ---")
print(f"Event: {session.event['EventName']}")
print(f"Winner: {session.results.loc[0, 'FullName']}")

# Display the Top 5 finishers
print("\n--- Top 5 Finishers ---")
print(session.results[['Abbreviation', 'TeamName', 'ClassifiedPosition']].head(5))


