
"""obtener titulo y precio"""
def getTitle(capitulo):
    switcher = {
        "1": "The Mandalorian",
        "2": "The Child",
        "3": "The Sin",
        "4": "Sanctuary",
        "5": "The Gunslinger",
        "6": "The Prisoner",
        "7": "The Reckoning",
        "8": "Redemption"
    }
    return switcher.get(capitulo)

"""obtener precio"""
def getPrice(capitulo):
    switcher = {
        "1": 200,
        "2": 250,
        "3": 270,
        "4": 150,
        "5": 300,
        "6": 200,
        "7": 280,
        "8": 250
    }
    return switcher.get(capitulo)
