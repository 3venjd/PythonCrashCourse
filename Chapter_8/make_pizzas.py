
#version 1 importing all file(module)
#import pizza

#pizza.make_pizza(16,'peperoni')
#pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

#version 2 importing by function
#from pizza import make_pizza

#make_pizza(16,'peperoni')
#make_pizza(12,'mushrooms','green peppers','extra cheese')

#version 3 importing by function and give it an alias
#from pizza import make_pizza as pz

#pz(16,'peperoni')
#pz(12,'mushrooms','green peppers','extra cheese')

#version 4 importing all file(module) with alias
#import pizza as p
#p.make_pizza(16, 'pepperoni')
#p.make_pizza(12,'mushrooms','green peppers','extra cheese')

#version 5 importing all functions in a module
from pizza import *
make_pizza(16,'peperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')