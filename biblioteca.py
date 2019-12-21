import os
import shutil
from Libros import Libros

CARPETA_DISPONIBLE = 'Biblioteca/disponibles/'
CARPETA_OCUPADOS = 'Biblioteca/prestados/'
EXTENSION = '.txt'

def app():

    crear_directorios();

    mostrar_menu();

    #while
    preguntar = True
    while preguntar:
        opcion = input('¿Que Desea Hacer? \r\n')
        opcion = int(opcion)

        #ejecutar opciones
        if opcion == 1:
            registrar_libro()
            preguntar = False
        elif opcion == 2:
            editar_libro()
            preguntar = False
        elif opcion == 3:
            eliminar_libro()
            preguntar = False
        elif opcion == 4:
            ver_libros_disponibles()
            preguntar = False
        elif opcion == 5:
            ver_libros_prestados()
            preguntar = False
        elif opcion == 6:
            prestar_libro();
            preguntar = False
        else:
            print('No es una opción Válida')

def prestar_libro():
    codigo = input('Ingrese el Codigo del Libro')

    shutil.move(CARPETA_DISPONIBLE + codigo + EXTENSION, CARPETA_OCUPADOS + codigo + EXTENSION)

    print('El Libro ahora se encuentra Reservado')

def ver_libros_prestados():
    print('Listado de Libros en Prestamo')

    no_disponibles = os.listdir(CARPETA_OCUPADOS)

    registros = [i for i in no_disponibles if i.endswith(EXTENSION)]

    for registro in registros:
        with open(CARPETA_OCUPADOS + registro) as libro:
            for linea in libro:
                print(linea.rstrip())
            print('\r\n')

def ver_libros_disponibles():
    print('Listar los Libros Disponibles en Tienda')
    disponibles = os.listdir(CARPETA_DISPONIBLE)
    registros = [i for i in disponibles if i.endswith(EXTENSION)]

    for registro in registros:
        with open(CARPETA_DISPONIBLE + registro) as libro:
            for linea in libro:
                print(linea.rstrip())
            print('\r\n')

def eliminar_libro():
    codigo = input('Ingrese el Codigo del libro a Eliminar \r\n')

    try:
        os.remove(CARPETA_DISPONIBLE + codigo + EXTENSION)
        print('\r\n Eliminado Correctamente')
    except IOError:
        print('\r\n Asegurese que el codigo Exista o Se encuentra en la Biblioteca')

def editar_libro():
    print('Escribe el Codigo del Libro a editar \r\n')
    codigo_buscar = input('Codigo del Libro a Buscar:  \r\n')

    existe = existe_libro(codigo_buscar)
   
    if existe:
        with open(CARPETA_DISPONIBLE + codigo_buscar + EXTENSION, 'w') as archivo:
        
        #resto de los campos
            codigo_nuevo = input('Ingrese el Nuevo Codigo del Libro \r\n')
            nombre_libro = input('Ingrese el Nuevo Nombre del Libro \r\n')
            autor_libro = input('Ingrese el Nuevo Nombre del Autor del Libro \r\n')
            paginas_libro = input('Ingrese el Nuevo numero de paginas del libro \r\n')
        
        #instancia
            Libro = Libros(codigo_nuevo, nombre_libro, autor_libro, paginas_libro)
        
        #Escribir en el archivo
            archivo.write('Codigo: \r\n'+ Libro.codigo+ '\r\n')
            archivo.write('Nombre: \r\n'+ Libro.nombre+ '\r\n')
            archivo.write('Paginas: \r\n'+ Libro.paginas+ '\r\n')
            archivo.write('Autor: \r\n'+ Libro.autor)

        #Mensaje de exito
            os.rename(CARPETA_DISPONIBLE + codigo_buscar + EXTENSION, CARPETA_DISPONIBLE + codigo_nuevo + EXTENSION)
        
        print('\r\n Actualizado Correctamente \r\n') 
    else:
        print('\r\n El Codigo del Libro no se encuentra')

def registrar_libro():
    print('Escriba los siguientes datos para registrar el Libro')
    codigo = input('Ingrese Codigo de Libro \r\n')

    existe = existe_libro(codigo)
    
    if not existe:
        with open(CARPETA_DISPONIBLE + codigo + EXTENSION, 'w') as archivo:
            nombre_libro = input('Ingrese el Nombre del Libro \r\n')
            autor_libro = input('Ingrese el Nombre del Autor del Libro \r\n')
            paginas_libro = input('Ingrese el numero de paginas del libro \r\n')

            Libro = Libros(codigo, nombre_libro, paginas_libro, autor_libro)

            #Escribir en el archivo
            archivo.write('Codigo: '+ Libro.codigo)
            archivo.write('\r\nNombre: '+ Libro.nombre)
            archivo.write('\r\nPaginas: '+ Libro.paginas)
            archivo.write('\r\nAutor: '+ Libro.autor)

            #Mensaje de exito
            print('\r\n Contacto Creado Correctamente \r\n')    

def existe_libro(codigo):
    return os.path.isfile(CARPETA_DISPONIBLE + codigo + EXTENSION) or os.path.isfile(CARPETA_OCUPADOS + codigo + EXTENSION)

def mostrar_menu():
    print('Administración de Biblioteca con Préstamo de Libros')
    print('1) Registrar Libro')
    print('2) Editar Libro')
    print('3) Eliminar Libro')
    print('4) Ver Libros Disponibles')
    print('5) Ver Libros Prestados')
    print('6) Prestar Libro')


def crear_directorios():
    #Validar si el directorio Disponible Existe
    #Parametro False no Permite crearla si no existe
    #Segundo Valor indica los permisos de la carpeta
    #os.makedirs(CARPETA_DISPONIBLE, 777, False)
    if not os.path.exists(CARPETA_DISPONIBLE):
        os.makedirs(CARPETA_DISPONIBLE)
    if not os.path.exists(CARPETA_OCUPADOS):
        os.makedirs(CARPETA_OCUPADOS)
    


app();