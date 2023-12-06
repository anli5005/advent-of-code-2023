from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import time

tz = ZoneInfo("America/New_York")
dt = datetime.now(tz=tz)

# Figure out the start of the next day
dt = dt.replace(hour=0, minute=0, second=0, microsecond=1000)
dt += timedelta(days=1)

print(f"Waiting until {dt}")

# Determine the time delta
delta = dt - datetime.now(tz=tz)

# Sleep until the next day
seconds = delta.total_seconds()
print(f"Sleeping for {seconds} seconds...")
if seconds > 0:
    time.sleep(seconds)