def get_country_city(country,city,population = ''):

    if population:
        formatted_country_city = f"{city}, {country} - population {population}"
    else:
        formatted_country_city = f"{city}, {country}"
    return formatted_country_city.title()