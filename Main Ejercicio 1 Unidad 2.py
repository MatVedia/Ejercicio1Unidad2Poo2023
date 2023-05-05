from ClaseGestorEmail import GestorEmail

def test(gestor):
    print("Bienvenido a la funcion test.")
    nuevoCorreo = input("Ingrese su correo. Para salir, ingrese FIN.\n")
    copia = nuevoCorreo.upper()
    while copia != "FIN":
        if gestor.crearCuenta(nuevoCorreo):
            print('{} se registro correctamente.'.format(nuevoCorreo))

        nuevoCorreo = input('Ingrese su correo. Para terminar, ingrese FIN.\n')
        copia = nuevoCorreo.upper()


if __name__ == '__main__':
    gestor = GestorEmail()

    test(gestor)

    gestor.mostrarCorreos()

    #Punto 1

    print("Vamos a cargar su correo\n")
    nombre = input("Ingrese su nombre").title()
    correo = 0
    noSeCargo = True
    while noSeCargo:
        correo = input("Ingrese su correo\n")
        noSeCargo = not gestor.crearCuenta(correo)
    print("Estimado {} te enviaremos tus mensajes a la dirección {}.".format(nombre, correo))

    #Punto 2

    print("\nAhora vamos a cambiar tu contrasenia\n")
    noCambio = True
    while noCambio:
        noCambio = not gestor.setContrasenia(correo)

    #Punto 3

    noTermina = True
    while noTermina:
        correo = input("Ingrese el correo a registrar\n")
        noTermina = not gestor.crearCuenta(correo)    

    #Punto 4

    gestor.crearCuentaConCsv("CorreosACargar", 10)

