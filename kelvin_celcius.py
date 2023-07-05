# a class to convert kelvin to celcius and vice versa

class CleciusConverter:

    def __init__(self, temp):
        self.temp = temp

    def celcius_to_kelvin(self):
        return f"Temperature {self.temp + 273.15} K"

    def celcius_to_farhenheit(self):
        return f"Temperature {self.temp * 9/5 - 459.67} F"
    

temp = CleciusConverter(100)
print(temp.celcius_to_kelvin())
print(temp.celcius_to_farhenheit())
