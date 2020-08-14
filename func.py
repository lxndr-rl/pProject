import json
import os
import datetime

lstOpciones = {1: 'Registro de Celulares', 2: 'Venta de Celulares', 3: 'Lista de Productos Vendidos por Marca', 4: 'Actualizar Producto', 5: 'Salir'}
lstMarcas = {1: 'Samsung', 2: 'Huawei', 3: 'iPhone (Apple)', 4: 'Sony'}
lstNumSerie = {1: '233246654345', 2: '7544534534', 3: '55435435434', 4: '643643636'}

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

def mostrarFecha():
    fecha = (f'{datetime.datetime.now().strftime("%x")} {datetime.datetime.now().strftime("%X")}')
    return fecha

def login(user, passw):
    with open('login.json') as login_file: 
        users = json.load(login_file) 
    login_file.close()
    for item in users['usuarios']:
        if (item['usuario'] == user and item['contrasena'] == passw):
            return True
        else:
            return False

def opciones():
    for opc in lstOpciones:
        print(f'{opc}.- {lstOpciones[opc]}')

def RegDeCel():
    def anadir(data, filename='data.json'): 
        with open(filename,'w') as f: 
            json.dump(data, f, indent=4) 
    print('\n\tRegistro de Celulares\n')
    codProd = int(input('Ingrese el código del producto: '))
    with open('data.json') as data_file: 
        data = json.load(data_file) 
    data_file.close()
    for item in data['entries']:
        if item['codigo'] == codProd:
            print('\nEl producto ya existe\n')
            os.system('pause')
            return
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
    anadir(data)
    print(f'\n{nombreProd} añadido')
    os.system('pause')

def VentDeCel():
    def anadir(data, filename='reporte.json'): 
        with open(filename,'w') as f: 
            json.dump(data, f, indent=4) 
    encontrado = False
    def formaPago():
        print('\nSeleccion su forma de pago')
        lstFormaPag = {1: 'Tarjeta crédito/débito', 2: 'Efectivo', 3: 'Cheque'}
        for forma in lstFormaPag:
            print(f'{forma}.- {lstFormaPag[forma]}')
        return lstFormaPag[int(input('Selección: '))]
    print('Venta de Celulares')
    codProd = int(input('Ingrese el código del producto: '))
    with open('data.json', 'r') as data_file: 
        data = json.load(data_file) 
    data_file.close()   
    for item in data['entries']:
        if item['codigo'] == codProd:
            encontrado = True
            break
    if encontrado:
        print(f"\nNombre: {item['nombre']}\nStock: {item['cantidad']}\nMarca: {item['marca']}\nNúmero de Serie: {item['serie']}\nPrecio: {item['precio']}")
    else:
        print('No se encontró el producto\n')
        os.system('pause')
        return
    cant = int(input('Ingrese la cantidad que desea: '))
    if cant > item['cantidad']:
        print('No hay suficiente stock')
        os.system('pause')
        return
    for item in data['entries']:
        if item['codigo'] == codProd:
            item['cantidad'] = item['cantidad']-cant
            break
    with open('data.json', 'w') as data_file:
        json.dump(data,data_file)
    forma = formaPago()
    print(f'|---Recibo---|')
    print(f"|Producto   {item['nombre']}|")
    print(f"|Precio Unit   {item['precio']}|")
    print(f"|Subtotal   {item['precio']*cant}|")
    print(f'|Forma de Pago   {forma}')
    print(f'|------------------|')
    print(f"|TOTAL      {item['precio']}|")    #FALTA AGREGAR IMPUESTO
    print(f'|-------------|\n')
    
    with open('reporte.json') as reporte_file: 
        data = json.load(reporte_file) 
        temp = data['ventas']
    try:
        temp[item['marca']].append({'codigo': codProd, 'nombre': item['nombre'], 'cantidad': cant, 'serie': item['serie'], 'precioUni': item['precio'], 'subtotal': item['precio']*cant, 'total': item['precio']})
    except:
        temp[item['marca']] = [{'codigo': codProd, 'nombre': item['nombre'], 'cantidad': cant, 'serie': item['serie'], 'precioUni': item['precio'], 'subtotal': item['precio']*cant, 'total': item['precio']}]
    reporte_file.close()
    anadir(data)
    os.system('pause')

def ListDeProdVend():
    print('\nLista de Productos Vendidos por Marca\n')
    os.system('pause')

def ActuProd():
    print('Actualizar Producto\n')
    os.system('pause')

#ListDeProdVend()
