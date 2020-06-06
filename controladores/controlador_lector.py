from modelos.modelo_lector import Lector



class ControladorLector:      
       
   
    @staticmethod
    def inicializar():
        Lector.inicializar()
       
    @staticmethod
    def agregar_lector(num_tarjeta, nombre, direccion, dni, correo, telefono):
        obj_lector = Lector(num_tarjeta, nombre, direccion, dni, correo, telefono)
        obj_lector.insertar_lector()

    @staticmethod
    def verificar_lector(num_tarjeta):
        obj_lector = Lector(num_tarjeta,
        nombre=None, direccion=None, dni=None, correo=None, telefono=None)
        return obj_lector.consultar_lector()

    @staticmethod
    def modificar_lector(num_tarjeta, nuevo_nombre, nueva_direccion, nuevo_dni, nuevo_correo, nuevo_telefono, id_lector):
        obj_lector = Lector(num_tarjeta, nuevo_nombre, nueva_direccion, nuevo_dni, nuevo_correo, nuevo_telefono)
        obj_lector.actualizar_lector(id_lector)

    @staticmethod
    def borrar_lector(id_lector):
        obj_lector = Lector(num_tarjeta=None,
        nombre=None, direccion=None, dni=None, correo=None, telefono=None)
        obj_lector.eliminar_lector(id_lector)
        
    @staticmethod
    def listar_lector():
        obj_lector = Lector(num_tarjeta=None,
        nombre=None, direccion=None, dni=None, correo=None, telefono=None)
        return obj_lector.listar_lector()
    

