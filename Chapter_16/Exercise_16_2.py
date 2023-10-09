import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'Chapter_16\data\death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    datesValley, highsValley, lowsValley = [],[],[]

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')

        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")  
        else:
            datesValley.append(current_date)
            highsValley.append(high)
            lowsValley.append(low)

filename = 'Chapter_16\data\sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file
    datesSitka, highsSitka, lowsSitka = [],[],[]

    #Get high temperatyres from this file
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        datesSitka.append(current_date)
        highsSitka.append(high)
        lowsSitka.append(low)


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(datesValley,highsValley, c= 'green', alpha = 0.5)
ax.plot(datesValley, lowsValley, c='yellow', alpha = 0.5)
ax.plot(datesSitka,highsSitka, c= 'red', alpha = 0.5)
ax.plot(datesSitka, lowsSitka, c='blue', alpha = 0.5)
ax.fill_between(datesValley, highsValley, lowsValley, facecolor = 'yellow', alpha = 0.1)
ax.fill_between(datesSitka, highsSitka, lowsSitka, facecolor = 'blue', alpha = 0.1)

#Format plot
ax.set_title("Compare Temperatures", fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize = 16)
ax.tick_params(axis='both', which = 'major', labelsize = 16)

plt.show()