from logging import critical
from operator import truediv


prompt = "\nPlease enter the name of a city you have visitied: "
prompt += "\n(Enter 'quit' when you finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")