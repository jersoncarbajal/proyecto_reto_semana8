from conexion import conexion as cx


class PrestamoDetalle:

    _tabla = "DETALLE_PRESTAMO"
   
    def __init__(self, id_prest, id_libro, fec_devol_max):       
        self.id_prest = id_prest
        self.id_libro = id_libro
        self.fec_devol_max = fec_devol_max


    @staticmethod
    def inicializar():
        cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=True).crear_tabla_detalle_prestamo()

    @staticmethod
    def consultar_cabecera():
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        return obj_conexion.cx_postgres.consultar_cabecera_prestamo()
      
    def insertar_prestamo_detalle(self):
        obj_conexion = cx.Conexion(crear_conexion_pg=True, crear_conexion_mdb=False)
        obj_conexion.cx_postgres.cambiar_tabla(self._tabla)
        obj_conexion.cx_postgres.insertar_dprestamo(self.id_prest, self.id_libro, self.fec_devol_max)

