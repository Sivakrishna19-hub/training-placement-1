import random
import string

def generate_username():
    adjectives = ["Cool", "Happy", "Fast", "Smart", "Strong"]
    nouns = ["Lion", "Tiger", "Eagle", "Shark", "Wolf"]
    return random.choice(adjectives) + random.choice(nouns) + str(random.randint(10, 99))

print("Generated Username:", generate_username())
