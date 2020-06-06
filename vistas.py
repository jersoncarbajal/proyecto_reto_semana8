from controladores.controlador_libro import ControladorLibro
from controladores.controlador_tipolibro import ControladorTipoLibro
from controladores.controlador_lector import ControladorLector
from controladores.controlador_editorial import ControladorEditorial
from controladores.controlador_prestamo import ControladorPrestamo
from controladores.controlador_prestamo_detalle import ControladorPrestamoDetalle

class VistaTipoLibro:
    
    @staticmethod
    def menu():
        continuar = True
        while continuar:
            
            ControladorTipoLibro.inicializar()
            print("\t\t\t***Bienvenid@ a la Seccion de la Libro! ***")
            print("\t\t\tElija 1 para registrar un Tipo de Libro")
            print("\t\t\tElija 2 para actualizar un Tipo de Libro")
            print("\t\t\tElija 3 para eliminar un Tipo de Libro")
            print("\t\t\tElija 4 para listar los Tipo de Libro")
            print("\t\t\tElija 5 para regresar al Menu Pricipal")

            opcion = input("Elija una opcion : ")
            if opcion.isdigit():

                if opcion == "1":
                    VistaTipoLibro.ingreso_datos()
                elif opcion == "2":
                    VistaTipoLibro.actualizar_datos()
                elif opcion == "3":
                    VistaTipoLibro.eliminar_datos()
                elif opcion == "4":
                    VistaTipoLibro.listar_datos()
                elif opcion == "5":
                    print("\n")
                    continuar = False
                else:
                    print("Debe Ingresar un numero de la Lista de Opciones\n")
                    continuar = True
            else:
                print("Ingrese un numero\n")
                continuar = True
 
    @staticmethod
    def ingreso_datos():      
        nombre = input("\t\t\tIngrese el Nombre del Tipo Libro: ")
        desc = input("\t\t\tIngrese la Descripcion del Tipo Libro: ")
        ControladorTipoLibro.agregar_tipo_libro(nombre, desc)
       
    @staticmethod
    def actualizar_datos():       
        nombre_consulta = input("\t\t\tIngrese el Nombre del Tipo Libro a actualizar: ")
        id_tipo_libro = ControladorTipoLibro.verificar_tipo_libro(nombre_consulta)       

        if id_tipo_libro:
            nuevo_nombre = input("\t\t\tIngrese el Nuevo Nombre del Tipo Libro a actualizar: ")
            nueva_descripcion = input("\t\t\tIngrese la Nueva Descripcion del Tipo Libro a actualizar: ")
            ControladorTipoLibro.modificar_tipo_libro(nuevo_nombre, nueva_descripcion, id_tipo_libro)
        else:
            print("No se encontró Tipo Libro a actualizar\n")

    @staticmethod
    def eliminar_datos(): 
        
        
        nombre_consulta = input("\t\t\tIngrese el Nombre de la Tipo Libro a Eliminar: ")
        
        id_tipo_libro = ControladorTipoLibro.verificar_tipo_libro(nombre_consulta)           
        if id_tipo_libro:
            ControladorTipoLibro.borrar_tipo_libro(id_tipo_libro)
        else:
            print("No se encontró la Tipo Libro a eliminar\n")
                
    @staticmethod
    def listar_datos():
        
        filas = ControladorTipoLibro.listar_tipo_libro()

        for i in filas:
            print(f"""
            Código: {i[0]}
            Nombre: {i[1]}
            Descripcion: {i[2]}
            """)


###########################VistaAplicacion################################
class VistaAplicacion:

    @staticmethod
    def iniciar():
      
        VistaAplicacion.bienvenida_menu()
    
    @staticmethod
    def bienvenida():
        pass

    @staticmethod
    def bienvenida_menu():
        continuar = True
        while continuar:
            print("\n")
            print("\n\t\t\t********Bienvenid@ a nuestro Sistema de Biblioteca********")
            print("")
            print("\t\t\tElija 1 para ir a la Seccion de Lector")
            print("\t\t\tElija 2 para ir a la Seccion de Editorial")
            print("\t\t\tElija 3 para ir a la Seccion de Tipo de Libro")
            print("\t\t\tElija 4 para ir a la Seccion de Libro")
            print("\t\t\tElija 5 para ir a la Seccion de Prestamo")
            print("\t\t\tElija 6 para ir a la Seccion de Entrega de Libro")

            print("\t\t\tElija 7 para Salir")
            
            opcion = input("Elija una opcion: ")
            if opcion == "1":
                VistaLector.menu()
            elif opcion == "2":
                VistaEditorial.menu()
            elif opcion == "3":
                VistaTipoLibro.menu()
            elif opcion == "4":
                VistaLibro.menu() 
            elif opcion == "5":
                VistaPrestamo.menu() 
            elif opcion == "6":
                VistaEntrega.menu()           
            else:
                continuar = False


###########################VistaLector################################

class VistaLector:
    @staticmethod
    def menu():
        continuar = True
        

        while continuar:
            
            ControladorLector.inicializar()
            print("\t\t\t***Bienvenid@ a la Seccion de la Lector! ***")
            print("\t\t\tElija 1 para registrar Lector")
            print("\t\t\tElija 2 para actualizar Lector")
            print("\t\t\tElija 3 para eliminar Lector")
            print("\t\t\tElija 4 para listar Lector")
            print("\t\t\tElija 5 para regresar al Menu Pricipal")

            opcion = input("Elija una opcion : ")
            if opcion.isdigit():

                if opcion == "1":
                    VistaLector.ingreso_datos()
                elif opcion == "2":
                    VistaLector.actualizar_datos()
                elif opcion == "3":
                    VistaLector.eliminar_datos()
                elif opcion == "4":
                    VistaLector.listar_datos()
                elif opcion == "5":
                    print("\n")
                    continuar = False
                else:
                    print("Debe Ingresar un numero de la Lista de Opciones\n")
                    continuar = True
            else:
                print("Ingrese un numero\n")
                continuar = True
 
    @staticmethod
    def ingreso_datos():      
        num_tarjeta = input("\t\t\tIngrese el Numero de Tarjeta del Lector: ")
        nombre = input("\t\t\tIngrese Nombre del Lector: ")
        direccion = input("\t\t\tIngrese Direccion del Lector: ")
        dni = input("\t\t\tIngrese la D.N.I. del Lector: ")
        correo = input("\t\t\tIngrese el Correo del Lector: ")
        telefono = input("\t\t\tIngrese la Telefono del Lector: ")



        ControladorLector.agregar_lector(num_tarjeta, nombre, direccion, dni, correo, telefono)
       
    @staticmethod
    def actualizar_datos():       
        num_tarjeta = input("\t\t\tIngrese el Numero de Tarjeta del Lector: ")
        id_lector = ControladorLector.verificar_lector(num_tarjeta)       

        if id_lector:
            nuevo_nombre = input("\t\t\tIngrese Nombre del Lector a actualizar: ")
            nueva_direccion = input("\t\t\tIngrese Direccion del Lector: ")
            nuevo_dni = input("\t\t\tIngrese D.N.I del Lector: ")
            nuevo_correo = input("\t\t\tIngrese el Correo del Lector: ")
            nuevo_telefono = input("\t\t\tIngrese la Telefono del Lector: ")

            ControladorLector.modificar_lector(num_tarjeta, nuevo_nombre, nueva_direccion, nuevo_dni,
            nuevo_correo, nuevo_telefono, id_lector)
        else:
            print("No se encontró Lector a actualizar\n")

    @staticmethod
    def eliminar_datos(): 
        
        
        nombre_consulta = input("\t\t\tIngrese el el Numero de Tarjeta del Lector a Eliminar: ")
        
        id_tipo_libro = ControladorLector.verificar_lector(nombre_consulta)           
        if id_tipo_libro:
            ControladorLector.borrar_lector(id_tipo_libro)
        else:
            print("No se encontró la Lector a eliminar\n")
                
    @staticmethod
    def listar_datos():
        
        filas = ControladorLector.listar_lector()

        for i in filas:
            print(f"""
                Numero Tarjeta: {i[1]}
                Nombre: {i[2]}
                Direccion: {i[3]}
                DNI: {i[4]}
                Correo: {i[5]}
                Telefono: {i[6]}
            """)

#################################VistaEditorial###################################

class VistaEditorial:
    @staticmethod
    def menu():
        continuar = True
        while continuar:
            
            ControladorEditorial.inicializar()
            print("\t\t\t***Bienvenid@ a la Seccion Editorial! ***")
            print("\t\t\tElija 1 para Registrar Editorial")
            print("\t\t\tElija 2 para Actualizar Editorial")
            print("\t\t\tElija 3 para Eliminar Editorial")
            print("\t\t\tElija 4 para Listar Editorial")
            print("\t\t\tElija 5 para regresar al Menu Pricipal")

            opcion = input("Elija una opcion : ")
            if opcion.isdigit():

                if opcion == "1":
                    VistaEditorial.ingreso_datos()
                elif opcion == "2":
                    VistaEditorial.actualizar_datos()
                elif opcion == "3":
                    VistaEditorial.eliminar_datos()
                elif opcion == "4":
                    VistaEditorial.listar_datos()
                elif opcion == "5":
                    print("\n")
                    continuar = False
                else:
                    print("Debe Ingresar un numero de la Lista de Opciones\n")
                    continuar = True
            else:
                print("Ingrese un numero\n")
                continuar = True
 
    @staticmethod
    def ingreso_datos():      
       
        nombre = input("\t\t\tIngrese Nombre del Editorial: ")
        pais = input("\t\t\tIngrese el Pais del Editorial: ")
        telefono = input("\t\t\tIngrese la Telefono del Editorial: ")

        ControladorEditorial.agregar_editorial(nombre, pais, telefono)
       
    @staticmethod
    def actualizar_datos():       
        nombre_ed = input("\t\t\tIngrese el Nombre del Editorial: ")
        id_ed = ControladorEditorial.verificar_editorial(nombre_ed)       

        if id_ed:
            nuevo_nombre = input("\t\t\tIngrese Nombre del Editorial a actualizar: ")
            nuevo_pais = input("\t\t\tIngrese el Pais del Editorial: ")
            nuevo_telefono = input("\t\t\tIngrese la Telefono del Editorial: ")

            ControladorEditorial.modificar_editorial(nuevo_nombre, nuevo_pais,
            nuevo_telefono, id_ed)
        else:
            print("No se encontró Editorial a actualizar\n")

    @staticmethod
    def eliminar_datos(): 
        
        
        nombre_consulta = input("\t\t\tIngrese el Nombre del Editorial a Eliminar: ")
        
        id_ed = ControladorEditorial.verificar_editorial(nombre_consulta)           
        if id_ed:
            ControladorEditorial.borrar_editorial(id_ed)
        else:
            print("No se encontró la Editorial a Eliminar\n")
                
    @staticmethod
    def listar_datos():
        
        filas = ControladorEditorial.listar_editorial()

        for i in filas:
            print(f"""
                \tCódigo: {i[0]}
                \tNombre Editorial: {i[1]}
                \tPais: {i[2]}
                \tTelefono: {i[3]}
            """)

       

###########################VistaLibro################################

class VistaLibro:
    @staticmethod
    def menu():
        continuar = True
        while continuar:
            
            ControladorLibro.inicializar()
            print("\t\t\t***Bienvenid@ a la Seccion de Libros! ***")
            print("\t\t\tElija 1 para Registrar Libro")
            print("\t\t\tElija 2 para Actualizar Libro")
            print("\t\t\tElija 3 para Eliminar Libro")
            print("\t\t\tElija 4 para Listar Libro(s)")
            print("\t\t\tElija 5 para regresar al Menu Pricipal")

            opcion = input("Elija una opcion : ")
            if opcion.isdigit():

                if opcion == "1":
                    VistaLibro.ingreso_datos()
                elif opcion == "2":
                    VistaLibro.actualizar_datos()
                elif opcion == "3":
                    VistaLibro.eliminar_datos()
                elif opcion == "4":
                    VistaLibro.listar_datos()
                elif opcion == "5":
                    print("\n")
                    continuar = False
                else:
                    print("Debe Ingresar un numero de la Lista de Opciones\n")
                    continuar = True
            else:
                print("Ingrese un numero\n")
                continuar = True
 
    @staticmethod
    def ingreso_datos():      
       
        isbn = input("\t\t\tIngrese ISBN del Libro: ")
        titulo = input("\t\t\tIngrese Título del Libro: ")
        autor = input("\t\t\tIngrese Autor del Libro: ")
        cod_ed = input("\t\t\tIngrese el Código de Editorial: ")  
        num_paginas = input("\t\t\tIngrese Número de Páginas del Libro: ")
        id_tipo = input("\t\t\tIngrese Código Tipo del Libro: ")
        fecha_ingreso = input("\t\t\tIngrese Fecha de Ingreso del Libro: ")
        fecha_publicacion = input("\t\t\tIngrese la Fecha de Publicacion del Libro: ")

        ControladorLibro.agregar_libro(isbn, titulo, autor, cod_ed, num_paginas, id_tipo, fecha_ingreso, fecha_publicacion)
       
    @staticmethod
    def actualizar_datos():       
        cod_isbn = input("\t\t\tIngrese el Código de ISBN del Libro: ")
        id_libro = ControladorLibro.verificar_libro(cod_isbn)       

        if id_libro:
            nuevo_titulo = input("\t\t\tIngrese Título del Libro: ")
            nuevo_autor = input("\t\t\tIngrese Autor del Libro: ")
            nuevo_cod_ed = input("\t\t\tIngrese el Código de Editorial: ")  
            nuevo_num_paginas = input("\t\t\tIngrese Número de Páginas del Libro: ")
            nuevo_id_tipo = input("\t\t\tIngrese Código Tipo del Libro: ")
            nuevo_fecha_ingreso = input("\t\t\tIngrese Fecha de Ingreso del Libro: ")
            nuevo_fecha_publicacion = input("\t\t\tIngrese Fecha de Publicacion del Libro: ")


            ControladorLibro.modificar_libro(cod_isbn, nuevo_titulo, nuevo_autor, nuevo_cod_ed, nuevo_num_paginas,
            nuevo_id_tipo, nuevo_fecha_ingreso, nuevo_fecha_publicacion, id_libro)
        else:
            print("No se encontró Libro a actualizar\n")

    @staticmethod
    def eliminar_datos(): 
        nombre_consulta = input("\t\t\tIngrese el Código de ISBN del Libro a Eliminar: ")
        
        id_libro_consulta = ControladorLibro.verificar_libro(nombre_consulta)           
        if id_libro_consulta:
            ControladorLibro.borrar_libro(id_libro_consulta)
        else:
            print("No se encontró el Libro a Eliminar\n")
                
    @staticmethod
    def listar_datos():
        
        filas = ControladorLibro.listar_libro()

        for i in filas:
            print(f"""
                \tISBN: {i[1]}
                \tTitulo: {i[2]}
                \tAutor: {i[3]}
                \tNúmero de Páginas: {i[5]}
                \tFecha Ingreso: {i[7]}
                \tFecha Publicación: {i[8]}
            """)
###########################VistaPrestamo################################

class VistaPrestamo:

  
    @staticmethod
    def menu():
        continuar = True
        

        while continuar:
            
            ControladorPrestamo.inicializar()
            ControladorPrestamoDetalle.inicializar()

            print("\t\t\t***Bienvenid@ a la Seccion de la Prestamo! ***")
            print("\t\t\tElija 1 para registrar Prestamo")
            print("\t\t\tElija 4 para regresar al Menu Pricipal")

            opcion = input("Elija una opcion : ")
            if opcion.isdigit():

                if opcion == "1":
                    VistaPrestamo.ingreso_datos()
                elif opcion == "4":
                    print("\n")
                    continuar = False
                else:
                    print("Debe Ingresar un numero de la Lista de Opciones\n")
                    continuar = True
            else:
                print("Ingrese un numero\n")
                continuar = True


    @staticmethod
    def ingreso_datos(): 
       
        detalle_prestamo ={}
        cabecera_prestamo = {}
        continua = True
        id_lector = ""
        flag_lector = ""
        flag_libro = False
        
        
        if continua :     
            cont=0
            num_tarjeta = input("\t\t\tIngrese el Numero de Tarjeta del Lector: ")
            id_lector = ControladorLector.verificar_lector(num_tarjeta) 
           
            if id_lector > 0:
                flag_lector = "S"


            while flag_lector=="S":
                cod_isbn = input("\t\t\tIngrese el Numero de ISBN del Libro: ")
                id_libro = ControladorLibro.verificar_libro(cod_isbn)
                estado_libro = ControladorLibro.verificar_estado_libro(cod_isbn)

                
                if id_libro>0 and estado_libro=="D":
                    flag_libro=True
                else: 
                    flag_lector="S"
              
                if flag_libro:
                    fec_devol_max = input("\t\t\tIngrese la Fecha a Devolver Libro: ")
                    
                    cabecera_prestamo={'id_lector' : id_lector}
                    cont+=1

                    detalle_prestamo[cont]=(id_libro, fec_devol_max)
                        
                    flag_lector=input("Desea Registar otro Libro para prestamo[S/N]? : ").upper()
                    continua=False
                    


        if len(detalle_prestamo)>0:
            ControladorPrestamo.agregar_prestamo_cabecera(cabecera_prestamo.get('id_lector'))
            id_prest = ControladorPrestamoDetalle.consultar_cabecera()

            for result in detalle_prestamo:
                ControladorPrestamoDetalle.agregar_prestamo_detalle(id_prest,
                detalle_prestamo[result][0], detalle_prestamo[result][1])

                #####UPDATE LIBRO#####
                ControladorLibro.modificar_estado_libro(detalle_prestamo[result][0])

    

###########################VistaEntrega################################

class VistaEntrega:
    @staticmethod
    def menu():
        continuar = True
        

        while continuar:
            print("\t\t\t***Bienvenid@ a la Seccion de Registro de Entrega Libro! ***")
            print("\t\t\tElija 1 para consultar los prestamos  de Lector")
            print("\t\t\tElija 2 para regresar al Menu Pricipal")

            opcion = input("Elija una opcion : ")
            if opcion.isdigit():

                if opcion == "1":
                    VistaEntrega.ingreso_datos()
                elif opcion == "2":
                    print("\n")
                    continuar = False
                else:
                    print("Debe Ingresar un numero de la Lista de Opciones\n")
                    continuar = True
            else:
                print("Ingrese un numero\n")
                continuar = True
 
    @staticmethod
    def ingreso_datos(): 
       
        
        continua = True
        id_lector = ""
       
        
        
        if continua :     
            
            num_tarjeta = input("\t\t\tIngrese el Numero de Tarjeta del Lector: ")
            id_lector = ControladorLector.verificar_lector(num_tarjeta) 
           
            if id_lector > 0:
                filas = ControladorPrestamo.listar_detalle_prestamo(id_lector)
                
                for i in filas:
                    print(f"""
                        \tN° Prestamo: {i[0]}
                        \tISBN: {i[1]}
                        \tTitulo: {i[2]}
                        \tEstado Prestamo: {i[3]}
                        \tFecha de Prestamo: {i[4]}
                        \tFecha a Devolver: {i[5]}
                    """)