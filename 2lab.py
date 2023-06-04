lnm1=[5,10,15,20]
lnm2=[6,12,16,19]
lnm1listed=list(lnm1)
lnm2set=set(lnm2)
print("Список1",lnm1)
print("Список2",lnm2)
print("Сортування списку 1",lnm1listed)
print("Пересортування списку", lnm2set)
dict={
    "dictator": 24,
    "boom4": 26,
    "zroz": print,
}
print()
for dictator,boom4 in dict.items():
    print(dictator,boom4)
lnm1.append(dict["dictator"])
print("Добавляємо диктатора",lnm1)
lnm2.remove(6)
print("Прибираємо 6",lnm2)
lnm1redacted=[4,10,*lnm1]
print("Добавляємо 4, 10", lnm1redacted)
import numpy as bros
splits=bros.array_split(lnm1redacted,2)
for array in splits:
    print(list(array))
print("Розєднуємо", lnm1redacted)
