from random import choice

class lotery:
    def __init__(self,my_ticket):
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                       'A', 'B', 'C', 'D', 'E']
        self.ticket = my_ticket
    
    def random(self):
        attemps = 0
        val = ''
        while(val != self.ticket):    
            val = ''
            for i in(range(4)):
                valini = str(choice(self.values))
                val = val + valini
            
            attemps = attemps + 1
        
        print(f'the quantity of attemps was {attemps}')
        
        
lotery_result = lotery('AAAA')
lotery_result.random()
