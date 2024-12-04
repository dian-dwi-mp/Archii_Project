import random

def tell_joke():
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they can't C#.",
        "What is a computer’s favorite snack? Microchips."
    ]
    return random.choice(jokes)

