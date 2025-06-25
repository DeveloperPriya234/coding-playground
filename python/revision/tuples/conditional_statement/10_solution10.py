def recommend_pet_food(species, age):
    species = species.lower()
    
    if species == "dog":
        if age < 2:
            return "Puppy Food"
        else:
            return "Senior Dog Food"
    elif species == "cat":
        if age > 5:
            return "Senior Cat Food"
        else:
            return "Regular Cat Food"
    else:
        return "Unknown species - no recommendation available"


print(recommend_pet_food("dog", 1))   # Puppy Food
print(recommend_pet_food("cat", 6))   # Senior Cat Food
print(recommend_pet_food("dog", 3))   # Senior Dog Food
print(recommend_pet_food("cat", 3))   # Regular Cat Food
print(recommend_pet_food("rabbit", 2))  # Unknown species
