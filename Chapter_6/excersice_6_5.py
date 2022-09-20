rivers = {'nile' : 'egypt', 'amazon' : 'peru', 'mississippi' : 'montana', 'chang jiang' : 'china', 'ob' : 'russia'}


for river, country in rivers.items():
	print(f"\n{river} runs through {country}")

for river in rivers.values():
	print(f"\n{river}")

for country in rivers.keys():
	print(f"\n{country}")