plant_store = {
    "name" : "Leaf Love",
    "cash" : 100,
    "plants" : [
        {
            "name" : "Bromeliad",
            "price" : 6,
            "toxic" : False
        },
        {
            "name" : "Polka Dot Plant",
            "price" : 3,
            "toxic" : False
        },
        {
            "name": "Monstera",
            "price" : 10,
            "toxic" : True
        }
    ]
}
# This is a function that will display either plants that are toxic to cats, or not toxic to cats
def get_plants_by_toxicity(plant_store, toxicity):
    plant_list = []
    for plant in plant_store["plants"]:
        if plant["toxic"] == toxicity:
            plant_list.append(plant)
    return plant_list 

# Calling the function and printing it
print(get_plants_by_toxicity(plant_store, True))
print(get_plants_by_toxicity(plant_store, False))

