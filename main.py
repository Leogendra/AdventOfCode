from datetime import datetime
import webbrowser
import os, sys



def create_file(year, day):

    print(f"Création du répertoire {year}/day{day}...")

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

    try:
        if len(parameters) == 1:
            day = parameters[0]
        else:
            year = parameters[0]
            day = parameters[1]
        file_path = f"{year}/day{day}/day{day}.py"
    except:
        pass

    while not os.path.exists(file_path):
        # check si on est en décembre
        if (datetime.now().month == 12) and (datetime.now().day < 26):
            create_file(year, day)
            break

        year, day = input("[year] [day]: ").split()
        file_path = f"{year}/day{day}/day{day}.py"
        

    print(f"\n\033[91m☆ {year} DAY {day} ☆\033[0m")
    os.system(f"python {year}/day{day}/day{day}.py")