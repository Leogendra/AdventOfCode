from datetime import datetime
import webbrowser
import os, sys



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
    year = datetime.now().year
    day = datetime.now().day
    file_path = f"{year}/day{day}/day{day}.py"

    args = sys.argv
    parameters = args[1:]

    if len(parameters) > 1:
        try:
            if len(parameters) == 1: # if we just entered the day
                day = int(parameters[0])
            else:
                year = int(parameters[0])
                day = int(parameters[1])
            file_path = f"{year}/day{day}/day{day}.py"
        except:
            pass # If the args are wrong (char, etc)

    else:
        # check if we're in december
        if (datetime.now().month == 12) and (day < 26):
            create_file(year, day)

    while not os.path.exists(file_path):
        if (year >= 2015) and (year <= datetime.now().year) and (day < 26):
            create_file(year, day)
            break

        year, day = input("[year] [day]: ").split()
        file_path = f"{year}/day{day}/day{day}.py"


    print(f"\n\033[91m☆ {year} - Day {day} ☆\033[0m")
    os.system(f"python {year}/day{day}/day{day}.py")