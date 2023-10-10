import os
from datetime import datetime
year = datetime.now().year
day = datetime.now().day
file_path = f"{year}/day{day}/day{day}.py"

while not os.path.exists(file_path):
    year = input("year: ")
    day = input("day: ")
    file_path = f"{year}/day{day}/day{day}.py"
    
print(f"☆ {year} DAY {day} ☆")
os.system(f"python {file_path}")