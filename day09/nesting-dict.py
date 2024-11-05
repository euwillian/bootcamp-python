# nesting - aninhamento
# {key: valeu}
# {key: [list], key2: {dict}}

# exercise:

capitals = {
    "Brazil": "Brasilia",
    "France": "Paris",
}

# Nested list in dict

travel_log = {
    "Brazil": ["Sao Paulo", "Rio de Janeiro", "Espirito Santo"],
    "Argentina": ["Ushuaia", "Buenos Aires"]
}

# print Rio de Janeiro
print(travel_log["Brazil"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log = {
    "Brazil": {
        "num_times_visited": 3,
        "cities_visited": ["Salto", "Itu", "Sao Paulo"]
    },
    "Argentina": {
        "num_times_visited": 2,
        "cities_visited": ["Buenos Aires", "Ushuaia"]
    }
}

print(travel_log["Argentina"]["cities_visited"][1])  # Ushuaia
