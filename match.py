dia = 7

match dia:
    case 1:
        print("Hoy es lunes")
    case 2:
        print("Hoy es martes")
    case 3:
        print("Hoy es miércoles")
    case 4:
        print("Hoy es jueves")
    case 5:
        print("Hoy es viernes")
    case 6:
        print("Hoy es sábado")
    case 7:
        print("Hoy es domingo")
    case _:
        print("Número de día inválido")


Juego = "Bloodborne"

match Juego:
    case "TLOU 1 & 2":
        print("Playstation")
    case "Halo":
        print("Xbox")
    case "Mario Bros":
        print("Nintendo")
    case "FIFA":
        print("Multiplataforma")
    case "Bloodborne":
        print("Playstation 4")