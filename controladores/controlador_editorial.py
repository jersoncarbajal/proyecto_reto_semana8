from modelos.modelo_editorial import Editorial



class ControladorEditorial:      
       
   
    @staticmethod
    def inicializar():
        Editorial.inicializar()
       
    @staticmethod
    def agregar_editorial(nombre, pais, telefono):
        obj_editorial = Editorial(nombre, pais, telefono)
        obj_editorial.insertar_editorial()

    @staticmethod
    def verificar_editorial(nombre):
        obj_editorial = Editorial(nombre, pais=None, telefono=None)
        return obj_editorial.consultar_editorial()

    @staticmethod
    def modificar_editorial(nuevo_nombre, nuevo_pais, nuevo_telefono, cod_ed):
        obj_editorial = Editorial(nuevo_nombre, nuevo_pais, nuevo_telefono)
        obj_editorial.actualizar_editorial(cod_ed)

    @staticmethod
    def borrar_editorial(cod_ed):
        obj_editorial = Editorial(nombre=None, pais=None, telefono=None)
        obj_editorial.eliminar_editorial(cod_ed)
        
    @staticmethod
    def listar_editorial():
        obj_editorial = Editorial(nombre=None, pais=None, telefono=None)
        return obj_editorial.listar_editorial()
    

