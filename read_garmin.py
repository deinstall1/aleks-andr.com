import sqlite3

db_path = '/Users/aleksandrandrienko/HealthData/DBs/garmin_activities.db'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT * FROM activities ORDER BY start_time DESC LIMIT 10;")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
