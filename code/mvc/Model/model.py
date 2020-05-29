from mysql import connector

class Model:
    """
    A data model eith MySQL from a store DB
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    
    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key,val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    
    """
    ************************
    *    Peliculas Method  *
    ***********************
    """    

    def agregar_pelicula(self,nombre, sinopsis, categoria, duracion):
        try:
            sql = 'INSERT INTO pelicula (`Nombre`,`Sinopsis`,`categoria`,`duracion`) VALUES (%s, %s, %s, %s)'
            vals = (nombre, sinopsis, categoria, duracion)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_pelicula(self,id):
        try:
            sql = 'SELECT * FROM pelicula WHERE id_pelicula = %s'
            vals = (id,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err
            
    def read_all_pelicula(self):
        try:
            sql = 'SELECT * FROM pelicula'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_pelicula_categoria(self,cat):
        try:
            sql = 'SELECT * FROM pelicula WHERE categoria = %s'
            vals = (cat,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return 


    def update_pelicula(self, fields, vals):
        try:
            sql = 'UPDATE pelicula SET '+','.join(fields)+ 'WHERE id_pelicula = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True 
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_pelicula(self,id_pelicula):
        try:
            sql = 'DElETE FROM pelicula WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *********************
    *    Sala Method    *
    *********************
    """    

    def agregar_sala(self,nombre):
        try:
            sql = 'INSERT INTO sala (`nombre_sala`) VALUES (%s)'
            vals = (nombre)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_sala(self,id):
        try:
            sql = 'SELECT * FROM sala WHERE id_sala = %s'
            vals = (id,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_all_salas(self):
        try:
            sql = 'SELECT * FROM sala'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_sala(self, fields, vals):
        try:
            sql = 'UPDATE sala SET '+','.join(fields)+ ' WHERE id_sala = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True 
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_sala(self,id_sala):
        try:
            sql = 'DELETE FROM salas WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def agregar_asiento(self,id_sala,nombre):
        try:
            sql = 'INSERT INTO asiento (`id_sala`,`nombre`) VALUES (%s, %s)'
            vals = (id_sala,nombre)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_asiento(self,id):
        try:
            sql = 'SELECT * FROM asiento WHERE id_asiento = %s'
            vals = (id,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_asientos_sala(self,id_sala):
        try:
            sql = 'SELECT * FROM asiento WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def delete_asientos(self,id_sala, id_asiento):
        try:
            sql = 'DElETE FROM asiento WHERE id_asiento = %s and id_sala = %s'
            vals = (id_asiento,id_sala)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***********************
    *   Funciones Method  *
    ***********************
    """    

    def agregar_funcion(self,id_pelicula, id_sala, fecha, hora, precio, idioma):
        try:
            sql = 'INSERT INTO funcion (`id_pelicula`,`id_sala`,`fecha`, `hora`, `precio`, `idioma`) VALUES (%s, %s, %s, %s, %s, %s)'
            vals = (id_pelicula, id_sala, fecha, hora, precio, idioma)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_funcion(self,id):
        try:
            sql = 'select funcion.*, pelicula.nombre, sala.nombre_sala from funcion join pelicula join sala on funcion.id_pelicula = pelicula.id_pelicula and funcion.id_sala = sala.id_sala and funcion.id_funcion = %s'
            vals = (id,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err
            
    def read_all_funciones(self):
        try:
            sql = 'select funcion.*, pelicula.nombre, sala.nombre_sala from funcion join pelicula join sala on funcion.id_pelicula = pelicula.id_pelicula and funcion.id_sala = sala.id_sala'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_funcion_pelicula(self,nombre_pelicula):
        try:
            sql = 'select funcion.*, pelicula.Nombre, sala.nombre_sala from funcion join sala join pelicula on sala.id_sala = funcion.id_sala and pelicula.id_pelicula = funcion.id_pelicula and pelicula.nombre = %s'
            vals = (nombre_pelicula,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return 


    def update_funcion(self, fields, vals):
        try:
            sql = 'UPDATE funcion SET '+','.join(fields)+ 'WHERE id_funcion = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True 
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_funcion(self,id_funcion):
        try:
            sql = 'DELETE FROM funcion WHERE id_funcion = %s'
            vals = (id_funcion,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ***********************
    *    Boletos Method   *
    ***********************
    """    

    def agregar_boleto(self,id_funcion,asiento):
        try:
            sql = 'INSERT INTO boleto (`id_funcion`,`id_asiento`) VALUES (%s,%s)'
            vals = (id_funcion,asiento)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err


    def read_a_boleto(self,id):
        try:
            sql = 'SELECT boleto.id_boleto,funcion.*, asiento.nombre, sala.nombre_sala, pelicula.Nombre from boleto join asiento join funcion join sala join pelicula on boleto.id_funcion = funcion.id_funcion and boleto.id_asiento = asiento.id_asiento and funcion.id_sala = sala.id_sala and pelicula.id_pelicula = funcion.id_funcion and boleto.id_boleto = %s'
            vals = (id,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err
            
    def read_all_boletos(self):
        try:
            sql = 'SELECT boleto.id_boleto,funcion.*, asiento.nombre, sala.nombre_sala, pelicula.Nombre from boleto join asiento join funcion join sala join pelicula on boleto.id_funcion = funcion.id_funcion and boleto.id_asiento = asiento.id_asiento and funcion.id_sala = sala.id_sala and pelicula.id_pelicula = funcion.id_pelicula'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_boletos_funcion(self,id_funcion):
        try:
            sql = 'SELECT boleto.id_boleto,funcion.*, asiento.nombre, sala.nombre_sala, pelicula.Nombre from boleto join asiento join funcion join sala join pelicula on boleto.id_funcion = funcion.id_funcion and boleto.id_asiento = asiento.id_asiento and funcion.id_sala = sala.id_sala and pelicula.id_pelicula = funcion.id_pelicula and boleto.id_funcion = %s '
            vals = (id_funcion,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return 


    def delete_boleto(self,id_boleto):
        try:
            sql = 'DELETE FROM boleto WHERE id_boleto = %s'
            vals = (id_boleto,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def asientos_funcion(self, id_funcion):
        try:
            sql = 'SELECT asiento.* FROM boleto join asiento on asiento.id_asiento = boleto.id_asiento and boleto.id_funcion = %s'
            vals = (id_funcion,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return 

    
    """
    *****************************
    *    Administrador Method   *
    *****************************
    """    

    def agregar_administrador(self,nombre,apellido_p,apellido_m,usuario,contraseña):
        try:
            sql = 'INSERT INTO administrador (`nombre`,`apellido_p`,`apellido_m`,`usuario`,`contraseña`) VALUES (%s,%s,%s,%s,%s)'
            vals = (nombre,apellido_p,apellido_m,usuario,contraseña)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_administrador(self,id):
        try:
            sql = 'SELECT * FROM administrador WHERE id_admin = %s'
            vals = (id,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_all_administradores(self):
        try:
            sql = 'SELECT * FROM administrador'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_administrador(self, fields, vals):
        try:
            sql = 'UPDATE administrador SET '+','.join(fields)+ 'WHERE id_admin = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True 
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_admin(self,id_admin):
        try:
            sql = 'DELETE FROM administrador WHERE id_admin = %s'
            vals = (id_admin,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def admin_login(self, usuario, contraseña):
        try:
            sql = 'SELECT nombre FROM administrador WHERE usuario = %s and contraseña = %s'
            vals = (usuario,contraseña)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err