import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'Chapter_16\data\sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file
    dates, rainfalls = [],[]

    #Get high temperatyres from this file
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')

        try:
            rainfall = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)

    #Plot the high and low temperatures
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates,rainfalls, c= 'red')

    #Format plot
    ax.set_title("Daily Rainfalls - 2018", fontsize = 24)
    ax.set_xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    ax.set_ylabel("Rainfall", fontsize = 16)
    ax.tick_params(axis='both', which = 'major', labelsize = 16)

    plt.show()

for data in dates:
    print(data)