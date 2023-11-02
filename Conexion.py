from BaseDatos import *
from os import system

db=Database()
while True:
    elige=input('\nElija una opción:\n\
                \tMantenedor de Viajes (A)\n\
                \tMantenedor de Venta de Viajes (B)\n\
                \tFin(f)\n\
                \t=> ').lower()
    system('cls')
    if elige=='a':
        while True:
            elige=input('\nElija una opción:\n\
                    \tInsertar Viaje (i)\n\
                    \tMostrar Viaje según codigo (m)\n\
                    \tMostrar Viaje según letra (l)\n\
                    \tVolver (v)\n\
                    \t=> ').lower()
            if elige=='i':
                db.insertar_viaje()
            elif elige=='m':
                db.mostrar_viaje_cod()
            elif elige=='l':
                db.mostrar_viaje_letra()
            elif elige=='v':
                system('cls')
                print('Volver al menu principal')
                break
            else:
                system('cls')
                print('Error de opción')
                

    elif elige=='b':
        while True:
            elige=input('\nElija una opción:\n\
                    \tInsertar Venta (i)\n\
                    \tMostrar todas las ventas (t)\n\
                    \tMostrar ventas según rango de precio (r)\n\
                    \tModificar una venta (m)\n\
                    \tEliminar venta (e)\n\
                    \tVolver (v)\n\
                    \t=> ').lower()
            if elige=='i':
                db.insertar_venta()
            elif elige=='t':
                db.mostrar_ventas()
            elif elige=='r':
                db.mostrar_venta_rango()
            elif elige=='m':
                db.modificar_venta()
            elif elige=='e':
                db.eliminar_venta()
            elif elige=='v':
                system('cls')
                print('Volver al menu principal')
                break
            else:
                system('cls')
                print('Error de opción')

    elif elige=='f':
        print('Fin')
        db.cerrarBD()
        break
        
    else:
        system('cls')
        print('Error de opción')
        