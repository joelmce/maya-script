class Rarity:
    def __init__(self, path, json):
        with open(path + '/' + json) as json_file:
            self.rarities = json.load(json_file)

    def pick_attributes(self, category):
        choices = list(self.rarities[category].keys())
        probabilities = list(map(lambda x: x / 100.0, list(self.rarities[category].values())))
        draw = choice(choices, 1, p = probabilities)[0]
        return draw
