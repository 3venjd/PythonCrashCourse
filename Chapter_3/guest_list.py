guests = ['Cristina', 'Jr', 'Tiago', 'Rosa']
#print(f"you {guests[0]} are invite to a dinner with me")
#print(f"you {guests[1]} are invite to a dinner with me")
#print(f"you {guests[2]} are invite to a dinner with me")
#print(f"you {guests[3]} are invite to a dinner with me")

#print(f"{guests[2]} can't go to the dinner")
#del guests[2]
#guests.insert(2, 'Maria')
#print(f"you {guests[0]} are invite to a dinner with me")
#print(f"you {guests[1]} are invite to a dinner with me")
#print(f"you {guests[2]} are invite to a dinner with me")
#print(f"you {guests[3]} are invite to a dinner with me")

#3-6
#print(f"{guests[0]},{guests[1]},{guests[2]},{guests[3]}, we found a bigger dinner table, we will invite more people")

guests.insert(0, 'Daniela')
guests.insert(3, 'Samuel')
guests.append('Laura')

#print(f"you {guests[0]} are invite to a dinner with me")
#print(f"you {guests[1]} are invite to a dinner with me")
#print(f"you {guests[2]} are invite to a dinner with me")
#print(f"you {guests[3]} are invite to a dinner with me")
#print(f"you {guests[4]} are invite to a dinner with me")
#print(f"you {guests[5]} are invite to a dinner with me")

#3-7
print(f"{guests[0]},{guests[1]},{guests[2]},{guests[3]},{guests[4]},{guests[5]} \ni can only invite two people")

personNotInvite = guests.pop(0)
print(f"sorry {personNotInvite} i can't invite you to dinner")
personNotInvite = guests.pop(1)
print(f"sorry {personNotInvite} i can't invite you to dinner")
personNotInvite = guests.pop(2)
print(f"sorry {personNotInvite} i can't invite you to dinner")
personNotInvite = guests.pop(3)
print(f"sorry {personNotInvite} i can't invite you to dinner")
personNotInvite = guests.pop()
print(f"sorry {personNotInvite} i can't invite you to dinner")

print(f"{guests[0]} you are invite!!")
print(f"{guests[1]} you are invite!!")

itemDelete = 'Samuel'
guests.remove(itemDelete)
itemDelete = 'Cristina'
guests.remove(itemDelete)

print(guests)