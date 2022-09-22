person1 = {
			'first_Name' : 'Ringa', 
			'Last_Name' : 'Tech', 
			'Age' : 30, 
			'City' : 'Frankfurt'
		}

person2 = {
			'first_Name' : 'Hector', 
			'Last_Name' : 'de leon', 
			'Age' : 34, 
			'City' : 'Mexico Df'
}

person3 = {
			'first_Name' : 'Dalto', 
			'Last_Name' : 'Web advance', 
			'Age' : 28, 
			'City' : 'Buenos aires'
}

people = {
			'Rtech' : person1,
			'HdeLeon' : person2,
			'YoSoyDalto' : person3
		}

for person,person_Detail in people.items():
	print(f"the user: {person} "
			f"the real name is {person_Detail['first_Name']} "
			f"{person_Detail['Last_Name']} and the age are "
			f"{person_Detail['Age']} old and lives in "
			f"{person_Detail['City']}")
