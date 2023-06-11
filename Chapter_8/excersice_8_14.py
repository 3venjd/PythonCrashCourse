def make_car(manufacturer,model_name,**caracteristics):
    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model_name
    car["details"] = caracteristics
    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)