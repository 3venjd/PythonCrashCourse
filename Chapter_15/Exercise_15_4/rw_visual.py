import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize = (15,9))

point_numbers = range(rw.num_points)

ax.plot(rw.x_values, rw.y_values)

plt.show()