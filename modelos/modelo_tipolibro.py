from conexion import conexion as cx


class TipoLibro:

    _tabla = "TIPO_LIBRO"
    _identificador = "id_tipo"

    def __init__(self, nombre="", desc=""):       
        self.nombre = nombre
        self.desc = desc

    def __str__(self):
        return f"\nTipoLibro : {self.nombre} {self.desc}\n"

    @staticmethod
    def inicializar():
        cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=True).crear_tabla_tipo_libro()
      
    def insertar_tipo_libro(self):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        obj_conexion.cx_postgres.insertar_tipolibro(self.nombre, self.desc)
    
    def consultar_tipo_libro(self):   
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        id_tipo_libro = obj_conexion.cx_postgres.consultar_registro(self.nombre)
        return id_tipo_libro
        
    def actualizar_tipo_libro(self, id_tipo_libro):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        obj_conexion.cx_postgres.actualizar_datos_tipolibro(self.nombre, self.desc, id_tipo_libro)
      
    def eliminar_tipo_libro(self, id_tipo_libro):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        obj_conexion.cx_postgres.eliminar_registro(self._identificador, id_tipo_libro)
    
    
    def listar_tipo_libro(self):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        return obj_conexion.cx_postgres.leer_datos()



       
      
