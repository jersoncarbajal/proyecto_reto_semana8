from modelos.modelo_libro import Libro



class ControladorLibro:      
       
   
    @staticmethod
    def inicializar():
        Libro.inicializar()
       
    @staticmethod
    def agregar_libro(isbn, titulo, autor, cod_ed, num_paginas, id_tipo, 
        fecha_ingreso, fecha_publicacion):
        obj_libro = Libro(isbn, titulo, autor, cod_ed, num_paginas, id_tipo, 
        fecha_ingreso, fecha_publicacion)
        obj_libro.insertar_libro()

    @staticmethod
    def verificar_libro(isbn):
        obj_libro = Libro(isbn, titulo=None, autor=None, cod_ed=None, num_paginas=None, id_tipo=None,
        fecha_ingreso=None, fecha_publicacion=None)
        return obj_libro.consultar_libro()

    @staticmethod
    def verificar_estado_libro(isbn):
        obj_libro = Libro(isbn, titulo=None, autor=None, cod_ed=None, num_paginas=None, id_tipo=None,
        fecha_ingreso=None, fecha_publicacion=None)
        return obj_libro.consultar_estado_libro()

    @staticmethod
    def modificar_libro(isbn, titulo, autor, cod_ed, num_paginas, id_tipo, fecha_ingreso, fecha_publicacion, id_libro):
        obj_libro = Libro(isbn, titulo, autor, cod_ed, num_paginas, id_tipo, fecha_ingreso, fecha_publicacion)
        obj_libro.actualizar_libro(id_libro)

    @staticmethod
    def borrar_libro(id_libro):
        obj_libro = Libro(isbn=None, titulo=None, autor=None, cod_ed=None, num_paginas=None, id_tipo=None,
        fecha_ingreso=None, fecha_publicacion=None)
        obj_libro.eliminar_libro(id_libro)
        
    @staticmethod
    def listar_libro():
        obj_libro = Libro(isbn=None, titulo=None, autor=None, cod_ed=None, num_paginas=None, id_tipo=None,
        fecha_ingreso=None, fecha_publicacion=None)
        return obj_libro.listar_libro()

    @staticmethod
    def modificar_estado_libro(id_libro):
        obj_libro = Libro(isbn=None, titulo=None, autor=None, cod_ed=None, num_paginas=None, id_tipo=None,
        fecha_ingreso=None, fecha_publicacion=None)
        obj_libro.actualizar_estado_libro(id_libro)

    
    

