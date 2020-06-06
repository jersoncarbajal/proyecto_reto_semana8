from modelos.modelo_tipolibro import TipoLibro



class ControladorTipoLibro:      
       
   
    @staticmethod
    def inicializar():
        TipoLibro.inicializar()
       
    @staticmethod
    def agregar_tipo_libro(nombre, desc):
        obj_tipo_libro = TipoLibro(nombre, desc)
        obj_tipo_libro.insertar_tipo_libro()

    @staticmethod
    def verificar_tipo_libro(nombre):
        obj_tipo_libro = TipoLibro(nombre, desc=None)
        return obj_tipo_libro.consultar_tipo_libro()

    @staticmethod
    def modificar_tipo_libro(nuevo_nombre, nueva_descripcion, id_tipo_libro):
        obj_tipo_libro = TipoLibro(nuevo_nombre, nueva_descripcion)
        obj_tipo_libro.actualizar_tipo_libro(id_tipo_libro)

    @staticmethod
    def borrar_tipo_libro(id_tipo_libro):
        obj_tipo_libro = TipoLibro(nombre=None, desc=None)
        obj_tipo_libro.eliminar_tipo_libro(id_tipo_libro)
        
    @staticmethod
    def listar_tipo_libro():
        obj_tipo_libro = TipoLibro(nombre=None, desc=None)
        return obj_tipo_libro.listar_tipo_libro()
    

