#%%
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

    def add_skill(self, skill):
        self.skills.append(skill)

#%% Inherited class
class Student(Person):
    pass

#%%
p = Person('Ashish', 'Panigrahi', 21, 'India', 'Chennai')
print(p.person_info())
p.add_skill('LaTeX')
p.add_skill('Linux')
print(p.skills)

#%%
s1 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('Java')
s1.add_skill('ReactJS')
print(s1.skills)

#%%
class Student(Person):
    def __init__(self, firstname='Ashish', lastname='Panigrahi', age=21, country='India', city='Chennai', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)

    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

#%%
s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki', 'male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
print(s2.person_info())

#%% Class exercise 1
class Statistics:
    def __init__(self, ages):
        self.ages = ages

    def count(self):
        return len(self.ages)

    def sum(self):
        return sum(self.ages)

    def min(self):
        return sorted(self.ages)[0]

    def max(self):
        return sorted(self.ages, reversed=True)[0]

    def range(self):
        return max(self.ages) - min(self.ages)

    def mean(self):
        return sum(self.ages)/len(self.ages)

    def mode(self):
        ct = 0
        for i in range(len(self.ages)):
            for j in range()
