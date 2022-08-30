players = ['charles','martina','michael','florence','eli']
#print(players[0:3])
#print(players[1:4])
#print(players[:4])
#print(players[2:])
#print(players[-3:]) #last 3 
#print(players[0:3:2]) #skip the quantity of the third value, if doesnt
					  #values in this range, doesnt show it

print('Here are the first three players of my team: ')
for player in players[:3]:
	print(player.title())