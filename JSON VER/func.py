import json
import os
import getpass
import datetime

lstOpciones = {1: 'Registro de Celulares', 2: 'Venta de Celulares', 3: 'Lista de Productos Vendidos por Marca', 4: 'Actualizar Producto', 5: 'Salir'}
lstMarcas = {1: 'Samsung', 2: 'Huawei', 3: 'iPhone (Apple)', 4: 'Sony', 5: 'Alcatel', 6: 'Honor'}
lstNumSerie = {1: '233246654345', 2: '7544534534', 3: '55435435434', 4: '643643636', 5: '4856457'}

def anadir(data, filename):
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) 

def pIni():
    print('               @@@@@@%                                                          ')
    print('           &@@@@@@@@@%                                                          ')
    print('          @@@@@@@@@@%@@@%.                                                      ')
    print('          @@@@@@@  @@@@@@@                                                      ')
    print('       @# @@@@@@@  @@@@@@@.                                @&,                  ')
    print('     @@@@@@@@@@@#      .@@@@@@@                          @@@@@@@                ')
    print('     @@@@@@@            @@@@@@@                     /@@@@@@@@@@@                ')
    print('     @@@@@@@            .%@@@#@@@@@@#            @@@@@@@@@@.#@@@@@@@@           ')
    print('     @@@@@@@                 @@@@@@@@@@@@@@@@%.%@@@@@@@@@@   ,@@@@@@@           ')
    print('     @@@@@@@                 @@@@@@@@@@@@@@@@@@@@@@@@@       ,@@@@@@@           ')
    print('     @@@@@@@                       /@@@@@@@@@@@@@@           ,@@@@@@@           ')
    print('     @@@@@@@                                .&@@              #@@@@&@@@@@       ')
    print('     @@@@@@@       @@@@@@@                                        @@@@@@@       ')
    print('     @@@@@@@       @@@@@@@                                        @@@@@@@       ')
    print('     @@@@@@@        &@@@@                                         @@@@@@@       ')
    print('     @@@@@@@                                                      @@@@@@@       ')
    print('     @@@@@@%@@@*              *@#                        @@@@@@@  @@@@@@@       ')
    print('          @@@@@@@            @@@@@@@    @@.              @@@@@@@  @@@@@@@       ')
    print('          @@@@@@@            @@@@@@@  @@@@@@@    #@(     *@@@@(   @@@@@@@       ')
    print('          @@@@@@@              ,&&@@@@@@@@@@@  %@@@@@@(           @@@@@@@       ')
    print('          @@@@@@@/               @@@@@@@ &@@@@@@@@@@@@(           @@@@@@@       ')
    print('              (@@@@@@@@@@@       &@@@@@.   @@@@@@@*@/             @@@@@@@       ')
    print('              (@@@@@@@@@@@                 @@@@@@             @@@@@@@@@@@       ')
    print('                *@@@@@@@@@@@                                 ,@@@@@@@&@.        ')
    print('                        @@@@@@@@@@@@@/                /      ,@@@@@@@           ')
    print('                        @@@@@@@@@@@@@@@@@@@@@@(     @@@@@@@@@@@@@@@@@           ')
    print('                          .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@             ')
    print('                                    (@@@@@@@@@@@@@@@@@@@@@@@@@@(                ')
    print('                                             ,@@@@@@@@                          ')

def fecha():
    return (f'{datetime.datetime.now().strftime("%x")} {datetime.datetime.now().strftime("%X")}')

def login(user, passw):
    with open('login.json') as login_file: 
        users = json.load(login_file) 
    login_file.close()
    for item in users['usuarios']:
        if (item['usuario'] == user and item['contrasena'] == passw):
            return True
    return False

def opciones():
    for opc in lstOpciones:
        print(f'{opc}.- {lstOpciones[opc]}')

def RegDeCel():
    print(fecha())
    print('\n\tRegistro de Celulares\n')
    while True:
        existe=False
        while True:
            try:
                codProd = int(input('Ingrese el código del producto: '))
                while(codProd<1):
                    print('Ingreso inválido')
                    codProd = int(input('Ingrese el código del producto: '))
            except:
                print('Error')
                continue
            break
        with open('data.json') as data_file: 
            data = json.load(data_file) 
        data_file.close()
        for item in data['entries']:
            if item['codigo'] == codProd:
                print('\nEl producto ya existe\n')
                os.system('pause')
                existe=True
                break
        if existe:
            continue
        break
    nombreProd = input('Ingrese el nombre del producto: ')
    while True:
        try:
            cantidad = int(input('Ingrese la cantidad a ingresar: '))
            while cantidad<1:
                print('Ingreso inválido')
                cantidad = int(input('Ingrese la cantidad a ingresar: '))
        except:
            print('Error')
            continue
        break

    for marcas in lstMarcas:
        print(f'{marcas}.- {lstMarcas[marcas]}')
    while True:
        try:
            marca = int(input('Seleccione la marca: '))
            while marca <1 or marca >len(lstMarcas):
                print('Ingreso inválido')
                marca = int(input('Seleccione la marca: '))
        except:
            print('Error')
            continue
        break
    for series in lstNumSerie:
        print(f'{series}.- {lstNumSerie[series]}')
    while True:
        try:
            serie = int(input('Seleccione el número de serie: '))
            while serie <1 or serie >len(lstNumSerie):
                print('Ingreso inválido')
                serie = int(input('Seleccione el número de serie: '))
        except:
            print('Error')
            continue
        break
    while True:
        try:
            prec = float(input('Ingrese el precio del producto: '))
            while prec<0:
                print('Ingreso Inválido')
                prec = float(input('Ingrese el precio del producto: '))
        except:
            print('Error')
            continue
        break

    with open('data.json') as data_file: 
        data = json.load(data_file) 
        temp = data['entries'] 
        nuevoIngreso = {'codigo': codProd, 'nombre': nombreProd, 'cantidad': cantidad, 'marca': lstMarcas[marca], 'serie': lstNumSerie[serie], 'precio': prec}
        temp.append(nuevoIngreso)
    data_file.close()
    anadir(data,'data.json')
    print(f'\n{nombreProd} añadido')
    os.system('pause')

def VentDeCel():
    print(fecha())
    def formaPago():
        print('\nSeleccion su forma de pago')
        lstFormaPag = {1: 'Tarjeta crédito/débito', 2: 'Efectivo', 3: 'Cheque'}
        for forma in lstFormaPag:
            print(f'{forma}.- {lstFormaPag[forma]}')
        while True:
            try:
                seleccionPago = int(input('Selección: '))
                while seleccionPago<1 or seleccionPago>len(lstFormaPag):
                    print('Ingreso inválido')
                    seleccionPago = int(input('Selección: '))
            except:
                print('Error')
                continue
            break
        return lstFormaPag[seleccionPago]
    print('Venta de Celulares')
    while True:
        while True:
            try:
                codProd = int(input('Ingrese el código del producto: '))
                while codProd<1:
                    print('Error')
                    codProd = int(input('Ingrese el código del producto: '))
            except:
                print('Error')
                continue
            break
        with open('data.json', 'r') as data_file: 
            data = json.load(data_file) 
        data_file.close()   
        for item in data['entries']:
            if item['codigo'] == codProd:
                print(f"\nNombre: {item['nombre']}\nStock: {item['cantidad']}\nMarca: {item['marca']}\nNúmero de Serie: {item['serie']}\nPrecio: {item['precio']}")
                while True:
                    while True:
                        try:
                            cant = int(input('Ingrese la cantidad que desea: '))
                            while cant<1:
                                print('Ingrese una cantidad válida')
                                cant = int(input('Ingrese la cantidad que desea: '))
                        except:
                            print('Error')
                            continue
                        break
                    if cant > item['cantidad']:
                        print('No hay suficiente stock')
                        os.system('pause')
                        continue
                    break
                for item in data['entries']:
                    if item['codigo'] == codProd:
                        item['cantidad'] = item['cantidad']-cant
                        break
                with open('data.json', 'w') as data_file:
                    json.dump(data,data_file)
                forma = formaPago()
                total = float(round(float(item['precio'])*cant,2))
                print(f'|---Recibo---|')
                print(f"|Producto   {item['nombre']}|")
                print(f"|Precio Unit   {item['precio']}|")
                print(f"|Subtotal   {total}|")
                print(f'|Forma de Pago   {forma}')
                print(f'|Fecha    {fecha()}|')
                print(f'|------------------|')
                print(f"|TOTAL      {total}|")
                print(f'|-------------|\n')
                
                with open('reporte.json') as reporte_file: 
                    data = json.load(reporte_file) 
                    temp = data['ventas']
                try:
                    temp[item['marca']].append({'codigo': codProd, 'nombre': item['nombre'], 'cantidad': cant, 'serie': item['serie'], 'fecha': fecha(), 'precioUni': float(item['precio']), 'subtotal': total, 'total': total})
                except:
                    temp[item['marca']] = [{'codigo': codProd, 'nombre': item['nombre'], 'cantidad': cant, 'serie': item['serie'], 'fecha': fecha(), 'precioUni': float(item['precio']), 'subtotal': total, 'total': total}]
                reporte_file.close()
                anadir(data,'reporte.json')
                os.system('pause')
                return
        print('No se encontró el producto\n')
        os.system('pause')
        continue

def ListDeProdVend():
    print(fecha())
    print('\nLista de Productos Vendidos por Marca\n')
    with open('reporte.json') as reporte_file:
        data = json.load(reporte_file)
        temp = data['ventas']  
    for marca in sorted(dict(temp), reverse=True):
        print(f'Productos {marca} vendidos:')
        for producto in temp[marca]:
            print(f"Código: {producto['codigo']}\nNombre: {producto['nombre']}\nCantidad Vendida: {producto['cantidad']}\nSerie: {producto['serie']}\nFecha de Venta: {producto['fecha']}\nPrecio Unitario: {producto['precioUni']}\nSubtotal: {producto['subtotal']}\nTotal: {producto['total']}\n")
    os.system('pause')

def ActuProd():
    print(fecha())
    print('Actualizar Producto\n')
    with open('data.json') as data_file:
        data = json.load(data_file)
    while True:
        while True:
            try:
                codProd = int(input('Ingrese el código del producto a modificar: '))
                while codProd<1:
                    print('Ingreso invalido')
                    codProd = int(input('Ingrese el código del producto a modificar: '))
            except:
                print('Error')
                continue
            break
        for item in data['entries']:
            if item['codigo'] == codProd:
                while True:
                    try:
                        editN = input(f"Quiere modificar el nombre {item['nombre']}: ").lower()
                        while editN != 's' and editN != 'n':
                            print('Haga una selección válida')
                            editN = input(f"Quiere modificar el nombre {item['nombre']}: ").lower()
                    except:
                        print('Error')
                        continue
                    break

                while True:
                    try:
                        editC = input(f"Quiere modificar la cantidad {item['cantidad']}: ").lower()
                        while editC != 's' and editC != 'n':
                            print('Haga una selección válida')
                            editC = input(f"Quiere modificar la cantidad {item['cantidad']}: ").lower()
                    except:
                        print('Error')
                        continue
                    break

                while True:
                    try:
                        editM = input(f"Quiere modificar la marca {item['marca']}: ").lower()
                        while editM != 's' and editM != 'n':
                            print('Haga una selección válida')
                            editM = input(f"Quiere modificar la marca {item['marca']}: ").lower()
                    except:
                        print('Error')
                        continue
                    break

                while True:
                    try:
                        editS = input(f"Quiere modificar el número de serie {item['serie']}: ").lower()
                        while editS != 's' and editS != 'n':
                            print('Haga una selección válida')
                            editS = input(f"Quiere modificar el número de serie {item['serie']}: ").lower()
                    except:
                        print('Error')
                        continue
                    break

                while True:
                    try:
                        editP = input(f"Quiere modificar el precio {item['precio']}: ").lower()
                        while editP != 's' and editP != 'n':
                            print('Haga una selección válida')
                            editP = input(f"Quiere modificar el precio {item['precio']}: ").lower()
                    except:
                        print('Error')
                        continue
                    break
                
                if editN == 's':
                    print('Modificando nombre')
                    nombre = input('Ingrese el nuevo nombre: ')
                    for item in data['entries']:
                        if item['codigo'] == codProd:
                            item['nombre'] = nombre
                            break
                    with open('data.json', 'w') as data_file:
                        json.dump(data,data_file)
                if editC == 's':
                    print('Modificando cantidad')
                    while True:
                        try:
                            cantidad = int(input('Ingrese la nueva cantidad: '))
                            while cantidad<1:
                                print('Ingrese una cantidad válida')
                                cantidad = int(input('Ingrese la nueva cantidad: '))
                        except:
                            print('Error')
                            continue
                        break
                    for item in data['entries']:
                        if item['codigo'] == codProd:
                            item['cantidad'] = cantidad
                            break
                    with open('data.json', 'w') as data_file:
                        json.dump(data,data_file)
                if editM == 's':
                    print('Modificanto marca')
                    for marcas in lstMarcas:
                        print(f'{marcas}.- {lstMarcas[marcas]}')
                    while True:
                        try:
                            marca = int(input('Seleccione la marca: '))
                            while marca <1 or marca >len(lstMarcas):
                                print('Ingreso inválido')
                                marca = int(input('Seleccione la marca: '))
                        except:
                            print('Error')
                            continue
                        break
                    for item in data['entries']:
                        if item['codigo'] == codProd:
                            item['marca'] = lstMarcas[marca]
                            break
                    with open('data.json', 'w') as data_file:
                        json.dump(data,data_file)
                if editS == 's':
                    print('Modificando numero de serie')
                    for series in lstNumSerie:
                        print(f'{series}.- {lstNumSerie[series]}')
                    while True:
                        try:
                            serie = int(input('Seleccione el número de serie: '))
                            while serie <1 or serie >len(lstNumSerie):
                                print('Ingreso inválido')
                                serie = int(input('Seleccione el número de serie: '))
                        except:
                            print('Error')
                            continue
                        break
                    for item in data['entries']:
                        if item['codigo'] == codProd:
                            item['serie'] = lstNumSerie[serie]
                            break
                    with open('data.json', 'w') as data_file:
                        json.dump(data,data_file)
                if editP == 's':
                    print('Modificando precio')
                    while True:
                        try:
                            precio = float(input('Ingrese el nuevo precio: '))
                            while precio<1:
                                print('Ingrese una cantidad válida')
                                precio = float(input('Ingrese el nuevo precio: '))
                        except:
                            print('Error')
                            continue
                        break
                    for item in data['entries']:
                        if item['codigo'] == codProd:
                            item['precio'] = precio
                            break
                    with open('data.json', 'w') as data_file:
                        json.dump(data,data_file)
                os.system('pause')
                return
        print('No se encontró el producto\n')
        os.system('pause')
        continue