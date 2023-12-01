import os
from datetime import datetime
year = datetime.now().year
day = datetime.now().day
print(f"\n\033[91m☆ {year} DAY {day} ☆\033[0m")
os.system(f"python {year}/day{day}/day{day}.py")