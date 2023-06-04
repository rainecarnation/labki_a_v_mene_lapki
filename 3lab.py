import datetime

class Person:
    name: str = None
    birthday: datetime.date = None

    def __init__(self, name: str, birthday: str):
        self.name = name
        self.birthday = datetime.datetime.fromisoformat(birthday).date()

    def __str__(self):
        return f"{self.name} [{self.birthday}]"

    def __lt__(self, other):
        return self.birthday < other.birthday

    def __eq__(self, other):
        return self.birthday == other.birthday


Person1=Person(name="Hello world", birthday="2005-04-23")
Person2=Person(name="Mrec world2", birthday="2003-06-21")
Person3=Person(name="Nohats world3", birthday="2002-04-08")
Person4=Person(name="Ukr world4", birthday="2007-03-15")

persons1=[Person1, Person2, Person3, Person4]

persons2 = [
    Person("Biden", "2005-01-02"),
    Person("Author", "1997-05-10"),
    Person("John Wick", "2006-12-24")
    ]
for I in persons1:
    print("1-ше",I)
for I in persons2:
    print("2-ге",I)
persons1.sort()
persons2.sort()
for I in persons1:
    print("1-е",I)
for I in persons2:
    print("2-ге",I)
if persons1 == persons2:
    print("\n\nКолекції однакові.")
else:
    print("\n\nКолекції не однакові")
if persons1 < persons2:
    print("\n\nКолекція менше.")
else:
    print("\n\nКолекція більша")
