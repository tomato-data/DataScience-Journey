class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print("{0}\t{1}\t{2}\t{3}\t{4}".format(self.location, self.house_type,\
            self.deal_type, self.price, self.completion_year))

Gangnam = House("Gangnam", "Apartment", "For Sale", "10m", 2010)
Mapo = House("Mapo", "Office-tel", "Lump-sum Lease", "5m", 2007)
Songpa = House("Songpa", "Villa", "Lease", "500/50", 2000)

lst = [Gangnam, Mapo, Songpa]

print("{0} possible options".format(len(lst)))

for h in lst:
    h.show_detail()