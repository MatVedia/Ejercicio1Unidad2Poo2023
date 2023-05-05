class Email():

    def __init__(self, id, dom, tipoDom, contra):
        self.__idCuenta = id
        self.__dominio = dom
        self.__tipoDominio = tipoDom
        self.__contrasenia = contra

    def getDominio(self):
        return '@' + self.__dominio
    
    def retornaEmail(self):
        return self.__idCuenta + self.getDominio() + '.' + self.__tipoDominio
    
    def setContrasenia(self, contraseniaIngresada):
        resultCambio = False
        if contraseniaIngresada == self.__contrasenia:
            sonDistintas = True
            while sonDistintas:
                nuevaContra = input("Ingrese su nueva contrasenia\n")
                copiaContra = input("Una vez mas\n")
                sonDistintas = nuevaContra != copiaContra
                if sonDistintas:
                    print("Error. Las contrasenias no coinciden. Intentelo una vez mas.")
                else:
                    self.__contrasenia = nuevaContra
                    resultCambio = True
        return resultCambio
    

