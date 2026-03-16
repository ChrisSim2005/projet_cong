def convertir_temp(cel):
    fah = cel * (9/5) + 32

    if fah >= 86 :
        msg = "Chaud"
    elif fah >= 68 :
        msg = "Tiéde"
    else:
        msg = "Froid"

    return fah , msg 

print ("conversion de celsius en fahrenheit")
cel = float(input("entrez la température en celsius : "))
f , msg = convertir_temp(cel)
print (f"conversion de {cel} = {f}F - {msg}")

