from ClaseEmail import Email
import csv

class GestorEmail():

    def __init__(self):
        self.__listaCorreos= []

    def __buscarCorreo(self, correoBuscado):
        i = 0
        N = len(self.__listaCorreos)
        while i < N and self.__listaCorreos[i].retornaEmail() != correoBuscado:
            i += 1
        if i == N:
            i = -1
        return i

    def crearCuenta(self, nuevoCorreo):
        resultado = False
        posiArroba = nuevoCorreo.find('@')
        if posiArroba != -1 and posiArroba != 0:
            posiPunto = nuevoCorreo.find('.', posiArroba+1)
            if posiPunto != -1 and posiPunto != len(nuevoCorreo)-1:
                if not self.__buscarCorreo(nuevoCorreo) == -1:
                    resultado = None
                else:
                    id = nuevoCorreo[0 : posiArroba]
                    dom = nuevoCorreo[posiArroba+1 : posiPunto]
                    tipoDom = nuevoCorreo[posiPunto+1 : len(nuevoCorreo)]
                    contrasenia = input("Ingrese la contrasenia para {}\n".format(nuevoCorreo))
                    self.__listaCorreos.append(Email(id, dom, tipoDom, contrasenia))
                    resultado = True
        if resultado == False:
            print("Error. El correo ingresado no es valido.")
        elif resultado == None:
            print("Error. El correo ingresado {} ya esta registrado.".format(nuevoCorreo))
            resultado = False
        return resultado
    
    def setContrasenia(self, correo):
        result = False
        posiCorreo = self.__buscarCorreo(correo)
        if posiCorreo != -1:
            contraIngresada = input("Ingrese su contrasenia actual\n")
            self.__listaCorreos[posiCorreo].setContrasenia(contraIngresada)
            result = True
        return result
    
    def crearCuentaConCsv(self, nomArchivo, cant):
        archi = open(nomArchivo.replace('.csv', '')+'.csv', 'r')
        reader = csv.reader(archi, delimiter=',')
        i = 0
        correo = 0
        while i < cant and correo in reader:
            i += 1
            self.crearCuenta(correo)
        archi.close()            