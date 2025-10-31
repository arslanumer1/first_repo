class Animal:
    def __init__(self,legs, tail=True, name="Animal"):
        self.legs = legs
        self.tail = True
        self.name = Animal

    def run(self):
        print(f"My {Animal} can run")
    def eat(self):
        print(f"My {Animal} can eat")

cat = Animal(4, True, "cat")
cat.run()
cat.eat()


class Degree:
    def __init__(self, name, advisor, num_of_publications, num_of_years):
        self.name = name
        self.advisor = advisor
        self.num_of_publications = num_of_publications
        self.num_of_years = num_of_years

    def __str__(self):
        return (
            f"{self.name} is in {self.num_of_years}th year of pHD "
            f"with {self.num_of_publications} publications"
            f"and under the supervision of {self.advisor}")


Arslan = Degree("Arslan", "Balkus", 5, 4)
print(Arslan)
