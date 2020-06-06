from modelos.modelo_prestamo_detalle  import PrestamoDetalle

class ControladorPrestamoDetalle:      
    
    @staticmethod
    def inicializar():
        PrestamoDetalle.inicializar()


    @staticmethod
    def consultar_cabecera():
        return PrestamoDetalle.consultar_cabecera()

    @staticmethod
    def agregar_prestamo_detalle(id_prest, id_libro, fec_devol_max):
        obj = PrestamoDetalle(id_prest, id_libro, fec_devol_max)
        obj.insertar_prestamo_detalle()
  

    