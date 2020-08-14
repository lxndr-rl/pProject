'''
El dueño de una empresa desea planificar las decisiones financieras que deben tomar sus clientes. La manera de planificadas depende de lo siguiente:
Si actualmente su capital se encuentra con saldo negativo, pedirá un préstamo bancario para que su nuevo saldo sea de $10000. Si su capital tiene actualmente un saldo positivo pedirá 
un préstamo bancario para tener un nuevo saldo de $20000, pero si su capital tiene actualmente un saldo superior a los $20000 no pedirá ningún préstamo.
Posteriormente repartirá su presupuesto de la siguiente manera $5000 para equipo de cómputo, $2000 para mobiliario y del resto la mitad será para la compra de insumos y la otra para
 otorgar incentivos al personal.
Desplegar que cantidades se destinaran para la compra de insumos e incentivos al personal y, en caso de que fuera necesario, a cuanto ascendería la cantidad que se pediría al banco.
'''
def prestamo(capital):
    if capital<0:
        nuevo = 10000
        prest = 10000-capital
    elif capital<=20000:
        nuevo = 20000
        prest = 20000-capital
    else:
        nuevo = capital
        prest = 0
    return prest, nuevo
def division(tot):
    computo = 5000
    mobil = 2000
    new = tot-computo-mobil
    insum = new/2
    incent = insum
    return computo, mobil, insum, incent
respt = 's'
while respt != 'n':
    while True:
        try:
            capit = float(input('Ingrese su capital: '))
        except:
            print('Error')
            continue
        break
    prestam, nuevo = prestamo(capit)
    computo, mobil, insum, incent = division(nuevo)
    print(f'Se pidió: ${prestam}\n${computo} destinados para equipo de cómputo\n${mobil} destinados para mobiliario\n${insum} para la compra de insumos\n${incent} serán para incentivos de personal')
    while True:
        try:
            respt = input('Desea volver a hacer ingreso? (S/N): ').lower()
            while respt != 's' and respt != 'n':
                print('Ingreso inválido')
                respt = input('Desea volver a hacer ingreso? (S/N): ').lower()
        except:
            print('Error')
            continue
        break
