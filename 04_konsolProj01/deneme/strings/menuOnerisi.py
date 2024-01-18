import random

corba = ["Tarhana","Yayla","Ezogelin","Mercimek"]
anaYemek = ["Karnı yarık","Kapama","Kuru fasulye","Mantı"]
tatli = ["Külbastı","Hoşaf","Baklava","Sütlaç"]

print("Menü öneri programı")
print(f"Bugün size {random.choice(corba)} çorbası,")
print(f"Bugün size {random.choice(anaYemek)} ana yemeği,")
print(f"Bugün size {random.choice(tatli)} tatlısı öneriyorum.")
