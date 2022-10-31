print("Bienvenido a la isla, tu misión será encontrar el tesoro")
print("Para iniciar la misión los ancestros de estas tierras te han ofrecido un mapa")
print("este mapa tiene 2 caminos que te conduciran a la victoria o a la muerte. ¡Qué inicie está aventura! ")

camino=input("por favor selecciona un camino, escribe la palabra derecha o izquierda para seleccionar el camino que desees seguir?")

if camino == "derecha":
    print("siento algunos ruidos, decide rapidamente")
    seleccion= input("te agachas o saltas?.Escribe la palabra agacharse o saltar")
    if seleccion == "agacharse":
        print("en el suelo hay dos flores que te daran un poder, elige sabiamente")
        flor=input("roja o azul. Escribe la palabra roja o azul para seleccionar la rosa")
        if flor == "azul":
            print("recibiste un poder secreto")
            aceptar = input("lo aceptos o no. Escribe la palabra si o no")
            if aceptar == "no":
                print("encuentras una cueva")
                entrar= input("deseas entrar o no. Escribe la palabra si o no")
                if entrar == "si":
                    print("ganaste, encontraste e tesoro")
                elif entrar == "no":
                    print("te encuentras con los piratas enemigos, perdiste")               
            elif aceptar == "si":
                print("el poder era la autodestrucción,perdiste")
                
        elif flor == "roja":
            print("la flor estaba envenenada,perdiste")
        
    elif seleccion == "saltar":
        print("no esquivaste la flecha, perdiste")
        
elif camino == "izquierda":
    print("caiste en un agujero, perdiste") 
    
else:
    print("no ingresaste un dato valido")
    