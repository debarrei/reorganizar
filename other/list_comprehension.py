pers = ["John", "Jane", "Paquito", "Juanito"]

#for loop:

for n in pers:
    #n = n.lower()
    if n.lower().startswith("j"):
        print(n.upper())

#list comprehension:
pers_j = [ nombre.upper() for nombre in pers if nombre[0].lower() == "j"]
print(pers_j)