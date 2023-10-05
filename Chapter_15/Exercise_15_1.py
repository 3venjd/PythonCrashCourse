from matplotlib import pyplot as plt

x_values = range(1,6)
y_values = [x**3 for x in x_values ]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(x_values,y_values,linewidth = 4)

ax.set_title("Cubic numbers", fontsize = 24)
ax.set_xlabel("Values", fontsize = 24)
ax.set_ylabel("Cubic of value", fontsize = 14)

ax.axis([0, x_values[-1],0, y_values[-1]])

print(x_values[-1])

plt.show()