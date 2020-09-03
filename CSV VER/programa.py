import pandas as pd
import csv
import datetime

def fechaActual():
    print(datetime.datetime.now())

def listaMarcas():
    print("1 Motorola")
    print("2 Oppo")
    print("3 Honor")

def listaSeries():
    print("1 4354363")
    print("2 63635")
    print("3 234235")

def modificar_csv(codigo, varAModificar, nuevoValor):
    datos = pd.read_csv("productos.csv")
    datos.loc[datos["codigo"]==codigo, varAModificar] = nuevoValor
    datos.to_csv("productos.csv", index=False)

def agregar_csv(nombreArchivo, elementos):
    with open(nombreArchivo, 'a+', newline='') as archivoAEscribir:
        csv_writer = csv.writer(archivoAEscribir)
        csv_writer.writefila(elementos)

def registroDeProducto():
    while True:
        try:
            codigo=int(input("Codigo de producto: "))
        except:
            print("Vuelva a intentarlo")
            continue
        break
    with open('productos.csv') as productos:
        csv_reader = csv.reader(productos, delimiter=',')
        linea = 0
        for fila in csv_reader:
            if linea == 0:
                linea = 1
            else:
                if codigo==int(fila[0]):
                    print("el producto ya esta registrado")
                    return
        nombre=input("Nombre del producto:")
        while True:
            try:
                cantidad=int(input("Cantidad de producto: "))
                while cantidad<=0:
                    print("La cantidad no es valida")
                    cantidad=int(input("Cantidad de producto: "))
            except:
                print("Vuelva a intentarlo")
                continue
            break
        while True:
            try:
                listaMarcas()
                marca=int(input("Marca de producto:"))
                while marca<1 or marca>3:
                    print("Marca no valida")
                    marca=int(input("Marca de producto:"))
            except:
                print("Vuelva a intentarlo")
                continue
            break
        if marca==1:
            seleccionMarca="Alcatel"
        elif marca==2:
            seleccionMarca="Oppo"
        else:
            seleccionMarca="Honor"
        while True:
            try:
                listaSeries()
                serie=int(input("Serie de producto:"))
                while serie<1 or serie>3:
                    print("Serie no valida")
                    serie=int(input("Serie de producto:"))
            except:
                print("Vuelva a intentarlo")
                continue
            break
        if serie==1:
            seleccionSerie="4354363"
        elif serie==2:
            seleccionSerie="63635"
        else:
            seleccionSerie="234235"
        while True:
            try:
                precio=float(input("Precio de producto:"))
                while precio<=0:
                    print("Precio no valido")
                    precio=float(input("Precio de producto:"))
            except:
                print("Vuelva a intentarlo")
                continue
            break
        elementos=[codigo,nombre,cantidad,seleccionMarca,seleccionSerie,precio]
        agregar_csv("productos.csv", elementos)

def pagoDeProducto():
    print("1 Efectivo")
    print("2 Tarjeta de credito")

def ventaDeProducto():
    while True:
        try:
            codigo=int(input("Codigo de producto: "))
        except:
            print("Vuelva a intentarlo")
            continue
        break
    with open('productos.csv') as productos:
        csv_reader = csv.reader(productos, delimiter=',')
        linea = 0
        for fila in csv_reader:
            if linea == 0:
                linea = 1
            else:
                if codigo==int(fila[0]):
                    print("El producto:",fila[1])
                    print("Unidades disponibles:",fila[2])
                    print("Marca de producto:",fila[3])
                    print("Numero de serie de producto",fila[4])
                    print("Precio:",fila[5])
                    while True:
                        try:
                            cantidad=int(input("Cantidad de producto:"))
                            while cantidad<1:
                                print("La cantidad no es valida")
                                cantidad=int(input("Cantidad de producto:"))
                        except:
                            print("Vuelva a intentarlo")
                            continue
                        break
                    if cantidad>int(fila[2]):
                        print("No se pudo completar la compra")
                        return
                    pagoDeProducto()
                    while True:
                        try:
                            pProducto=int(input("Forma de pago de producto:"))
                            while pProducto<1 or pProducto>2:
                                print("Forma no valida")
                                pProducto=int(input("Forma de pago de producto:"))
                            if pProducto==1:
                                formaDePago="Efectivo"
                            else:
                                formaDePago="Tarjeta de credito"
                        except:
                            print("Vuelva a intentarlo")
                            continue
                        break

                    pTotal=cantidad*float(fila[5])
                    print("Pagara",pTotal)
                    elementos=[codigo,fila[1],cantidad,formaDePago,fila[3],fila[4],pTotal]
                    modificar_csv(codigo,"cantidad",int(fila[2])-cantidad)
                    agregar_csv("reporte.csv",elementos)
                    return
        print("No existe")

def listaDeProducto():
    marcas=[]
    with open("reporte.csv") as reportes:
        csv_reader = csv.reader(reportes, delimiter=',')
        linea = 0
        for fila in csv_reader:
            if linea == 0:
                linea = 1
            else:
                marcas.append(fila[4])
        marcas.sort()
        for marca in marcas:
            print("Productos de la marca",marca)
            print("Codigo:",fila[0])
            print("nombre del producto:",fila[1])
            print("Forma de pago:",fila[3])
            print("Cantidad vendida:",fila[2])
            print("numero de serie:",fila[5])
            print("Total:",fila[6])

def actualizacionDeProducto():
    while True:
        try:
            codigo=int(input("Codigo de producto: "))
        except:
            print("Vuelva a intentarlo")
            continue
        break
    with open('productos.csv') as productos:
        csv_reader = csv.reader(productos, delimiter=',')
        linea = 0
        for fila in csv_reader:
            if linea == 0:
                linea = 1
            else:
                if codigo==int(fila[0]):
                    while True:
                        try:
                            cambiarNombre=int(input("Desea cambiar el nombre del producto: (1/0):"))
                            while cambiarNombre!=1 and cambiarNombre!=0:
                                print("Valor invalido")
                                cambiarNombre=int(input("Desea cambiar el nombre del producto: (1/0):"))
                        except:
                            print("Vuelva a intentarlo")
                            continue
                        break
                    if cambiarNombre==1:
                        nombre=input("Nuevo nombre: ")
                        modificar_csv(codigo,"nombre",nombre)
                    while True:
                        try:
                            cambiarCantidad=int(input("Desea cambiar la cantidad existente del producto: (1/0):"))
                            while cambiarCantidad!=1 and cambiarCantidad!=0:
                                print("Valor invalido")
                                cambiarCantidad=int(input("Desea cambiar la cantidad existente del producto: (1/0):"))
                        except:
                            print("Vuelva a intentarlo")
                            continue
                        break
                    if cambiarCantidad==1:
                        while True:
                            try:
                                cantidad=int(input("Cantidad de producto: "))
                                while cantidad<=0:
                                    print("La cantidad no es valida")
                                    cantidad=int(input("Cantidad de producto: "))
                            except:
                                print("Vuelva a intentarlo")
                                continue
                            break
                        modificar_csv(codigo,"cantidad",cantidad)
                    while True:
                        try:
                            cambiarMarca=int(input("Desea cambiar la marca del producto: (1/0):"))
                            while cambiarMarca!=1 and cambiarMarca!=0:
                                print("Valor invalido")
                                cambiarMarca=int(input("Desea cambiar la marca del producto: (1/0):"))
                        except:
                            print("Vuelva a intentarlo")
                            continue
                        break
                    if cambiarMarca==1:
                        while True:
                            try:
                                listaMarcas()
                                marca=int(input("Marca de producto:"))
                                while marca<1 or marca>3:
                                    print("Marca no valida")
                                    marca=int(input("Marca de producto:"))
                            except:
                                print("Vuelva a intentarlo")
                                continue
                            break
                        if marca==1:
                            seleccionMarca="Alcatel"
                        elif marca==2:
                            seleccionMarca="Oppo"
                        else:
                            seleccionMarca="Honor"
                        modificar_csv(codigo,"marca",seleccionMarca)
                    while True:
                        try:
                            cambiarNSerie=int(input("Desea cambiar el numero de serie del producto: (1/0):"))
                            while cambiarNSerie!=1 and cambiarNSerie!=0:
                                print("Valor invalido")
                                cambiarNSerie=int(input("Desea cambiar el numero de serie del producto: (1/0):"))
                        except:
                            print("Vuelva a intentarlo")
                            continue
                        break
                    if cambiarNSerie==1:
                        while True:
                            try:
                                listaSeries()
                                serie=int(input("Serie de producto:"))
                                while serie<1 or serie>3:
                                    print("Serie no valida")
                                    serie=int(input("Serie de producto:"))
                            except:
                                print("Vuelva a intentarlo")
                                continue
                            break
                        if serie==1:
                            seleccionSerie="4354363"
                        elif serie==2:
                            seleccionSerie="63635"
                        else:
                            seleccionSerie="234235"
                        modificar_csv(codigo,"numeroserie",seleccionSerie)
                    while True:
                        try:
                            cambiarPrecio=int(input("Desea cambiar el precio del producto: (1/0):"))
                            while cambiarPrecio!=1 and cambiarPrecio!=0:
                                print("Valor invalido")
                                cambiarPrecio=int(input("Desea cambiar el precio del producto: (1/0):"))
                        except:
                            print("Vuelva a intentarlo")
                            continue
                        break
                    if cambiarPrecio==1:
                        while True:
                            try:
                                precio=float(input("Precio de producto:"))
                                while precio<=0:
                                    print("Precio no valido")
                            except:
                                print("Vuelva a intentarlo")
                                continue
                            break
                        modificar_csv(codigo,"precio",precio)
                    return
    print("No existe")

def usuario(usuario, contraseña):
    with open('acceso.csv') as archivoInicioDeSesion:
        csv_reader = csv.reader(archivoInicioDeSesion, delimiter=',')
        linea = 0
        for fila in csv_reader:
            if linea == 0:
                linea = 1
            else:
                if usuario==fila[0] and contraseña==fila[1]:
                    return True
        return False

print('                                             88           88  ')
print('                                             88           88  ')
print('                                             88           88  ')
print('8b      db      d8   ,adPPYba,   8b,dPPYba,  88   ,adPPYb,88  ')
print('`8b    d88b    d8   a8"     "8a  88P    "Y8  88  a8"    `Y88  ')
print(' `8b  d8 `8b  d8    8b       d8  88          88  8b       88  ')
print('  `8bd8   `8bd8     "8a,   ,a8"  88          88  "8a,   ,d88  ')
print('    YP      YP       `"YbbdP"    88          88   `"8bbdP"Y8  ')
fechaActual()
nusuario=input("Nombre de usuario: ")
contraseña=input("Contraseña:")

acceso=usuario(nusuario,contraseña)
if acceso == True:
    seleccion=''
    while seleccion!=5:
        print("\n")
        print("1- Registro de Celulares")
        print("2- Venta de Celulares")
        print("3- Lista de Productos Vendidos por Marca")
        print("4- Actualizar Producto")
        print("5- Salir")
        fechaActual()
        while True:
            try:
                seleccion=int(input("Elija su opcion:"))
                while seleccion<1 or seleccion>5:
                    print("Valor invalido")
                    seleccion=int(input("Elija su opcion:"))
            except:
                print("Vuelva a intentarlo")
                continue
            break
        if seleccion==1:
            registroDeProducto()
        elif seleccion==2:
            ventaDeProducto()
        elif seleccion==3:
            listaDeProducto()
        elif seleccion==4:
            actualizacionDeProducto()
        else:
            break

else:
    print("No se pudo iniciar sesion")
