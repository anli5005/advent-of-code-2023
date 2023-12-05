from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime.now(tz=ZoneInfo("America/New_York"))
print(dt.year)