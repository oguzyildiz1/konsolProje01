araba = {
    "audi" : "A4",
    "mercedes" : "C300",
    "bmw" : "3.20D"
}

for count, i in enumerate(araba, 100):
    print(count, i)


asa1 = "string"
asa2 = ["asdf"]

print(type(asa1))

if type(asa2) == str:
    print("string")
elif type(asa2) == list:
    print("list")
