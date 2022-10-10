from weather import *

file = "weather.dat"

prompt = """
        *** TUFFY TITAN WEATHER LOGGER MAIN MENU

1. Set data filename
2. Add weather data
3. Print daily report
4. Print historical report
9. Exit the program
"""

response = 0
while(True):
    print("""
        *** TUFFY TITAN WEATHER LOGGER MAIN MENU

        1. Set data filename
        2. Add weather data
        3. Print daily report
        4. Print historical report
        9. Exit the program\n""")
    response = int(input("Enter menu choice: "))
    if response == 1:
        myfile = input("\nEnter data filename: ")
        weather = read_data(filename=myfile)
    elif response == 2:
        dt = input("\nEnter date (YYYYMMDD): ")
        tm = input("Enter time (hhmmss): ")
        tmp = int(input("Enter temperature: "))
        hmd = int(input("Enter humidity: "))
        rain = float(input("Enter rainfall: "))
        weather[dt+tm] = {'t': tmp, 'h': hmd, 'r':rain}
        weather = write_data(weather, myfile)
    elif response == 3:
        date = input("\nEnter date (YYYYMMDD): ")
        display = report_daily(weather, date)
        print(display)
    elif response == 4:
        display = report_daily(weather)
        print(display)
    elif response == 9:
        break
    else:
        continue

# while(response != 9):
#     if(response == 1):
#         weather.read_data(filename='wthr.dat')
#     print('Hello World')
#     print(prompt)
#     response = int(input("Enter menu choice: "))
