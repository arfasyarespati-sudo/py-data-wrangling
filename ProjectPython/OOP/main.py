class car:
    def __init__(self, brand: str, series: str, horsepower: int):
        self.brand = brand
        self.series = series
        self.horsepower = horsepower

class truck(car):
    def __init__(self, brand, series, horsepower, diesel):
        super().__init__(brand, series, horsepower)
        self.diesel = diesel

car1 = car('mercedes', 'Y', '1000')
truck1 = truck('hilux', 'X', '5000', True)

print(car1.series)
print(truck1.diesel)
