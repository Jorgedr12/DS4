planetas = list()
print(planetas)

planetas = []
print(planetas)

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno"]
print(planetas)

planetas.append("Urano")
planetas.append("Neptuno")
print(planetas)

p = planetas.pop()
print(planetas)
print(p)

pa = planetas.pop(0)
print(planetas)
print(pa)

planetas.insert(0,pa)

lunas = ["Luna", "Ceres", "Deimos", "Phobos"]
print(lunas[1])
print(lunas[3])

lunas.append("Europa")
lunas.append("Titan")
lunas.append("Ganymede")
lunas.append("Calisto")
lunas.append("Io")

print(lunas)

i=3

print(lunas[0:i])
print(lunas[i:])
print(lunas[2:5])
print(lunas[-1])
print("antepenultimo, penultimo y ultimo", lunas[-3:])
print("Antepenultimo,penultimo", lunas[-3:-1])
print(lunas[-2:])
print(lunas[::2])
print(lunas[::3])
print(lunas[::-1])

moons = lunas
print(f"Lunas {lunas}")
print(f"Moons {moons}")

moons.append("Triton")

print(f"Lunas {lunas}")
print(f"Moons {moons}")

print(f"Lunas id {id(lunas)} {lunas}")
print(f"Moons id {id(moons)} {moons}")
moons = lunas.copy()
moons.append("Charon")

print(f"Lunas id {id(lunas)} {lunas}")
print(f"Moons id {id(moons)} {moons}")

planetas_sw = ["Hoth", "Tatooine", "Naboo","Mustafar","Endor","Kamino"]
planetas.extend(planetas_sw)
print(planetas)
planetas.sort()
print(planetas)

moons_sw = ["Yavin 4", "Dagobah", "Coruscant", "Kashyyyk", "Geonosis", "Utapau"]
listas_lunas = [lunas, moons_sw]
print(listas_lunas)
print(listas_lunas[1][0])

print("--------------------")
for i,planeta in enumerate(planetas):
    print(i,planeta)
    
print(planetas.index("Marte"))
planetas=planetas.reverse()
print(planetas)

print("---------------------")

A= []
for i in range(0,10):
    A.append(i)
print(A)

B=[]
for i in range(0,10):
    if i%2==0:
        B.append(i)
print(B)

print("---------------------")
A = [i for i in range(0,10)]
B = [i for i in range(0,10) if i%2==0]
print(f"A:{A} ")
print(f"B:{B} ")
    
square = [i**2 for i in range(0,10)]
print(f"Square: {square}")
pi= 3.141592653589793
print(f"Pi: {pi:.2f}")