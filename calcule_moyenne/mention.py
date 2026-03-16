def calcule_moyenne(notes):
    moyenne = sum(notes) / len(notes)
    return moyenne

def obtenir_mention(moyenne):
    if moyenne >= 16:
        msg = "Trés bien "
    elif moyenne >= 14:
        msg = "bien"
    elif moyenne >= 12:
        msg = "assez bien"
    elif moyenne >= 10:
        msg = "passable"
    else:
        msg = "echec"
    return msg


notes = []
print ("les notes ")
for i in range(4):
    while True:
        try:
            note = float(input(f"note {i + 1} : "))
            if  0 <= note <=20:
                notes.append(note)
                break
            else:
                print("note entre 0 et 20")
        except ValueError:
            print("on veux un nombre")
        
    
moyenne = calcule_moyenne(notes)
mention = obtenir_mention(moyenne)

print(f"votre moyenne : {moyenne} , mention : {mention}")

