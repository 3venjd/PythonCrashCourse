#motorcycles = ['Honda','yamaha', 'susuki']
#print(motorcycles)

#motorcycles[0] = 'ducati'

#motorcycles.append('ducati')
#print(motorcycles)

#adding items in last position
#motorcycles = []
#motorcycles.append('Honda')
#motorcycles.append('yamaha')
#motorcycles.append('susuki')
#print(motorcycles)

#insert items in any place 
motorcycles2 = ['honda','yamaha', 'susuki']
motorcycles2.insert(0, 'ducati')
#print(motorcycles2)

# delete from any position
#del motorcycles2[3]
#print(motorcycles2)

# pop(extract item) last item
#popped_motorcycle = motorcycles2.pop()
#print(motorcycles2)
#print(popped_motorcycle)

#pop from any position
#first_item = motorcycles2.pop(1)
#print(motorcycles2)

#delete by value
item_delete = 'honda'
motorcycles2.remove(item_delete)
print(motorcycles2)