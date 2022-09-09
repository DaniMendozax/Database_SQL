from cities import Cities

paises = Cities()

menu = ''' ************************
*         MENU paises    *
****************************
*                          *
* 1) Insertar paises    *
* 2) Eliminar paises    *
* 3) Modificar paises   *
* 4) Imprimir la tabla    *
* 5) Salir                *
*                         *
***************************'''

def main():
    opcion = '0'
    while opcion != '5':
        print(menu)
        opcion = input("¿Que opcion deseas realizar?: ")

        if opcion == '1':
            print("*****  Insertar Paises   *****")
            iso3 = input('Introduce la clave ISO3 del nuevo País: ')
            countryName = input('Introduce el nombre del nuevo País: ')
            capital = input('Introduce la capital del nuevo País: ')
            currencyCode = input('Introduce el codigo de la moneda del nuevo País: ')
            r = paises.inserta_paises(iso3, countryName, capital, currencyCode)         
            if(r==0):
                print('->No se pudo insertar el pais :(')
            else:
                print('-> El pais se inserto correctamente :)')

        elif opcion == '2':
            print('*****  Eliminar Paises  *****')
            id = int(input("Ingresa id del pais para eliminar: "))
            r = paises.elimina_paises(id)
            if(r==0):
                print('->Ese pais no existe')
            else:
                print('-> Pais eliminado :)')

        elif opcion == '3':
            print('*****  Modificar Paises  *****')
            id = int(input("Ingresa id del pais para modificar: "))
            r = paises.buscar_pais(id)
            if r == None:
                print('->Ese pais no existe')
            else:
                print("*** Pais que se va a modificar: ***")
                print(r)
                iso3 = input('Introduce la nueva clave ISO3 del nuevo País: ')
                countryName = input('Introduce el nuevo nombre del nuevo País: ')
                capital = input('Introduce la  nueva capital del nuevo País: ')
                currencyCode = input('Introduce el nuevo codigo de la moneda del nuevo País: ')
                paises.Modificaa_países(id, iso3, countryName, capital, currencyCode)
                print('****  Pais actualizado  ****')
        elif opcion == '4':
            print('*****  Imprimir Paises  *****')
            print(paises)
        elif opcion == '5':
            print('*****  Saliendo del sistema  *****')
        else:
            print(' -> Opcion no valida')


if __name__ == "__main__":
    main()