from func import *

pIni()
print(f'\n{fecha()}\n')
print('Bienvenido al sistema de inventario\nInicie sesión')
while True:
    user = input('Ingrese su usuario: ')
    passw = getpass.getpass(prompt='Contraseña: ') 
    if login(user, passw):
        break
    else:
        os.system('cls')
        pIni()
        print(f'\n{fecha()}\n')
        print('\nCredenciales incorrectas')
        continue

selecc = 'n'
while selecc != 's':
    while True:
        try:
            os.system('cls')
            print(f'{fecha()}\n')
            opciones()
            selecc = int(input('Seleccione su opción: '))
            while selecc > 5 or selecc <1:
                print('Error')
                selecc = int(input('Seleccione su opción: '))
        except:
            print('Error')
            os.system('pause')
            continue
        break
    if selecc == 1:
        os.system('cls')
        RegDeCel()
    elif selecc == 2:
        os.system('cls')
        VentDeCel()
    elif selecc == 3:
        os.system('cls')
        ListDeProdVend()
    elif selecc == 4:
        os.system('cls')
        ActuProd()
    else:
        while True:
            try:
                selecc = input('\nEstá seguro que desea salir? (S/N): ').lower()
                while selecc != 's' and selecc != 'n':
                    print('Haga una selección válida')
                    selecc = input('Está seguro que desea salir? (S/N): ').lower()
            except:
                print('Error')
                continue
            break
