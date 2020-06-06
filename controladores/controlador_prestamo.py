from modelos.modelo_prestamo import Prestamo

class ControladorPrestamo:      
       
   
    @staticmethod
    def inicializar():
        Prestamo.inicializar()

    @staticmethod   
    def agregar_prestamo_cabecera(id_lector):
        obj_prestamo = Prestamo(id_lector)
        obj_prestamo.insertar_prestamo()
        

    @staticmethod
    def listar_detalle_prestamo(id_lector):
        obj_prestamo = Prestamo(id_lector)
        return obj_prestamo.listar_prestamo()