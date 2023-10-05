from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create a D6 and D10
die_1 = Die()
die_2 = Die(10)


# Make some rolls, and store results in a list
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll() #1
    results.append(result)

# Analyze the results
frequencies = []
max_results = die_1.num_sides + die_2.num_sides #2
for value in range(2, max_results + 1): #3
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results 
x_values = list(range(2, max_results + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1} # dtick is the space between the x-axis
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling D6 dice and D10 50000 times', xaxis= x_axis_config, yaxis= y_axis_config)
offline.plot({'data' : data, 'layout':my_layout}, filename='Chapter_15\Die\d6_d10.html')

print(frequencies)