import os, sys
from datetime import datetime
year = datetime.now().year
day = datetime.now().day
file_path = f"{year}/day{day}/day{day}.py"

args = sys.argv
parameters = args[1:]

try:
    year = parameters[0]
    day = parameters[1]
    file_path = f"{year}/day{day}/day{day}.py"
except:
    pass

while not os.path.exists(file_path):
    year, day = input("[year] [day]: ").split()
    file_path = f"{year}/day{day}/day{day}.py"
    
print(f"☆ {year} DAY {day} ☆")
os.system(f"python {file_path}")