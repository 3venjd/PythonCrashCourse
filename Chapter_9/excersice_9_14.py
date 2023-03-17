from random import choice

class lotery:
    def __init__(self):
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                       'A', 'B', 'C', 'D', 'E']

    def random(self):
        val = ''
        for i in(range(4)):
            valini = str(choice(self.values))
            val = val + valini

        return val
        

lotery_result = lotery()
v = lotery_result.random()
print(f'the win value is {v}')

