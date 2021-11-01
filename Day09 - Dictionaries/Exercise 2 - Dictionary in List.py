travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# Write program that that user can add to travel log


def add_to_travel_log(country: str, visits: int, cities: list):
    """Program that add to travel_log"""
    new_dict = {"country": country, "visits": visits, "cities": cities}
    travel_log.append(new_dict)


print(travel_log)
add_to_travel_log("Australia", 27, ["Sydney", "Melbourne", "Gold Coast"])
print(travel_log)
