#alien_0 = {'color' : 'green', 'points' : 5}

#print(alien_0['color'])
#print(alien_0['points'])

#new_points = alien_0['points']
#print(f'You just earned {new_points} points')

#print(alien_0)
#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)

#alien_0 = {}
#alien_0['color'] = 'green'
#alien_0['points'] = 5

#print(alien_0)

#alien_0 = {'color' : 'green'}
#print(f"the alien is {alien_0['color']}")

#alien_0['color'] = 'yellow'
#print(f"the alien is now {alien_0['color']}")

#alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
#print(f"Original position: {alien_0['x_position']}")

# move the alien to the right
# determine how far to move the alien based on its current speed

#if alien_0['speed'] == 'slow':
#	x_increment = 1
#elif alien_0['speed'] == 'medium':
#	x_increment = 2
#else:
	#this must be a fast alien
#	x_increment = 3

#the new position is the old position plus the incremenet
#alien_0['x_position'] = alien_0['x_position'] + x_increment

#print(f"new position : {alien_0['x_position']}")

#alien_0 = {'color' : 'green', 'points' : 5}
#print(alien_0)

#del alien_0['points']
#print(alien_0)

#alien_0 = {'color' : 'green', 'points' : 5}
#alien_1 = {'color' : 'yellow', 'points' : 10}
#alien_2 = {'color' : 'red', 'points' : 15}

#aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
#	print(alien)

#make an empty list for storing aliens
aliens = []

#Make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color' : 'green', 'point' : 5, 'speed' : 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['point'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['point'] = 15

#show the first 5 aliens
for alien in aliens[:5]:
	print(alien)
print("...")

#show many aliens have been created
print(f"Total number of aliens: {len(aliens)}")