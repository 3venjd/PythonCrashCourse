from matplotlib import pyplot as plt

x_values = range(1, 5000)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c= y_values, cmap=plt.cm.Blues, s=10)


ax.set_title("Cubic Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cubic of Value", fontsize = 14)


ax.axis([0, x_values[-1], 0, y_values[-1]])

plt.show()
