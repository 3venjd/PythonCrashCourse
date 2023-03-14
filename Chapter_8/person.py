#def build_person(first_name, last_name):
#    """return a dictionary of information about a person"""
#    person = {'first': first_name, 'last': last_name}
#    return person

def build_person(first_name, last_name, age = None):
    """return a dictionary of information about a person"""
    person = {'first': first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=28)
print(musician)