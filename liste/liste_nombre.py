nombres = []
for i in range(5):
    nombre = int(input(f"nombre {i+1} : "))
    nombres.append(nombre)
som = sum(nombres)
moy = som/len(nombres)
maxi = max(nombres)

print(f"somme : {som} , moyenne : {moy} , maximum : {maxi}")