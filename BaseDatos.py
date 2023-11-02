import mysql.connector
from datetime import datetime
from os import system
class Database():
    def __init__(self):
        self.conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        database='empresa',
        password='inacap2023'
        )
        self.cursor=self.conexion.cursor()
        
    def cerrarBD(self):
        self.cursor.close()
        self.conexion.close()
    
    def insertar_venta(self):
        system('cls')
        numVenta=input('Ingrese el Núm. de Venta=')
        while numVenta.isspace() or len(numVenta)<1:
            system('cls')
            numVenta=input('Ingrese Núm. de la Venta= ')

        sql1='select numVenta from VentaDeViajes where numventa='+repr(numVenta)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone()==None:
                print('Núm. Venta= '+str(numVenta))
                codViaje=input('codigo de Viaje= ')
                while codViaje.isspace() or len(codViaje)<1:
                    system('cls')
                    print('Núm. Venta= '+str(numVenta))
                    codViaje=input('Error Cod. de Viaje= ')
                try: 
                    sql0='select codViaje from Viajes where codviaje='+repr(codViaje)
                    self.cursor.execute(sql0)
                    if self.cursor.fetchone()!=None:  #si el código no existe (None)
                        sql3='select * from viajes where codviaje='+repr(codViaje)
                        self.cursor.execute(sql3)
                        cupos=self.cursor.fetchone()
                        if cupos[-1]>0:
                            while True:
                                try:
                                    system('cls')
                                    print('Núm. Venta= '+str(numVenta))
                                    print('Cod. Viaje= '+str(codViaje))
                                    maxima_compra=cupos[-1]
                                    compra_pasaje=int(input('¿Cuantos cupos desea comprar? (máx.'+str(cupos[-1])+')= '))
                                    while compra_pasaje>maxima_compra:
                                        system('cls')
                                        print('Núm. Venta= '+str(numVenta))
                                        print('Cod. Viaje= '+str(codViaje))
                                        compra_pasaje=int(input('No puede comprar más cupos que el máximo (máx.'+str(cupos[-1])+')= '))
                                    while compra_pasaje<=0:
                                        system('cls')
                                        print('Núm. Venta= '+str(numVenta))
                                        print('Cod. Viaje= '+str(codViaje))
                                        compra_pasaje=int(input('No se permite una compra nula o negativa, vuelva a ingresar los cupos a comprar (máx.'+str(cupos[-1])+')= '))
                                    break
                                except ValueError:
                                    system('cls')
                                    print('Solo se permiten caracteres númericos, tampoco se permiten espacios vacios...\n')
                            sql4='update viajes set cupos=cupos-'+str(compra_pasaje)+' where codviaje='+repr(codViaje)
                            try:
                                self.cursor.execute(sql4)
                                self.conexion.commit()
                            except Exception as err:
                                self.conexion.rollback()
                                print(err)
                            while True:
                                try:
                                    
                                    print('Núm. Venta= '+str(numVenta))
                                    print('Cod. Viaje= '+str(codViaje))
                                    print('Cupos comprados= '+str(compra_pasaje))
                                    fechaVenta=input('Fecha de Venta (dd/mm/aaaa)= ')
                                    while fechaVenta.isspace() or len(fechaVenta)<6:
                                        
                                        print('Núm. Venta= '+str(numVenta))
                                        print('Cod. Viaje= '+str(codViaje))
                                        print('Cupos comprados= '+str(compra_pasaje))
                                        fechaVenta=input('Error de Ingreso en Fecha de venta (dd/mm/aaaa)= ')
                                    datetime.strptime(fechaVenta, '%d/%m/%Y')
                                    break
                                except ValueError:
                                    system('cls')
                                    print('La fecha que ha ingresado no pudo ser validada, por favor, ingresela correctamente')
                                    print('No olvide agregar "/" para separar los días, meses y año.')
                            while True:
                                try:
                                    system('cls')
                                    print('Núm. Venta= '+str(numVenta)+'\nCod. Viaje= '+str(codViaje))
                                    print('Cupos Comprados= '+str(compra_pasaje))
                                    print('Fecha Venta= '+str(fechaVenta))
                                    precioVenta=int(input('Monto de venta= '))
                                    while precioVenta<0:
                                        precioVenta=int(input('Error, no se permiten montos negativos, corrija= '))
                                    break
                                except ValueError:
                                    print('Solo se permiten caracteres númericos, tampoco se permiten espacios vacios...\n')
                            sql2="insert into ventaDeViajes values ("+repr(numVenta)+","+repr(codViaje)+\
                            ",str_to_date("+repr(fechaVenta)+",'%d/%m/%Y'),"+repr(precioVenta)+','+repr(compra_pasaje)+")"
                            try:
                                self.cursor.execute(sql2)
                                self.conexion.commit()
                                system('cls')
                                print('Venta ingresada Correctamente:\n')
                                print('Núm. Venta= '+str(numVenta)+'\nCod. Viaje= '+str(codViaje))
                                print('Cupos Comprados= '+str(compra_pasaje))
                                print('Fecha Venta= '+str(fechaVenta))
                                print('Precio Venta= '+str(precioVenta))
                            except Exception as err:
                                self.conexion.rollback()
                                print(err)
                        else:
                            print('No quedan cupos para este viaje.')
                            input('Presione enter para continuar...')
                            system('cls')
                            
                    else:
                        raise NameError
                except NameError:
                    print('El codigo de Viaje no existe')
                    input('Presione enter para continuar...')
                    system('cls')
            else:
                print('Ya existe ese número de venta')
                continuar=input('Para volver a ingresar la fecha presione (s)\nPara volver atrás presione (v)\n=> ').lower()
                while continuar!='s' and continuar!='v':
                    system('cls')
                continuar=input('Para volver a ingresar la fecha presione (s)\nPara volver atrás presione (v)\n=> ')

        except Exception as err:
            print(err)

    def mostrar_ventas(self):
            mysql='select * from ventaDeViajes'
            try:
                self.cursor.execute(mysql)
                if self.cursor.fetchone()!=None:
                    self.cursor.execute(mysql)
                    vent=self.cursor.fetchall()
                    print('Núm Venta\tCod. de Viaje\tFecha de Venta\tPrecio de Venta\tCupos Vendidos')
                    for resp in vent:
                        print(resp[0],'\t\t',resp[1],'\t\t',resp[2].strftime('%d/%m/%Y'),'\t',resp[3],'\t\t',resp[4])
                else:
                    system('cls')
                    print('No se a encontrado ninguna venta.')
            except Exception as err:
                print(err)

    def mostrar_venta_rango(self):
        while True:
            try:
                rangoMen=int(input('Ingrese el rango más bajo de precio= '))
                while rangoMen<0:
                    system('cls')
                    rangoMen=int(input('No se permite un número negativo, Ingrese el rango más bajo de precio= '))
                break
            except ValueError:
                system('cls')
                print('Debe ingresar un valor númerico, para el rango de valores.')
        while True:
            try:
                print('Rango Men.=',rangoMen)
                rangoMay=int(input('Ingrese el mayor rango de precio= '))
                while rangoMay<rangoMen:
                    system('cls')
                    print('Rango Men.=',rangoMen)
                    print('Rango May.=',rangoMay)
                    rangoMay=int(input('Error, el valor menor actualmente, supera al valor del rango mayor\nIngrese nuevamente el mayor rango de precio= '))
                break
            except ValueError:
                system('cls')
                print('Debe ingresar un valor númerico, para el rango de valores.')

        mysql='select * from ventaDeViajes where precioventa between '+str(rangoMen)+' and '+str(rangoMay)
        try:
            self.cursor.execute(mysql)
            if self.cursor.fetchone()!=None:
                self.cursor.execute(mysql)
                vent=self.cursor.fetchall()
                print('Núm Venta\tCod. de Viaje\tFecha de Venta\tPrecio de Venta\tCupos Vendidos')
                for resp in vent:
                    print(resp[0],'\t\t',resp[1],'\t\t',resp[2].strftime('%d/%m/%Y'),'\t',resp[3],'\t\t',resp[4])
            else:
                system('cls')
                print('No se han encontrado ventas dentro del rango especificado.')
        except Exception as err:
                print(err)
        input('Presione enter para continuar...')
    
    def modificar_venta(self):
        numVenta=input('Número de venta= ')
        while numVenta.isspace() or len(numVenta)<1:
            system('cls')
            numVenta=input('Error de ingreso, Ingrese el núm de venta a buscar= ')
        sql1='select * from ventadeviajes where numventa='+repr(numVenta)
        try:
            self.cursor.execute(sql1)
            rep=self.cursor.fetchone()
            if rep!=None:
                print('{:10}{:10}{:11}{:13}{:14}'.format('Núm. venta','\tCod. viaje','\tFecha venta','\tPrecio venta.','\tCupos Vendidos'))
                print('{:2}{:2}{:12}{:<6}{:<2}'.format(rep[0],rep[1],rep[2].strftime('%d/%m/%Y'),rep[3],rep[4]))
        
                elige=input('\nQué desea modificar? (Cod. viaje(c), Fecha de venta.(f), Precio venta.(p), Cupos vendidos(k))=').lower()
                system('cls')
                if elige=='f':
                    continuar='s'
                    while continuar=='s':
                        try:
                            nuevo=input('Fecha de Venta (dd/mm/aaaa)= ')
                            while nuevo.isspace() or len(nuevo)<6:
                                nuevo=input('Error de Ingreso en Fecha de venta (dd/mm/aaaa)= ')
                            datetime.strptime(nuevo, '%d/%m/%Y')
                            break
                        except ValueError:
                            print('La fecha que ha ingresado no pudo ser validada, por favor, ingresela correctamente\n')
                            print('No olvide agregar "/" para separar los días, meses y año.\n')
                            continuar=input('Para volver a ingresar la fecha presione (s)\nPara volver atrás presione (v)\n=> ').lower()
                            while continuar!='s' and continuar!='v':
                                system('cls')
                                continuar=input('Para volver a ingresar la fecha presione (s)\nPara volver atrás presione (v)\n=> ')
                    sql2="update ventadeviajes set fechaventa=str_to_date("+repr(nuevo)+",'%d/%m/%Y') where numVenta="+repr(numVenta)
                else:
                    while True:
                        if elige=='c':
                            campo='codigoviaje'
                            nuevo=input('Ingrese nuevo codigo asociado= ')
                            while nuevo.isspace() or len(nuevo)<1:
                                nuevo=input('Error de Ingreso, Ingreso nuevo Cod. de viaje= ')
                            #Voy a confirmar que el nuevo codigo de viaje tenga los cupos suficientes, de otro modo,
                            #le recomendare al usuario modificar los cupos primero y luego modificar el codigo...
                            sql3='select * from viajes where codviaje='+repr(nuevo)
                            self.cursor.execute(sql3)
                            cupos=self.cursor.fetchone()
                            if cupos!=None:
                                if cupos[-1]<rep[-1]:
                                    print('Los cupos asociados a la venta, exceden los disponibles en el cod. de viaje que desea asociar \
                                            los cupos actuales son ',cupos[-1],')')
                                    input('Se recomienda modificar la cant. de cupos antes de cambiar el cod. de viaje...\nPresione Enter para continuar...')
                                else:
                                    #Ahora devolvere los cupos comprados a la tabla original
                                    sql4='update viajes set cupos=cupos+'+str(rep[4])+' where codviaje='+repr(rep[1])
                                    try:
                                        self.cursor.execute(sql4)
                                        self.conexion.commit()
                                    except Exception as err:
                                        self.conexion.rollback()
                                        print(err)
                                    #Y le resto los cupos asociados al nuevo codigo de viaje
                                    sql5='update viajes set cupos=cupos-'+str(rep[4])+' where codviaje='+repr(nuevo)
                                    try:
                                        self.cursor.execute(sql5)
                                        self.conexion.commit()
                                        break
                                    except Exception as err:
                                        self.conexion.rollback()
                                        print(err)
                            else:
                                print('No existe este codigo.')
                                input('Presione enter para continuar...')
                                system('cls')
                                
                        elif elige=='p':
                            campo='precioventa'
                            while True:
                                try:
                                    nuevo=int(input('Ingrese nuevo precio= '))
                                    while nuevo<0:
                                        nuevo=int(input('Error, no se permite un precio inferior a 0, Ingrese nuevo precio= '))
                                    break
                                except ValueError:
                                    print('Solo se aceptan caracteres númericos, por favor corrija.')
                            break
                        elif elige=='k':
                            campo='cuposvendidos'
                            while True:
                                try:
                                    nuevo=int(input('Ingrese la nueva cantidad de cupos en la venta= '))
                                    while nuevo<0:
                                        system('cls')
                                        nuevo=int(input('Error, no se permite una cant. inferior a 0, Ingrese nuevamente los cupos= '))
                                    break
                                except ValueError:
                                    print('Solo se aceptan caracteres númericos, por favor corrija.')

                            sql6='select * from viajes where codviaje='+repr(rep[1])
                            self.cursor.execute(sql6)
                            tupla=self.cursor.fetchone()
                            cupos=tupla[-1]
                            diferencia=rep[-1]-nuevo
                            if diferencia>=0:
                                sql7='update viajes set cupos=cupos+'+str(diferencia)+' where codviaje='+repr(rep[1])
                                try:
                                    self.cursor.execute(sql7)
                                    self.conexion.commit()
                                    break
                                except Exception as err:
                                    self.conexion.rollback()
                                    print(err)
                            else:
                                if (cupos+diferencia)<0:
                                    print('Esta cantidad de cupos causaria una cant. negativa en el viaje')
                                    print('(cupos disp.= '+str(cupos)+')')
                                else:
                                    sql7='update viajes set cupos=cupos'+str(diferencia)+' where codviaje='+repr(rep[1])
                                    try:
                                        self.cursor.execute(sql7)
                                        self.conexion.commit()
                                        break
                                    except Exception as err:
                                        self.conexion.rollback()
                                        print(err)
                            break           

                            #Falta revisar
                        else:
                            print('Error de opción')
                            
                    sql2='update ventadeviajes set '+campo+'='+repr(nuevo)+' where numventa='+repr(numVenta)
                try:
                        self.cursor.execute(sql2)
                        self.conexion.commit()
                except Exception as err:
                        self.conexion.rollback()
                        print(err)
            else:
                print('No existe ese código')
        except Exception as err:
            print(err)

    def eliminar_venta(self):
        numVen=input('Número de venta a eliminar= ')
        while numVen.isspace() or len(numVen)<1:
            system('cls')
            numVen=input('Error de ingreso, Núm. de Venta= ')
        sql1='select * from Ventadeviajes where numVenta='+repr(numVen)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone()!=None:
                sql2 = 'delete from ventadeviajes where numVenta='+repr(numVen)
                try:
                    self.cursor.execute(sql2)
                    self.conexion.commit()
                    input('Venta eliminada exitosamente, presione enter para continuar...')
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                print('No existe ese número de venta')
        except Exception as err: 
                print(err)

    def insertar_viaje(self):
        #listo
        system('cls')
        codViaje=input('Código del viaje= ')
        while codViaje.isspace() or len(codViaje)<1 or len(codViaje)>2:
            system('cls')
            codViaje=input('Error de ingreso, solo se aceptan como máx. 2 caracteres\nCod. de viaje= ')
        sql1='select codviaje from viajes where codviaje='+repr(codViaje)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone()==None:
                while True:
                    try:
                        destino=str(input('Destino= ')).capitalize()
                        while destino.isspace() or len(destino)<1 or destino.isdigit():
                            system('cls')
                            print('Código del viaje= '+codViaje)
                            destino=input('Error, ingrese el nombre del Destino= ').capitalize()
                        break
                    except ValueError:
                        print('No se permite un ingreso de solo números')
                while True:
                    try:
                        cupos=int(input('Cupos del viaje= '))
                        while cupos<=0:
                            system('cls')
                            print('Código del viaje= '+codViaje)
                            print('Destino= '+destino)
                            cupos=int(input('No se permiten digitos nulos o negativos, por favor corrija\nCupos del viaje= '))
                        break
                    except ValueError:
                        system('cls')
                        print('Código del viaje= '+codViaje)
                        print('Destino= '+destino)
                        print('Solo se aceptan caracteres Númericos, por favor corrija.')

                sql2="insert into viajes values ("+repr(codViaje)+","+repr(destino)+\
                ","+repr(cupos)+")"
                try:
                    self.cursor.execute(sql2)
                    self.conexion.commit()
                    system('cls')
                    print('Ingresado Correctamente:\n\tCódigo del viaje= '+codViaje+'\
                          \n\tDestino= '+destino+'\n\tCupos= '+str(cupos))
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                system('cls')
                print('Ya existe ese código')
        except Exception as err:
            print(err)

    def mostrar_viaje_cod(self):
        #listo
        system('cls')
        codViaje=input('Ingrese el codigo del viaje a buscar= ')
        while codViaje.isspace() or len(codViaje)<1:
            system('cls')
            codViaje=input('Error de ingreso, Ingrese el codigo del viaje a buscar= ')
        sql3='select * from viajes where codviaje='+repr(codViaje)
        try:
            self.cursor.execute(sql3)
            viaje=self.cursor.fetchone()
            if viaje!=None:
                print('Código de Viaje\tDestino\tCupos')
                print('\t',viaje[0],'\t',viaje[1],'\t',viaje[2])
            else:
                system('cls')
                print('No existen coincidencias')
        except Exception as err:
            print(err)

    def mostrar_viaje_letra(self):
            #listo
            system('cls')
            letra=input('Ingrese una letra para iniciar la busqueda= ').upper()
            while letra.isspace() or len(letra)!=1 or letra.isdigit():
                system('cls')
                letra=input('Ingrese solo "una" letra del abecedario para realizar la busqueda= ').upper()
            sql3="select * from viajes where destino like '"+letra+"%'"
            try:
                system('cls')
                self.cursor.execute(sql3)
                if  self.cursor.fetchone()!=None:
                    self.cursor.execute(sql3)
                    viaje=self.cursor.fetchall()
                    print('Código de Viaje\t\tDestino\tCupos')
                    for resp in viaje:
                        print(resp[0],'\t\t\t',resp[1],'\t',resp[2])
                else:
                    system('cls')
                    print('No existen coincidencias')
            except Exception as err:
                print(err)