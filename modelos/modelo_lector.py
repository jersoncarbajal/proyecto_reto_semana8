from conexion import conexion as cx


class Lector:

    _tabla = "LECTOR"
    _identificador = "id_lector"

    def __init__(self, num_tarjeta="", nombre="", direccion="", dni="", correo="", telefono=""):       
        self.num_tarjeta = num_tarjeta
        self.nombre = nombre
        self.direccion = direccion
        self.dni = dni
        self.correo = correo
        self.telefono = telefono


    def __str__(self):
        return f"\nLector : {self.num_tarjeta} {self.nombre} {self.direccion} {self.dni} {self.correo} {self.telefono}\n"

    @staticmethod
    def inicializar():
        cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=True).crear_tabla_lector()
      
    def insertar_lector(self):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        obj_conexion.cx_postgres.insertar_lector(self.num_tarjeta, self.nombre,
         self.direccion, self.dni, self.correo, self.telefono)
    
    def consultar_lector(self):   
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        id_lector = obj_conexion.cx_postgres.consultar_registro_lector(self.num_tarjeta)
        return id_lector
        
    def  actualizar_lector(self, id_lector):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        obj_conexion.cx_postgres.actualizar_datos_lector(self.nombre,
        self.direccion, self.dni, self.correo, self.telefono, id_lector)
      
    def eliminar_lector(self, id_lector):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        obj_conexion.cx_postgres.eliminar_registro(self._identificador, id_lector)
    
    
    def listar_lector(self):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        return obj_conexion.cx_postgres.leer_datos()



       
      
