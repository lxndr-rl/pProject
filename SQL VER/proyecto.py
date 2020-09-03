import sqlite3
import datetime
import os

def fecha():
    now = datetime.datetime.now()  #FECHA Y HORA
    return now

con = sqlite3.connect('datos.db')
sentenc = con.cursor()

def logo():
    print("_________ _       _________")
    print("\__   __/| \    /|\__    _/")
    print("   ) (   |  \  ( |   |  |  ")
    print("   | |   |   \ | |   |  |  ")
    print("   | |   | (\ \) |   |  |  ")
    print("   | |   | | \   |   |  |  ")
    print("   | |   | )  \  ||\_/  /  ")
    print("   \_/   |/    \_/\____/   ")


def menu():
    print("***Menu de opciones***")
    print("1. Registro de Celulares")
    print("2. Venta de Celulares")
    print("3. Lista de Productos Vendidos por Marca")
    print("4. Actualizar Producto")
    print("5. Salir")
    while True:
        try:
            seleccion = int(input("Seleccione una opcion: "))
            while seleccion <1 or seleccion>5:
                print("Seleccione una de la lista")
                seleccion = int(input("Seleccione una opcion: "))
        except:
            print("Algo salio mal")
            continue
        break
    return seleccion
def marcas():
        print("***Marcas de Celulares***")
        print("1. Samsung")
        print("2. Huawei")
        print("3. iPhone")
        while True:
            try:
                selMarca = int(input("Seleccione una marca: "))
                while selMarca <1 or selMarca>3:
                    print("Seleccione una de la lista")
                    selMarca = int(input("Seleccione una marca: "))
            except:
                print("Algo salio mal")
                continue
            break
        if selMarca==1:
            marca='Samsung'
        elif selMarca==2:
            marca='Huawei'
        else:
            marca='iPhone'
        return marca
def series():
    print("***Series de Celulares***")
    print("1. 382383")
    print("2. 2354235")
    print("3. 34535")
    while True:
        try:
            selSerie = int(input("Seleccione un numero de serie: "))
            while selSerie <1 or selSerie>3:
                print("Seleccione una de la lista")
                selSerie = int(input("Seleccione un numero de serie: "))
        except:
            print("Algo salio mal")
            continue
        break
    if selSerie==1:
         nserie='382383'
    elif selSerie==2:
        nserie='2354235'
    else:
        nserie='34535'
    return nserie
def registro():
    print("Registro de Celulares")
    while True:
        try:
            codigo = int(input("Ingrese el código: "))
            while codigo<1:
                print("Ingrese un código valido")
        except:
            print("Algo salio mal")
            continue
        break
    sentenc.execute("SELECT * FROM DATOS")
    rows = sentenc.fetchall()
    for row in rows:
        if codigo == row[0]:
            print("\n\tEl producto ya existe")
            return
    nombre = input("Ingrese el nombre: ")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            while cantidad<1:
                print("Ingrese una cantidad valida")
                cantidad = int(input("Ingrese la cantidad: "))
        except:
            print("Algo salio mal")
            continue
        break
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            while precio<1:
                print("Ingrese una cantidad valida")
                precio = float(input("Ingrese el precio: "))
        except:
            print("Algo salio mal")
            continue
        break
    nserie = series()
    marca = marcas()
    valores = (codigo, nombre, cantidad, marca, nserie, precio)
    sentenc.execute('''INSERT INTO DATOS(CODIGO, NOMBRE, CANTIDAD, MARCA, NSERIE, PRECIO) VALUES(?, ?, ?, ?, ?, ?)''', valores)
    con.commit()

def venta():
    print("Venta de Producto")
    while True:
        try:
            codigo = int(input("Ingrese el código: "))
            while codigo<1:
                print("Ingrese un código valido")
        except:
            print("Algo salio mal")
            continue
        break
    sentenc.execute("SELECT * FROM DATOS")
    rows = sentenc.fetchall()
    existe=0
    for row in rows:
        if codigo == row[0]:
            existe = 1
            break
    if existe==0:
        print("El producto no existe")
        return
    print("El producto",row[1],"tiene",row[2],"cantidades disponibles","\nEs de la marca",row[3],"con numero de serie",row[4],"\nCuesta",row[5])
    while True:
        try:
            cantidad = int(input("Cuantos desea?: "))
            while cantidad<1:
                print("Ingrese una cantidad valida")
                cantidad = int(input("Cuantos desea?: "))
        except:
            print("Algo salio mal")
            continue
        break
    if row[2]<cantidad:
        print("Solo tenemos",row[2],"disponibles y usted quiere",cantidad)
        return
    total = cantidad*row[5]
    print("Su compra tiene un total de",total)
    valores = (row[3], row[0], row[1], cantidad, row[4], row[5], total)
    sentenc.execute('''UPDATE DATOS SET CANTIDAD = ? WHERE CODIGO = ?''',(row[2]-cantidad, codigo))
    con.commit()
    sentenc.execute('''INSERT INTO VENTAS(MARCA, CODIGO, NOMBRE, CVENDIDA, NSERIE, PRECIO, TOTAL) VALUES(?, ?, ?, ?, ?, ?, ?)''', valores)
    con.commit()

def lista():
    print("Lista de Productos Vendidos Por Marca")
    sentenc.execute("SELECT * FROM VENTAS")
    rows = sentenc.fetchall()
    lista = []
    for row in rows:
        lista.append(row)
    lista.sort()
    ok = ''
    for item in lista:
        if item[0]!=ok:
            ok = item[0]
            print("\nProductos vendidos de la marca",ok,":")
        print("Codigo",item[1],"nombre del producto",item[2],"\nCantidad vendida",item[3],"numero de serie",item[4],"\nPrecio",item[5],"Total",item[6],"\n")

def actualizar():
    print("Actualizar Producto")
    while True:
        try:
            codigo = int(input("Ingrese el codigo: "))
            while codigo<1:
                print("Ingrese un codigo valido")
        except:
            print("Algo salio mal")
            continue
        break
    sentenc.execute("SELECT * FROM DATOS")
    rows = sentenc.fetchall()
    existe=0
    for row in rows:
        if codigo == row[0]:
            existe = 1
            break
    if existe==0:
        print("El producto no existe")
        return
    while True:
        try:
            modificaNombre = input("Quiere modificar el nombre (S - N): ").upper()
            while modificaNombre != "S" and modificaNombre != "N":
                print("Haga una selección valida")
                modificaNombre = input("Quiere modificar el nombre (S - N): ").upper()
        except:
            print("Algo salio mal")
            continue
        break
    while True:
        try:
            modificaCantidad = input("Quiere modificar la cantidad (S - N): ").upper()
            while modificaCantidad != "S" and modificaCantidad != "N":
                print("Haga una selección valida")
                modificaCantidad = input("Quiere modificar la cantidad (S - N): ").upper()
        except:
            print("Algo salio mal")
            continue
        break
    while True:
        try:
            modificaMarca = input("Quiere modificar la marca (S - N): ").upper()
            while modificaMarca != "S" and modificaMarca != "N":
                print("Haga una selección valida")
                modificaMarca = input("Quiere modificar la marca (S - N): ").upper()
        except:
            print("Algo salio mal")
            continue
        break
    while True:
        try:
            modificaSerie = input("Quiere modificar el numero de serie (S - N): ").upper()
            while modificaSerie != "S" and modificaSerie != "N":
                print("Haga una selección valida")
                modificaSerie = input("Quiere modificar el numero de serie (S - N): ").upper()
        except:
            print("Algo salio mal")
            continue
        break
    while True:
        try:
            modificaPrecio = input("Quiere modificar el precio (S - N): ").upper()
            while modificaPrecio != "S" and modificaPrecio != "N":
                print("Haga una selección valida")
                modificaPrecio = input("Quiere modificar el precio (S - N): ").upper()
        except:
            print("Algo salio mal")
            continue
        break

    if modificaNombre == 'S':
        print('Modificando nombre')
        nombre = input("Ingrese el nuevo nombre: ")
        sentenc.execute('''UPDATE DATOS SET NOMBRE = ? WHERE CODIGO = ?''', (nombre, codigo))
        con.commit()
    if modificaCantidad == 'S':
        print('Modificando cantidad')
        while True:
            try:
                cantidad = int(input("Ingrese la nueva cantidad: "))
                while cantidad<1:
                    print("Ingrese una cantidad valida")
                    cantidad = int(input("Ingrese la nueva cantidad: "))
            except:
                print("Algo salio mal")
                continue
            break
        sentenc.execute('''UPDATE DATOS SET CANTIDAD = ? WHERE CODIGO = ?''', (cantidad, codigo))
        con.commit()
    if modificaMarca == 'S':
        print('Modificanto marca')
        marca = marcas()
        sentenc.execute('''UPDATE DATOS SET MARCA = ? WHERE CODIGO = ?''', (marca, codigo))
        con.commit()
    if modificaSerie == 'S':
        print('Modificando numero de serie')
        serie = series()
        sentenc.execute('''UPDATE DATOS SET NSERIE = ? WHERE CODIGO = ?''', (serie, codigo))
        con.commit()
    if modificaPrecio == 'S':
        print('Modificando precio')
        while True:
            try:
                precio = float(input("Ingrese el nuevo precio: "))
                while precio<1:
                    print("Ingrese una cantidad valida")
                    precio = float(input("Ingrese el nuevo precio: "))
            except:
                print("Algo salio mal")
                continue
            break
        sentenc.execute('''UPDATE DATOS SET PRECIO = ? WHERE CODIGO = ?''', (precio, codigo))
        con.commit()

def inciaSesion(usuario,contraseña):
    sentenc.execute("SELECT * FROM USUARIOS")
    rows = sentenc.fetchall()
    for row in rows:
        if usuario == row[0] and contraseña == row[1]:
            return True
    return False

logo()
print(fecha())
while True:
    usuario = input('Ingrese su usuario: ')
    contraseña = input('Ingrese su contraseña: ')
    if inciaSesion(usuario,contraseña):
        break
    else:
        print('error')
os.system("CLS")

while True:
    print(fecha())
    seleccion = menu()
    if seleccion==1:
        registro()
        os.system("PAUSE")
        os.system("CLS")


    elif seleccion==2:
        venta()
        os.system("PAUSE")
        os.system("CLS")

    elif seleccion==3:
        lista()
        os.system("PAUSE")
        os.system("CLS")

    elif seleccion==4:
        actualizar()
        os.system("PAUSE")
        os.system("CLS")

    else:
        break

con.close()
