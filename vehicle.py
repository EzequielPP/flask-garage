class Vehicle:

    def __init__(self, make, model, year, km):
        self.make = make
        self.model = model
        self.year = year
        self.km = km

    def to_dict(self):
        return {
            "marca": self.make,
            "model": self.model,
            "year": self.year,
            "km": self.km,
        }
