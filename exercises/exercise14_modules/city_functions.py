"""This module holds the city function for exercise 14 11.1 and 11.2"""


def get_city_country(city, country, population=''):
    """Gets a city and country, and joins them in one string"""
    if population:
        location = f'{city}, {country} - population: {population}'
    else:
        location = f'{city}, {country}'
    return location
