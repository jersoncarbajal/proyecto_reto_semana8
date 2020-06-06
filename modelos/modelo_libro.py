from conexion import conexion as cx


class Libro:

    _tabla = "LIBRO"
    _identificador = "id_libro"

    def __init__(self, isbn, titulo, autor, cod_ed, num_paginas, id_tipo, fecha_ingreso, fecha_publicacion):       
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.cod_ed = cod_ed
        self.num_paginas = num_paginas
        self.id_tipo = id_tipo
        self.fecha_ingreso = fecha_ingreso
        self.fecha_publicacion = fecha_publicacion
  
    @staticmethod
    def inicializar():
        cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=True).crear_tabla_libro()
      
    def insertar_libro(self):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        obj_conexion.cx_postgres.insertar_libro(self.isbn, self.titulo, self.autor, self.cod_ed, 
        self.num_paginas, self.id_tipo, self.fecha_ingreso, self.fecha_publicacion)
    
    def consultar_libro(self):   
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        cod_libro = obj_conexion.cx_postgres.consultar_registro_libro(self.isbn)
        return cod_libro

    def consultar_estado_libro(self):   
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        cod_libro = obj_conexion.cx_postgres.consultar_estado_libro(self.isbn)
        return cod_libro
        
    def actualizar_libro(self, id_libro):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        obj_conexion.cx_postgres.actualizar_datos_libro(self.titulo, self.autor, self.cod_ed, 
        self.num_paginas, self.id_tipo, self.fecha_ingreso, self.fecha_publicacion, id_libro)
      
    def eliminar_libro(self, id_libro):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        obj_conexion.cx_postgres.eliminar_registro(self._identificador, id_libro)
    
    
    def listar_libro(self):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        return obj_conexion.cx_postgres.leer_datos()

    def actualizar_estado_libro(self, id_libro):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        obj_conexion.cx_postgres.actualizar_estado_libro(id_libro)
    