from conexion import conexion as cx


class Prestamo:

    _tabla = "PRESTAMO"
    _identificador = "id_prest"

    def __init__(self, id_lector):  
        self.id_lector = id_lector 

    @staticmethod
    def inicializar():
        cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=True).crear_tabla_prestamo()  
        
      
    def insertar_prestamo(self):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        obj_conexion.cx_postgres.insertar_cprestamo(self.id_lector)

    def listar_prestamo(self):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        return obj_conexion.cx_postgres.consultar_prestamo_lector(self.id_lector)