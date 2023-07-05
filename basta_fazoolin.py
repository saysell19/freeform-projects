# README; using "cc_basta" conda environment.
# Please switvh to this environment before running 
# the program and switch back to "base" once you are done

class Menu:

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        return '{name} menu available from {start} to {end}'.format(name=self.name, start=self.start_time, end=self.end_time)

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]

        return bill

# FRANCHISE class
class Franchise:

    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self) -> str:
        return 'The address of this store is {address}. Enjoy!'.format(address=self.address)

    def available_menus(self, time):
        available_menu = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menu.append(menu)
        return available_menu

# BUSINESS class
class Business:

    def __init__(self, name, franchises) -> None:
        self.name = name
        self.franchises = franchises
    

# MENUS
brunch_menu = {
  'pancakes': 7.50, 
  'waffles': 9.00, 
  'burger': 11.00, 
  'home fries': 4.50, 
  'coffee': 1.50, 
  'espresso': 3.00, 
  'tea': 1.00, 
  'mimosa': 10.50, 
  'orange juice': 3.50
}

e_b_menu = {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 
  'espresso': 3.00,
}

dinner_menu = {
  'crostini with eggplant caponata': 13.00, 
  'caesar salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 
  'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 2.00, 
  'espresso': 3.00,
}

kids_menu = {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00

}

# Time is in 24 hour clock
# Create MENU objects
brunch = Menu('Brunch', brunch_menu, 1100, 1600)
early_bird = Menu('Early Bird', e_b_menu, 1500, 1800)
dinner = Menu('Dinner', dinner_menu, 1700, 2300)
kids = Menu('Kids', kids_menu, 1100, 2100)

# ALL MENU OBJECTS VVV
all_menus = [brunch, early_bird, dinner, kids]

# Create FRANCHISE objects
flagship_store = Franchise("1232 West End Road", all_menus)
new_installment = Franchise('12 East Mulberry Street', all_menus)

# Create new BUSINESS objects
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Create new business - for AREPAS
ap_menu = {
  'arepa pabellon': 7.00, 
  'pernil arepa': 8.50, 
  'guayanes arepa': 8.00, 
  'jamon arepa': 7.50
}
arepas_menu = Menu('Arepas menu', ap_menu, 1000, 2000)
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])
arepas = Business("Take a' Arepa", [arepas_place])



# TEST AREA
print(flagship_store)
print(new_installment)
print(flagship_store.available_menus(1200))
print(new_installment.available_menus(1700))
print(brunch)
print(type(brunch))
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['mushroom ravioli (vegan)', 'salumeria plate']))