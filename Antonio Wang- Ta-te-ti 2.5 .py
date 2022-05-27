def mostrar(listvalores):
    print("  " + str(listvalores[0]) + " | " + str(listvalores[1]) + " | " + str(listvalores[2]))
    print("----|---|----")
    print("  " + str(listvalores[3]) + " | " + str(listvalores[4]) + " | " + str(listvalores[5]))
    print("----|---|----")
    print("  " + str(listvalores[6]) + " | " + str(listvalores[7]) + " | " + str(listvalores[8]))

listvalores = [1,2,3,4,5,6,7,8,9]
completar = 0
mostrar(listvalores)
rondas = 0
i = 0
j = 0
contadorX = 0
contadorO = 0
ejecutar = 0
esquinas = listvalores.count(1) + listvalores.count(3) + listvalores.count(7) + listvalores.count(9)

print("Este un programa del juego ta-te-ti modificado, el jugador 1 usa X y AI usa O como sus marcas")
print("Cada espacio solo se puede usar 1 vez, y los numeros invalidos no van a poder modificar el juego")

while completar != 9:
    rondas += 1
    print("ronda: " + str(rondas))

    if contadorO == 3:
        break

    if rondas % 2 != 0:
        print("Ronda del jugador")
        valor = int(input("Ingresa el numero elegido: "))

        for i in range(len(listvalores)):

            if listvalores[i] == valor:
                listvalores[i] = "X"
                completar += 1
            else:
                ""
        mostrar(listvalores)


    else:
        print("Ronda de AI")
        esquinas = listvalores.count(1) + listvalores.count(3) + listvalores.count(7) + listvalores.count(9)
        ejecutar = 0
        movementAI = 0

        if movementAI == 0:
            horizontal = (1, 4, 7)
            for j in horizontal:
                contadorO = 0

                for i in listvalores[j - 1:j + 2]:
                    try:
                        contadorO = listvalores[j - 1:j + 2].count("O")

                        if 0 <= i <= 9 and contadorO == 2:
                            listvalores[i - 1] = "O"
                            completar += 1
                            ejecutar += 1
                            movementAI += 1

                    except TypeError:
                        pass
        if movementAI == 0:
            vertical = (1, 2, 3)
            for j in vertical:
                contadorO = 0

                for i in listvalores[j - 1:j + 8:3]:
                    try:
                        contadorO = listvalores[j - 1:j + 8:3].count("O")
                        if 0 <= i <= 9 and contadorO == 2:
                            listvalores[i - 1] = "O"
                            completar += 1
                            ejecutar += 1
                            movementAI += 1

                    except TypeError:
                        pass
        if movementAI == 0:
            contadorO = 0

            for i in listvalores[0:9:4]:
                try:
                    contadorO = listvalores[0:9:4].count("O")
                    if 0 <= i <= 9 and contadorO == 2:
                        listvalores[i - 1] = "O"
                        completar += 1
                        ejecutar += 1
                        movementAI += 1

                except TypeError:
                    pass
        if movementAI == 0:
            contadorO = 0
            for i in listvalores[2:7:2]:
                try:
                    contadorO = listvalores[2:7:2].count("O")
                    if 0 <= i <= 9 and contadorO == 2:
                        listvalores[i - 1] = "O"
                        completar += 1
                        ejecutar += 1
                        movementAI += 1

                except TypeError:
                    pass

            if movementAI == 0:
                horizontal = (1, 4, 7)
                for j in horizontal:
                    contadorX = 0

                    for i in listvalores[j - 1:j + 2]:
                        try:
                            contadorX = listvalores[j - 1:j + 2].count("X")

                            if 9 >= i >= 0 and contadorX == 2:
                                listvalores[i - 1] = "O"
                                completar += 1
                                ejecutar += 1
                                movementAI += 1
                        except TypeError:
                            pass

            if movementAI == 0:
                vertical = (1, 2, 3)
                for j in vertical:
                    contadorX = 0

                    for i in listvalores[j - 1:j + 8:3]:
                        try:
                            contadorX = listvalores[j - 1:j + 8:3].count("X")

                            if 9 >= i >= 0 and contadorX == 2:
                                listvalores[i - 1] = "O"
                                completar += 1
                                ejecutar += 1
                                movementAI += 1

                        except TypeError:
                            pass

            if movementAI == 0:
                    contadorX = 0

                    for i in listvalores[0:9:4]:
                        try:
                            contadorX = listvalores[0:9:4].count("X")
                            if 9 >= i >= 0 and contadorX == 2:
                                listvalores[i - 1] = "O"
                                completar += 1
                                ejecutar += 1
                                movementAI += 1

                        except TypeError:
                            pass

            if movementAI == 0:
                    contadorX = 0
                    for i in listvalores[2:7:2]:
                        try:
                            contadorX = listvalores[2:7:2].count("X")
                            if 9 >= i >= 0 and contadorX == 2:
                                listvalores[i - 1] = "O"
                                completar += 1
                                ejecutar += 1
                                movementAI += 1

                        except TypeError:
                            pass

        #---------------------------------------------------------------------------------------------

        if ejecutar == 0:
            if listvalores[4] == 5:
                try:
                    ubicacion = 0
                    ubicacion = listvalores.index(5)
                    listvalores[ubicacion] = "O"
                    completar += 1
                except ValueError:
                    pass

            elif esquinas != 0:

                for i in range(1, 11, 2):
                    try:
                        ubicacion = 0
                        ubicacion = listvalores.index(i)
                        listvalores[ubicacion] = "O"
                        completar += 1

                        if listvalores[ubicacion] == "O":
                            break
                    except ValueError:
                        pass

            else:

                for i in range(2, 10, 2):
                    try:
                        ubicacion = 0
                        ubicacion = listvalores.index(i)
                        listvalores[ubicacion] = "O"
                        completar += 1

                        if listvalores[ubicacion] == "O":
                            break
                    except ValueError:
                        pass
            mostrar(listvalores)
        else:
            mostrar(listvalores)

        # ---------------------------------------------------------------------------------------------
        horizontal = (1, 4, 7)
        vertical = (1, 2, 3)
        for j in horizontal:
            contadorO = 0
            contadorO = listvalores[j - 1:j + 2].count("O")
            if contadorO == 3:
                break
            else:
                for j in vertical:
                    contadorO = 0

                    contadorO = listvalores[j - 1:j + 8:3].count("O")
                    if contadorO == 3:
                        break
                    else:
                        contadorO = 0

                        contadorO = listvalores[0:9:4].count("O")
                        if contadorO == 3:
                            break
                        else:
                            contadorO = 0
                            contadorO = listvalores[2:7:2].count("O")
                            if contadorO == 3:
                                break

if contadorO == 3:
    print("Ganó el AI")
else:
    print("Empate")