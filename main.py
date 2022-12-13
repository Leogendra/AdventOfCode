import os
from datetime import datetime
year = datetime.now().year
day = datetime.now().day
print(f"☆ {year} DAY {day} ☆")
os.system(f"python {year}/day{day}/day{day}.py")