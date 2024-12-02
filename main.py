import datetime
import webbrowser
import os, sys




def get_correct_date():
    now_utc = datetime.datetime.now(datetime.UTC)
    utc_offset = datetime.timedelta(hours=-5)
    adjusted_time = now_utc + utc_offset

    if adjusted_time.hour < 0:  # If it's between 0h and 5h UTC
        adjusted_time -= datetime.timedelta(days=1)

    return adjusted_time.year, adjusted_time.month, adjusted_time.day


def create_file(year, day):

    print(f"Creating folder for {year}/day{day}...")

    os.makedirs(f"{year}/day{day}") 
    
    template = ""
    with open("template.txt", "r", encoding="utf-8") as file:
        template = file.read()

    with open(f"{year}/day{day}/day{day}.py", "w", encoding="utf-8") as file:
        file.write(template.replace("{real_year}", str(year)).replace("{real_day}", str(day)))

    with open(f"{year}/day{day}/input.txt", "w") as file:
        pass
    with open(f"{year}/day{day}/test.txt", "w") as file:
        pass

    webbrowser.open(f"https://adventofcode.com/{year}/day/{day}")
    webbrowser.open(f"https://adventofcode.com/{year}/day/{day}/input")




if __name__ == "__main__":
    year, current_month, day = get_correct_date()
    current_year = year
    file_path = f"{year}/day{day}/day{day}.py"

    args = sys.argv
    parameters = args[1:]

    if len(parameters) > 1:
        try:
            if len(parameters) == 1: # if we just entered the day
                param1 = int(parameters[0])
                if param1 < 26:
                    day = param1
                else:
                    year = param1
            else:
                param1 = int(parameters[0])
                param2 = int(parameters[1])
                if param1 < 26:
                    day = param1
                    year = param2
                else:
                    day = param2
                    year = param1
            file_path = f"{year}/day{day}/day{day}.py"
        except:
            print("Invalid arguments.")
            day, year, file_path = 0, 0, "error/"

    else:
        # check if we're in december
        if (current_month == 12) and (day < 26):
            if not(os.path.exists(file_path)):
                create_file(year, day)

    while not(os.path.exists(file_path)):
        if (year >= 2015) and (year <= current_year) and (day < 26):
            create_file(year, day)
            break

        parameters = input("[year] [day]: ").split()
        try:
            param1 = int(parameters[0])
            param2 = int(parameters[1])
            if param1 < 26:
                day = param1
                year = param2
            else:
                day = param2
                year = param1
            file_path = f"{year}/day{day}/day{day}.py"
        except:
            print("Invalid arguments.")
            day, year, file_path = 0, 0, "error/"

    print(f"\n\033[91m☆ {year} - Day {day} ☆\033[0m")
    os.system(f"python {year}/day{day}/day{day}.py")