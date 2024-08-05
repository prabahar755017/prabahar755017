from datetime import datetime

class person:

    def __init__(self, name, country, dob) :
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d")

    def get_age(self):
        today = datetime.today()
        age = today.year - self.dob.years
        return age


Person = person("Prabaharan", "india", "1999-08-14")
print(f"{Person.name},{Person.country},{Person.get_age()}")
