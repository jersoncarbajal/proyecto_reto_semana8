from pymongo import MongoClient, errors
from logger import escribir_al_log
import atributos_conexion
from psycopg2 import connect, Error

class Conexion:

    def __init__(self, crear_conexion_pg=True, crear_conexion_mdb=True):

        self.cx_postgres = None
        self.cx_mongodb = None

        

        if crear_conexion_pg:
            self.cx_postgres = ConexionPG(
                direccion_servidor=atributos_conexion.DIRECCION_SERVIDOR_POSTGRES,
                usuario=atributos_conexion.USUARIO_POSTGRES,
                contrasena=atributos_conexion.CONTRASENA_POSTGRES,
                base_datos=atributos_conexion.BASE_DATOS_POSTGRES,
                tabla=""
            )
           
        if crear_conexion_mdb:
            self.cx_mongodb = ConexionMDB(
                atributos_conexion.CADENA_DE_CONEXION_MONGODB,
                atributos_conexion.BASE_DATOS_MONGODB,
                atributos_conexion.COLECCION_MONGODB
            )
           
##LECTOR##
    def crear_tabla_lector(self):

            #print('>----CREACIONN LECTOR TABLAS S/N?---<')
            existe = self.cx_mongodb.obtener_documento_mdb(
                {
                    'tipo': "CREACION_DB",
                    'recurso': 'lector'
                }
            )
            if not existe:
                #print('>----CREACIONN LECTOR TABLAS---<')
                self.cx_postgres.crear_tabla(
                    """
                    CREATE TABLE LECTOR(
                        id_lector SERIAL NOT NULL PRIMARY KEY,
                        num_tarjeta VARCHAR(50) NOT NULL,
						nombre VARCHAR(200) NOT NULL,
						direccion VARCHAR(200) NOT NULL,
						dni VARCHAR(20) NOT NULL,
						correo VARCHAR(100) NOT NULL,
						telefono VARCHAR(20) NOT NULL					
						)
                    """
                )
                self.cx_mongodb.insertar_documento_mdb(
                    {
                        "tipo": "CREACION_DB",
                        "recurso": "lector"
                    }
                )


##TIPO_LIBRO##
    def crear_tabla_tipo_libro(self):

            #print('>----CREACIONN TIPO_LIBRO TABLAS S/N?---<')
        
            existe = self.cx_mongodb.obtener_documento_mdb(
                {
                    'tipo': "CREACION_DB",
                    'recurso': 'tipo_libro'
                }
            )
            if not existe:
                #print('>----CREACIONN TIPO_LIBRO TABLAS---<')
                
                self.cx_postgres.crear_tabla(
                    """
                    CREATE TABLE TIPO_LIBRO(
                        id_tipo SERIAL NOT NULL PRIMARY KEY,
                        nombre VARCHAR(100) NOT NULL,
                        descripcion VARCHAR(100)
						)
                    """
                )
                self.cx_mongodb.insertar_documento_mdb(
                    {
                        "tipo": "CREACION_DB",
                        "recurso": "tipo_libro"
                    }
                )

##EDITORIAL##
    def crear_tabla_editorial(self):
            #print('>----CREACIONN EDITORIAL TABLAS S/N?---<')      
            existe = self.cx_mongodb.obtener_documento_mdb(
                {
                    'tipo': "CREACION_DB",
                    'recurso': 'editorial'
                }
            )
            if not existe:
                #print('>----CREACIONN EDITORIAL TABLAS---<')
                
                self.cx_postgres.crear_tabla(
                    """
                    CREATE TABLE EDITORIAL(
                        cod_ed SERIAL NOT NULL PRIMARY KEY,
                        nombre VARCHAR(100) NOT NULL,
                        pais VARCHAR(100) NOT NULL,
                        telefono VARCHAR(50) NOT NULL
						)
                    """
                )
                self.cx_mongodb.insertar_documento_mdb(
                    {
                        "tipo": "CREACION_DB",
                        "recurso": "editorial"
                    }
                )

##LIBRO##
    def crear_tabla_libro(self):
            #print('>----CREACIONN LIBRO TABLAS S/N?---<')       
            existe = self.cx_mongodb.obtener_documento_mdb(
                {
                    'tipo': "CREACION_DB",
                    'recurso': 'libro'
                }
            )
            if not existe:
                #print('>----CREACIONN LIBRO TABLAS---<')
                self.cx_postgres.crear_tabla(
                    """
                    CREATE TABLE LIBRO(
                        id_libro SERIAL NOT NULL PRIMARY KEY,
                        isbn VARCHAR(200) NOT NULL,
                        titulo VARCHAR(200) NOT NULL,
						autor VARCHAR(200) NOT NULL,
						cod_ed INTEGER NOT NULL,
						num_paginas INTEGER NOT NULL,
						id_tipo INTEGER NOT NULL,
						fecha_ingreso VARCHAR(10) NOT NULL,
						fecha_publicacion VARCHAR(10) NOT NULL,
                        estado CHAR(1) NOT NULL DEFAULT 'D',
						FOREIGN KEY (cod_ed) REFERENCES EDITORIAL (cod_ed),
						FOREIGN KEY (id_tipo) REFERENCES TIPO_LIBRO (id_tipo)
						)
                    """
                )
                self.cx_mongodb.insertar_documento_mdb(
                    {
                        "tipo": "CREACION_DB",
                        "recurso": "libro"
                    }
                )

##PRESTAMO##
    def crear_tabla_prestamo(self):
            #print('>----CREACIONN PRESTAMO TABLAS S/N?---<')       
            existe = self.cx_mongodb.obtener_documento_mdb(
                {
                    'tipo': "CREACION_DB",
                    'recurso': 'prestamo'
                }
            )
            if not existe:
                #print('>----CREACIONN LIBRO TABLAS---<')
                self.cx_postgres.crear_tabla(
                    """
                    CREATE TABLE PRESTAMO(
                        id_prest SERIAL NOT NULL PRIMARY KEY,
                        id_lector INTEGER NOT NULL,
                        fec_solic DATE NOT NULL DEFAULT CURRENT_DATE,
                        estado CHAR(1) NOT NULL DEFAULT 'A',
						FOREIGN KEY (id_lector) REFERENCES LECTOR (id_lector)
						)
                    """
                )
                self.cx_mongodb.insertar_documento_mdb(
                    {
                        "tipo": "CREACION_DB",
                        "recurso": "prestamo"
                    }
                )


##DETALLE PRESTAMO##
    def crear_tabla_detalle_prestamo(self):
            #print('>----CREACIONN DETALLE PRESTAMO TABLAS S/N?---<')       
            existe = self.cx_mongodb.obtener_documento_mdb(
                {
                    'tipo': "CREACION_DB",
                    'recurso': 'detalle_prestamo'
                }
            )
            if not existe:
                #print('>----CREACIONN DETALLE TABLAS---<')
                self.cx_postgres.crear_tabla(
                    """
                    CREATE TABLE DETALLE_PRESTAMO(
                        id_prest INTEGER NOT NULL,
                        id_libro INTEGER NOT NULL,
                        mora DECIMAL(5,2) NOT NULL DEFAULT 0.00,
                        est_prest CHAR(1) NOT NULL DEFAULT 'P' ,
                        fec_devol_max VARCHAR(10) NOT NULL,
                        fec_devol VARCHAR(10) NOT NULL DEFAULT '',
                        PRIMARY KEY (id_prest, id_libro),
						FOREIGN KEY (id_prest) REFERENCES PRESTAMO (id_prest),
                        FOREIGN KEY (id_libro) REFERENCES LIBRO (id_libro)
						)
                    """
                )
                self.cx_mongodb.insertar_documento_mdb(
                    {
                        "tipo": "CREACION_DB",
                        "recurso": "detalle_prestamo"
                    }
                )


########################################POSTGRES_DB###########################################

class ConexionPG:
    def __init__(self, **parametros):
        
        try:
            self.db = connect(
                host=parametros['direccion_servidor'],
                user=parametros['usuario'],
                password=parametros['contrasena'],
                database=parametros['base_datos']
            )
            self.cursor = self.db.cursor()
            self.tabla = parametros['tabla']
            self.campo_condicional = ''
           
        except Error as e:
            escribir_al_log(e, "Ocurrio un error al conectar a la base de datos aqui")

    def crear_tabla(self, sentencia_sql=None):
        if sentencia_sql is not None:
                self._ejecutar_sql(sentencia_sql)
   
    def __del__(self):
        self.db.close()

    def _ejecutar_sql(
        self, sentencia_sql, parametros=None, 
        escribir_en_bd=True
    ):
        try:
            self.cursor.execute(sentencia_sql, parametros) # execute corre las sentencias sql
            if escribir_en_bd:
                self.db.commit()
            else:
                return self.cursor.rowcount
                
        except Exception as e:
            escribir_al_log(e, f"Ocurrio un error al ejecutar la sentencia SQL:\n\n{sentencia_sql}\n")
            if escribir_en_bd:
                self.db.rollback()

    def _leer_desde_sql(self):
        registros = []
        try:
            registros = self.cursor.fetchall()
        except Exception as e:
            escribir_al_log(e, f'Un error ocurrió al momento de leer desde la BD')
        return registros    

    def leer_datos(self):
        
        self._ejecutar_sql(
            "SELECT * FROM " + self.tabla + " ORDER BY 1",
            escribir_en_bd=False
        )
        return self._leer_desde_sql()    

    
###consultar_registro###    
    def consultar_registro(self, nombre):
        try:
            self._ejecutar_sql("SELECT id_tipo FROM " + self.tabla + f"""  WHERE nombre='{nombre}';""",
            escribir_en_bd=False)   
            if self.cursor.rowcount:
                id_fila = self.cursor.fetchone()[0]
                return id_fila
            else:
                return self.cursor.rowcount
        except Exception as e:
             escribir_al_log(e, f'Un error ocurrió al momento de consultar registro')


    def consultar_registro_editorial(self, nombre):
        try:
            self._ejecutar_sql("SELECT cod_ed FROM " + self.tabla + f"""  WHERE nombre='{nombre}';""",
            escribir_en_bd=False)   
            if self.cursor.rowcount:
                id_fila = self.cursor.fetchone()[0]
                return id_fila
            else:
                return self.cursor.rowcount
        except Exception as e:
             escribir_al_log(e, f'Un error ocurrió al momento de consultar registro')


    def consultar_registro_lector(self, num_tarjeta):
        try:       
            self._ejecutar_sql("SELECT id_lector FROM " + self.tabla + f"""  WHERE num_tarjeta='{num_tarjeta}';""",
            escribir_en_bd=False)
            if self.cursor.rowcount:
                id_fila = self.cursor.fetchone()[0]
                return id_fila
            else:
                return self.cursor.rowcount
        except Exception as e:
             escribir_al_log(e, f'Un error ocurrió al momento de consultar registro lector')


    def consultar_registro_libro(self, isbn):
        try:            
            self._ejecutar_sql("SELECT id_libro FROM " + self.tabla + f"""  WHERE isbn ='{isbn}';""",
            escribir_en_bd=False)

            if self.cursor.rowcount is not None:
                id_fila = self.cursor.fetchone()[0]
                return id_fila
            else:
                return 0
        except Exception as e:
             escribir_al_log(e, f'Un error ocurrió al momento de consultar registro libro')

    def consultar_estado_libro(self, isbn):
        try:            
            self._ejecutar_sql("SELECT estado FROM " + self.tabla + f"""  WHERE isbn ='{isbn}';""",
            escribir_en_bd=False)
            if self.cursor.rowcount:
                id_fila = self.cursor.fetchone()[0]
                return id_fila
            else:
                return self.cursor.rowcount
        except Exception as e:
             escribir_al_log(e, f'Un error ocurrió al momento de consultar registro libro')

    def consultar_cabecera_prestamo(self):
        try:            
            self._ejecutar_sql("SELECT CASE WHEN max(id_prest) IS NULL THEN 0 ELSE max(id_prest) END AS id_prest FROM PRESTAMO;",
            escribir_en_bd=False)
            if self.cursor.rowcount:
                id_fila = self.cursor.fetchone()[0]
                return id_fila
            else:
                return self.cursor.rowcount
        except Exception as e:
             escribir_al_log(e, f'Un error ocurrió al momento de consultar cabecera')

    def consultar_prestamo_lector(self, id_lector):
        try: 
                     
            self._ejecutar_sql(f"""
            SELECT CAB.id_prest, LIB.isbn, LIB.titulo, DET.est_prest, CAB.fec_solic, DET.fec_devol_max
            FROM PRESTAMO AS CAB
            INNER JOIN  DETALLE_PRESTAMO AS DET 
            ON CAB.id_prest = DET.id_prest INNER JOIN LIBRO AS LIB
            ON DET.id_libro = LIB.id_libro
            WHERE CAB.id_lector={id_lector};""",
            escribir_en_bd=False)
            
            return self._leer_desde_sql() 
            
        except Exception as e:
             escribir_al_log(e, f'Un error ocurrió al momento de consultar prestamo por lector')
###consultar_registro### 

###INSERTAR_PG###
    def insertar_tipolibro(self, nombre, desc):      
        self._ejecutar_sql(
            sentencia_sql="INSERT INTO " + self.tabla + " (nombre,descripcion) VALUES (%s,%s);",
            parametros=(nombre,desc)
            )
        print("Se agrego correctamente el Tipo de Libro\n")


    def insertar_lector(self, num_tarjeta, nombre, direccion, dni, correo, telefono):      
        self._ejecutar_sql(
            sentencia_sql="INSERT INTO " + self.tabla + " (num_tarjeta, nombre, direccion, dni, correo, telefono) VALUES (%s,%s,%s,%s,%s,%s);",
            parametros=(num_tarjeta, nombre, direccion, dni, correo, telefono)
            )
        print("Se agrego correctamente el Lector\n")


    def insertar_editorial(self, nombre, pais, telefono):      
        self._ejecutar_sql(
            sentencia_sql="INSERT INTO " + self.tabla + " (nombre, pais, telefono) VALUES (%s,%s,%s);",
            parametros=(nombre, pais, telefono)
            )
        print("Se agrego correctamente la Editorial\n")


    def insertar_libro(self, isbn, titulo, autor, cod_ed, num_paginas, id_tipo, fecha_ingreso, fecha_publicacion):      
        self._ejecutar_sql(
            sentencia_sql="INSERT INTO " + self.tabla + 
            " (isbn, titulo, autor, cod_ed, num_paginas, id_tipo, fecha_ingreso, fecha_publicacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
            parametros=(isbn, titulo, autor, cod_ed, num_paginas, id_tipo, fecha_ingreso, fecha_publicacion)
            )
        print("Se agrego correctamente el Libro\n")

    def insertar_cprestamo(self, id_lector):      
        self._ejecutar_sql(
            sentencia_sql="INSERT INTO " + self.tabla + " (id_lector) VALUES (%s);",
            parametros=(id_lector,)
            )

    def insertar_dprestamo(self, id_prest, id_libro, fec_devol_max):      
        self._ejecutar_sql(
            sentencia_sql="INSERT INTO " + self.tabla + " (id_prest, id_libro, fec_devol_max) VALUES (%s,%s,%s);",
            parametros=(id_prest, id_libro, fec_devol_max)
            )   

###ACTUALIZAR###
    def actualizar_datos_tipolibro(self, nombre, desc, id):
        
        sentencia_sql="UPDATE  " + self.tabla + f"""  SET nombre = '{nombre}', descripcion = '{desc}' where ID_TIPO = {id}"""
        self._ejecutar_sql(sentencia_sql, parametros=(nombre, desc, id))
        print("Se Actualizo correctamente el Tipo de Libro\n")

    def actualizar_datos_lector(self, nombre, direccion, dni, correo, telefono, id_lector):
        
        sentencia_sql="UPDATE  " + self.tabla + f"""  SET  nombre = '{nombre}',
        direccion = '{direccion}', dni = '{dni}', correo = '{correo}', telefono = '{telefono}' where id_lector = {id_lector}"""
        self._ejecutar_sql(sentencia_sql, parametros=(nombre, direccion, dni, correo, telefono,  id_lector))
        print("Se Actualizo correctamente el Tipo de Libro\n")

    def actualizar_datos_editorial(self, nombre, pais, telefono, cod_ed):
        
        sentencia_sql="UPDATE  " + self.tabla + f"""  SET  nombre = '{nombre}',
        pais = '{pais}', telefono = '{telefono}' where cod_ed = {cod_ed}"""
        self._ejecutar_sql(sentencia_sql, parametros=(nombre, pais, telefono, cod_ed))
        print("Se Actualizo correctamente los datos de Editorial \n")

    def actualizar_datos_libro(self, titulo, autor, cod_ed, num_paginas, 
        id_tipo, fecha_ingreso, fecha_publicacion, id_libro):
        
        sentencia_sql="UPDATE  " + self.tabla + f"""  SET  titulo = '{titulo}', autor = '{autor}', cod_ed = {cod_ed}, num_paginas = {num_paginas}, \
        id_tipo = {id_tipo}, fecha_ingreso = '{fecha_ingreso}', fecha_publicacion = '{fecha_publicacion}' where id_libro = {id_libro}"""
        self._ejecutar_sql(sentencia_sql, 
        parametros=(titulo, autor, cod_ed, num_paginas, id_tipo, fecha_ingreso, fecha_publicacion))
        print("Se Actualizo correctamente del Libro\n")

    def actualizar_estado_libro(self, id_libro):
        
        sentencia_sql="UPDATE  " + self.tabla + f"""  SET  estado = 'P' where id_libro = {id_libro}"""
        self._ejecutar_sql(sentencia_sql, 
        parametros=(id_libro))
        print("Se Actualizo correctamente estado del Libro\n")

###ELIMINAR###
    def eliminar_registro(self, identificador, id_libro):
        self._ejecutar_sql(
            "DELETE FROM " + self.tabla + f" WHERE  {identificador}=%s",
            parametros=(id_libro,)
        )
        print("Se ha Eliminado el Registro\n")

    def cambiar_tabla(self, tabla):
        self.tabla = tabla

    def cambiar_campo(self, campo_condicional):
        self.campo_condicional = campo_condicional


    
###########################################MONGO_DB##################################################
class ConexionMDB:

    def __init__(self, cadena_conexion, base_datos, coleccion):
        try:
            self.client = MongoClient(
                cadena_conexion
            )
            self.db_md = self.client[base_datos]
            self.coleccion = self.db_md[coleccion]
        except errors.ConnectionFailure as e:
            escribir_al_log(
                e,
                f"Ocurrio un error al conectarnos a la BD MongoDB {base_datos}"
            )
            
    def __del__(self):
        self.client.close()

    def insertar_documento_mdb(self, datos_documento):
        nuevo_id = None
        try:
            resultado = self.coleccion.insert_one(datos_documento)
            nuevo_id = resultado.inserted_id
        except errors.PyMongoError as e:
            escribir_al_log(
                e,
                "Ocurrio un error al insertar el documento a la BD MongoDB"
            )
        return nuevo_id


    def obtener_documentos_mdb(self, condicion):
        documentos = []
        try:
            respuesta = self.coleccion.find(condicion)
            documentos = list(respuesta)
        except errors.PyMongoError as e:
            escribir_al_log(
                e,
                "Ocurrio un error al buscar los documentos en la BD MongoDB"
            )
        return documentos

    def obtener_documento_mdb(self, condicion):
        documento = None
        try:
            documento = self.coleccion.find_one(condicion)
        except errors.PyMongoError as e:
            escribir_al_log(
                e,
                "Ocurrio un error al obtener el documento de la BD MongoDB"
            )
        return documento