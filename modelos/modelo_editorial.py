from conexion import conexion as cx


class Editorial:

    _tabla = "EDITORIAL"
    _identificador = "cod_ed"

    def __init__(self, nombre="", pais="", telefono=""):       
        self.nombre = nombre
        self.pais = pais
        self.telefono = telefono

    def __str__(self):
        return f"\nEditorial : {self.nombre} {self.pais} {self.telefono}\n"

    @staticmethod
    def inicializar():
        cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=True).crear_tabla_editorial()
      
    def insertar_editorial(self):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        obj_conexion.cx_postgres.insertar_editorial(self.nombre, self.pais, self.telefono)
    
    def consultar_editorial(self):   
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        cod_ed = obj_conexion.cx_postgres.consultar_registro_editorial(self.nombre)
        return cod_ed
        
    def actualizar_editorial(self, cod_ed):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        obj_conexion.cx_postgres.actualizar_datos_editorial(self.nombre, self.pais, self.telefono, cod_ed)
      
    def eliminar_editorial(self, cod_ed):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        obj_conexion.cx_postgres.eliminar_registro(self._identificador, cod_ed)
    
    
    def listar_editorial(self):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        return obj_conexion.cx_postgres.leer_datos()



       
      
