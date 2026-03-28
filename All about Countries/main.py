class Bangladesh():
    def capital(self):
        print ("Dhaka is the capital of Bangladesh")
    def language(self):
        print ("Bengla is the mother language of Bangladesh")
    def type(self):
        print ("Bangladesh is a developing country")
class USA():
    def capital(self):
        print ("Washington DC is the capital of USA")
    def language(self):
        print ("English is the mother language of USA")
    def type(self):
        print ("USA is a developed country")
obj_bangladesh = Bangladesh()
obj_usa = USA()
for country in (obj_bangladesh, obj_usa):
    country.capital()
    country.language()
    country.type()