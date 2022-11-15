myString = 'hello guys!'
myString2 = "hello my 'friends'"  # Если внешние ковычки одинарные, то внутренние должны быть двойные
myString3 = "I press \"like\" button"  # Экранирование
myString4 = """Hello
Mr
Friends
Hello
You
Is
"Big"
"""

print(myString4)

myString = "Bear " + "is not" + "a beer"

print(myString)

myStringMulti = "Go " * 15
print(myStringMulti)

myString = "one sentence"
print(len(myString))

myString5 = "Python"
for item in dir(myString5):
    print(item)

myString6 = "I like js"
myString6 = myString6.split(" ")
print(myString6)
print(type(myString6))

myString6 = " ".join(myString6)
print(myString6)

name = "Вадем"
myString7 = f"Привет {name}!"
print(myString7)

myString8 = "DVA TOP BRUISER NO CAP"
myString8 = myString8[0:7]  # Срез данных
print(myString8)
myString8 = myString8[:7]  # Срез данных
print(myString8)
print(myString8[::-1])  # Перевернутая строка

