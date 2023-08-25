def get_city_name(cityName,countryName,population = ''):
    
    if(population):
        full_city = f"{countryName.title()}, {cityName.title()} - {population}"
    else:
        full_city = f"{countryName.title()}, {cityName.title()}"
        
    return full_city