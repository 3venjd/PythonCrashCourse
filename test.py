from random import randint

list1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
list2 = [ind for ind, x in enumerate(list1) if x == 'two']


results = [randint(2,12) for roll_num in range(1_000)]

#get the index
#finalList = [index for index,x in enumerate([2,3,4,5,6])]


print(results)