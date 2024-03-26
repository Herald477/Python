class animal:
    def __init__(self, name : str, race : str, legs : str):
        self.name = name
        self.race = race
        self.legs = legs
    
    def __str__(self):
        return f"{self.name} {self.race} {self.legs}"