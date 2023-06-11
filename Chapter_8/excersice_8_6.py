def city_country(city_name, country):
    formatted_city = f"{city_name}, {country}"
    return formatted_city.title()

print(city_country("santiago","chile"))