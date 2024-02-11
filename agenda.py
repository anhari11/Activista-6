import time

def pasaraarray(agenda_file):
    # Obtenim la informació de l'agenda des del fitxer
    with open(agenda_file, 'r') as file:
        lines = file.readlines()
        array = []
        # Processem cada línia del fitxer
        for line in lines:
            j = 0
            frase = []
            # Dividim la línia en fragments separats per comes
            while j < len(line):
                dada = ""
                while j < len(line) and line[j] != ",":
                    dada += line[j]
                    j += 1

                frase.append(dada)
                j += 1

            array.append(frase)
    return array

def mostrarllista(array):
    z = 0
    continuar = False
    # Mostrem la llista d'entrades en grups de 10
    while z < len(array) - 1 and not continuar:
        j = z
        while j < z + 10 and j < len(array):
            # Mostrem l'índex i l'entrada corresponent
            if j == 0:
                print(" ", "".join(array[j]))
            else:
                print(j, "".join(array[j]))
            j += 1
        # Demanem a l'usuari que escrigui 'a' per aturar-se o qualsevol tecla per continuar
        z += 10
        inp = input("Escriu a per parar, qualsevol tecla per continuar")
        if inp == "a":
            continuar = True

def validar_nom():
    try:
        i = 0
        correcte = True
        found = False
        # Validem el nom, assegurant-nos que només conté lletres i espais
        while not found:
            nom = input("Quin és el teu nom ")
            count = 0
            trancar = True
            while i < len(nom) - 1 and trancar and count < len(nom):
                if nom[i].isalpha() or nom[i].isspace():
                    count += 1
                    if count == len(nom):
                        found = True
                else:
                    trancar = False

    except ValueError as e:
        print(f"Error: {e}")

    return nom.title() + " "  # Convertim a majúscules la primera lletra de cada paraula

def validar_cognom():
    try:
        i = 0
        correcte = True
        found = False
        # Validem el cognom, assegurant-nos que només conté lletres i espais
        while not found:
            cognom = input("Quin és el teu cognom ")
            count = 0
            trancar = True
            while i < len(cognom) - 1 and trancar and count < len(cognom):
                if cognom[i].isalpha() or cognom[i].isspace():
                    count += 1
                    if count == len(cognom):
                        found = True
                else:
                    trancar = False
                    print("Format Incorrecte")

    except ValueError as e:
        print(f"Error: {e}")

    return cognom.title() + " "  # Convertim a majúscules la primera lletra de cada paraula

def validar_telefon():
    found = False

    while not found:
        try:
            numero = input("Quin número? ")

            if numero.isdigit() and (numero[0] == '6' or numero[0] == '7') and len(numero) == 9:
                found = True
            else:
                print("El número ha de començar per 6 o 7.")
        except IndexError:
            print("El número només ha de contenir dígits")

    return numero + " "

def validar_telegram():
    try:
        found = False

        while not found:
            username = input("Quin és el teu usuari de Telegram? ")

            if username[0] == "@" and username[1:].isalnum() and len(username) > 1:
                found = True
            else:
                print("Nom d'usuari de Telegram no vàlid. Torna a introduir.")

    except Exception as e:
        print(f"Error: {e}")

    return username + " "

def validardades():
    dades = []
    # Validem cada tipus d'informació i l'afegim a la llista de dades
    dades.append(validar_nom())
    dades.append(validar_cognom())
    dades.append(validar_telefon())
    dades.append(validar_telegram())

    return dades

def modificar_entrada(array):
    mostrarllista(array)

    try:
        fila = int(input("Quina fila vols modificar? "))

        if 0 <= fila < len(array):
            print("Dades actuals:")
            print(array[fila])
            
            #Cridem la funcio validardades per asegurarnos que les dades son correctes.

            data = validardades()

            array[fila] = data

            print("Entrada modificada correctament.")
        else:
            print("Fila incorrecta. No s'ha modificat cap entrada.")
    except ValueError:
        print("Fila incorrecta. No s'ha modificat cap entrada.")

def eliminar_entrada(array):
    mostrarllista(array)

    try:
        fila = int(input("Quina fila vols eliminar? "))

        if 0 <= fila < len(array):
            print("Dades de l'entrada a eliminar:")
            print(array[fila])

            confirmacio = input("Segur que vols eliminar aquesta entrada? (s/n): ")

            if confirmacio == 's':
                del array[fila]
                print("Entrada eliminada correctament.")
            else:
                print("No s'ha eliminat cap entrada.")
        else:
            print("Fila incorrecta. No s'ha eliminat cap entrada.")
    except ValueError:
        print("Fila incorrecta. No s'ha eliminat cap entrada.")

def cercar_dades(array):
    camp = int(input("Quin camp vols cercar? 1: nom, 2: cognom, 3: telefon, 4: Telegram "))
    coincidencia = input("Introdueix el valor pel camp seleccionat: ")

    resultat = []

    i = 0
    while i < len(array):
        if coincidencia == array[i][camp - 1]:
            resultat.append(array[i])
        i += 1

    print("Resultats de la cerca:", resultat)

    guardar_fitxer = input("Vols guardar els resultats en un fitxer? (s/n): ")

    if guardar_fitxer == 's':
        with open(f"carpeta/cerca-{time.time()}.txt", 'w') as f:
            for resultat in resultat:
                print(resultat)
                f.write(','.join(resultat) + '\n')
            print("Resultats guardats en l'arxiu.")

def generaraxius(array):
    i = 1
    arxiusjafets = []

    while i < len(array):
        if array[i][1] not in arxiusjafets:
            arxiusjafets.append(array[i][1])
            
            j = i
            cognoms = []
            while j < len(array):
                if array[i][1] == array[j][1]:
                    cognoms.append(array[j])
                j += 1
            i = j

            with open("carpeta/" + array[i-1][1] + ".txt", "w") as file:
                for z in cognoms:
                    file.write(','.join(z) + '\n')

    print("Arxius Cognoms generats correctament.")

if __name__ == "__main__":
    # Inicialitzem l'agenda a partir del fitxer
    agenda_file = "agenda.txt"
    agenda = pasaraarray(agenda_file)
    
    continuar = True

    while continuar:
        print("\n1. Afegir entrada")
        print("2. Llistar entrades")
        print("3. Modificar entrada")
        print("4. Eliminar entrada")
        print("5. Cercar dades")
        print("6. Generar arxius Cognoms ")
        print("7. Sortir")

        opcio = input("Escull una opció (1-7): ")

        if opcio == '1':
            try:
                agenda.append(validardades())
                print ("Entrada afegida correctament.")
                
            except Exception as e:
                print ("Hi ha hagut un problema", e)
            
        elif opcio == '2':
            mostrarllista(agenda)
        elif opcio == '3':
            modificar_entrada(agenda)
        elif opcio == '4':
            eliminar_entrada(agenda)
        elif opcio == '5':
            cercar_dades(agenda)
        elif opcio == "6":
            generaraxius(agenda)
        elif opcio == '7':
            print("Has sortit, fins aviat")
            continuar = False
        else:
            print("Opció no vàlida.")

