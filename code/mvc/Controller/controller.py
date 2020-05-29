from Model.model import Model
from View.view import View


class Controller:
    """
    *********************************
    *  A controller for a store DB  *
    *********************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()


    """
    *********************************
    *       General Controller      *
    *********************************
    """
    def main_menu(self):
        o = '0'
        while 0 != '3':
            self.view.main_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.menu_usuario()
            elif o == '2':
                self.login()
            elif o == '3':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields,vals


    def menu_usuario(self):
        o = '0'
        while o != '4':
            self.view.main_menu_usuario()
            self.view.option('4')
            o = input()
            if o == '1':
                self.usuario_peliculas()
            elif o == '2':
                self.usuario_funciones()
            elif o == '3':
                self.usuario_boletos()
            elif o == '4':
                self.main_menu()
                return
            else:
                self.view.not_valid_option()
        return

    def administrador_menu(self):
        o = '0'
        while o != '5':
            self.view.main_menu_admin()
            self.view.option('5')
            o = input()
            if o == '1':
                self.administrador_peliculas()
            elif o == '2':
                self.administrador_salas()
            elif o == '3':
                self.administrador_funciones()
            elif o == '4':
                self.administrador_boletos()
            elif o == '5':
                self.administrador_admins()
            elif o == '6':
                self.main_menu()
                return
            else:
                self.view.not_valid_option()
        return


    """
    *********************************
    *   Controllers for peliculas   *
    *********************************
    """

    def administrador_peliculas(self):
        o = '0'
        while o != '7':
            self.view.peliculas_menu_admin()
            self.view.option('7')
            o = input()
            if o == '1':
                self.agregar_pelicula()
            elif o == '2':
                self.read_a_pelicula()
            elif o == '3':
                self.read_all_peliculas()
            elif o == '4':
                self.read_peliculas_categoria()
            elif o == '5':
                self.update_pelicula()
            elif o == '6':
                self.delete_pelicula()
            elif o == '7':
                self.administrador_menu()
                return
            else:
                self.view.not_valid_option()
        return

    def usuario_peliculas(self):
        o = '0'
        while o != '3':
            self.view.pelicuas_menu_usuario()
            self.view.option('3')
            o = input()
            if o == '1':
                self.read_all_peliculas()
            elif o == '2':
                self.read_peliculas_categoria()
            elif o == '3':
                self.menu_usuario()
                return
            else:
                self.view.not_valid_option()
        return

    def ask_pelicula(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Sinopsis: ')
        sinopsis = input()
        self.view.ask('Categoria: ')
        categoria = input()
        self.view.ask('Duracion: ')
        duracion = input()
      
        return [nombre, sinopsis, categoria, duracion]

    def agregar_pelicula(self):
        nombre, sinopsis, categoria, duracion = self.ask_pelicula()
        out = self.model.agregar_pelicula(nombre, sinopsis, categoria, duracion)
        if out == True:
            self.view.ok(nombre,'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA PELICULA. REVISA')
        return

    def read_a_pelicula(self):
        self.view.ask('ID pelicula: ')
        id_pelicula = input()
        pelicula = self.model.read_a_pelicula(id_pelicula)
        if type(pelicula) == tuple:
            self.view.show_pelicula_header(' Datos de la pelicula '+id_pelicula+' ')
            self.view.show_a_pelicula(pelicula)
            self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA')
        return

    def read_all_peliculas(self):
        peliculas = self.model.read_all_pelicula()
        if type(peliculas) == list:
            self.view.show_pelicula_header(' Todas las peliculas ') 
            for pelicula in peliculas:
                self.view.show_a_pelicula(pelicula)
                self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA')
        return

    def read_peliculas_categoria(self):
        self.view.ask('Categoria: ')
        categoria = input()
        peliculas = self.model.read_pelicula_categoria(categoria)
        if type(peliculas) == list:
            self.view.show_pelicula_header(' Peliculas categoria '+categoria+' ')
            for pelicula in peliculas:
                self.view.show_a_pelicula(pelicula)
                self.view.show_pelicula_midder()
            self.view.show_pelicula_footer
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA')
        return


    def update_pelicula(self):
        self.view.ask('ID de pelicula a modificar: ')
        id_pelicula = input()
        pelicula = self.model.read_a_pelicula(id_pelicula)    
        if type(pelicula) == tuple:
            self.view.show_pelicula_header(' Datos de la pelicula '+id_pelicula+' ')
            self.view.show_a_pelicula(pelicula)
            self.view.show_pelicula_midder()
            self.view.show_pelicula_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_pelicula()
        fields, vals = self.update_lists(['Nombre', 'Sinopsis', 'Categoria', 'Duracion'], whole_vals)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.update_pelicula(fields,vals)
        if out == True:
            self.view.ok(id_pelicula, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA PELICULA. REVISA')
        return  


    def delete_pelicula(self):
        self.view.ask('Id de la pelicula a borrar: ')
        id_pelicula = input()
        count = self.model.delete_pelicula(id_pelicula)
        if count != 0:
            self.view.ok(id_pelicula, 'borro')
        else:
            if count == 0:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA PELICULA. REVISA.')
        return
    
    """
    *********************************
    *   Controllers for salas       *
    *********************************
    """

    def administrador_salas(self):
        o = '0'
        while o != '8':
            self.view.sala_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.agregar_sala()
            elif o == '2':
                self.read_a_sala()
            elif o == '3':
                self.read_all_salas()
            elif o == '4':
                self.update_sala()
            elif o == '5':
                self.agregar_asientos_sala()
            elif o == '6':
                self.eliminar_asientos_sala()
            elif o == '7':
                self.delete_sala()
            elif o == '8':
                self.administrador_menu()
                return
            else:
                self.view.not_valid_option()
        return

    def ask_sala(self):
        self.view.ask('Nombre: ')
        nombre = input()
        return [nombre]

    def agregar_sala(self):
        nombre = self.ask_sala()
        out = self.model.agregar_sala(nombre)
        if out == True:
            self.view.ok(nombre,'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA SALA. REVISA')
        return

    def read_a_sala(self):
        self.view.ask('ID sala: ')
        id_sala = input()
        sala = self.model.read_a_sala(id_sala)
        if type(sala) == tuple:
            self.view.show_sala_header(' Datos de la sala '+id_sala+' ')
            self.view.show_a_sala(sala)
            self.read_all_asientos(id_sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if sala == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA SALA. REVISA')
        return

    def read_all_salas(self):
        salas = self.model.read_all_salas()
        if type(salas) == list:
            self.view.show_sala_header(' Todas las salas ') 
            for sala in salas:
                self.view.show_sala_header('Sala '+str(sala[0])) 
                self.view.show_a_sala(sala)
                self.read_all_asientos(sala[0])
                self.view.show_sala_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA')
        return

    def read_all_asientos(self,id_sala):
        asientos = self.model.read_asientos_sala(id_sala)
        if type(asientos) == list:
            if len(asientos) == 0:
                print('Aun no se egregan asientos')
                self.view.show_asiento_footer()
            else:
                self.view.show_asiento_header(' Asientos sala '+str(id_sala))
                for asiento in asientos:
                    self.view.show_a_asiento(asiento)
                self.view.show_asiento_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ASIENTOS')
        return

    def read_asientos(self,asientos):
        if type(asientos) == list:
            self.view.show_asiento_header('Asientos Disponibles')
            for asiento in asientos:
                self.view.show_a_asiento(asiento)
            self.view.show_asiento_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ASIENTOS')
        return

    def agregar_asientos_sala(self):
        self.read_all_salas()
        self.view.ask('ID de la sala: ')
        id_sala = input()
        self.view.ask('Cuantos asientos desea agregar? ')
        no_asientos = input()
        for a in range (0,int(no_asientos)):
            self.view.ask('Nombre del asiento: ')
            nombre = input()
            out = self.model.agregar_asiento(id_sala, nombre)
            if out == True:
                self.view.ok(nombre,'agrego')
            else:
                self.view.error('NO SE PUDO AGREGAR EL ASIENTO. REVISA')
        return


    def ask_sala(self):
        self.view.ask('Nombre: ')
        nombre = input()
        return [nombre]

    def update_sala(self):
        self.view.ask('ID de la sala a modificar: ')
        id_sala = input()
        sala = self.model.read_a_sala(id_sala)    
        if type(sala) == tuple:
            self.view.show_sala_header(' Datos de la sala '+id_sala+' ')
            self.view.show_a_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if sala == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA SALA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_sala()
        fields, vals = self.update_lists(['nombre_sala'], whole_vals)
        vals.append(id_sala)
        vals = tuple(vals)
        out = self.model.update_sala(fields,vals)
        if out == True:
            self.view.ok(id_sala, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA SALA. REVISA')
        return  

    def eliminar_asientos_sala(self):
        self.view.ask('Id de la sala: ')
        id_sala = input()
        self.view.ask('ID del asiento: ')
        id_asiento = input()
        count = self.model.delete_asientos(id_sala, id_asiento)
        if count != 0:
            self.view.ok(id_asiento, 'borro')
        else:
            if count == 0:
                self.view.error('El ASIENTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL ASIENTO')
        return

    def delete_sala(self):
        self.view.ask('ID de la sala: ')
        id_sala = input()
        count = self.model.delete_sala(id_sala)
        if count != 0:
            self.view.ok(id_sala, 'borro')
        else:
            if count == 0:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA SALA')
        return

    """
    *********************************
    *   Controllers for Funciones   *
    *********************************
    """
    def usuario_funciones(self):
        o = '0'
        while o != '3':
            self.view.menu_funciones_usuario()
            self.view.option('3')
            o = input()
            if o == '1':
                self.read_all_funciones()
            elif o == '2':
                self.read_funciones_pelicula()
            elif o == '3':
                self.menu_usuario()
                return
            else:
                self.view.not_valid_option()
        return

    def administrador_funciones(self):
        o = '0'
        while o != '7':
            self.view.funciones_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.agregar_funciones()
            elif o == '2':
                self.read_a_funcion()
            elif o == '3':
                self.read_all_funciones()
            elif o == '4':
                self.read_funciones_pelicula()
            elif o == '5':
                self.update_funcion()
            elif o == '6':
                self.delete_funcion()
            elif o == '7':
                self.administrador_menu()
                return
            else:
                self.view.not_valid_option()
        return

    def ask_funcion(self):
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        self.view.ask('ID_sala: ')
        id_sala = input()
        self.view.ask('Fecha: ')
        fecha = input()
        self.view.ask('Hora: ')
        hora = input()
        self.view.ask('Precio: ')
        precio = input()
        self.view.ask('Idioma: ')
        idioma = input()
      
        return [id_pelicula, id_sala, fecha, hora, precio, idioma]


    def agregar_funciones(self):
        id_pelicula, id_sala, fecha, hora, precio, idioma = self.ask_funcion()
        out = self.model.agregar_funcion(id_pelicula, id_sala, fecha, hora, precio, idioma)
        if out == True:
            self.view.ok(fecha,'Funcion agregada')
        else:
            self.view.error('NO SE PUDO AGREGAR LA FUNCION. REVISA')
        return

    def read_a_funcion(self):
        self.view.ask('ID funcion: ')
        id_funcion = input()
        funcion = self.model.read_a_funcion(id_funcion)
        if type(funcion) == tuple:
            self.view.show_funcion_header(' Datos de la funcion '+id_funcion+' ')
            self.view.show_a_funcion(funcion)
            self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            if funcion == None:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA FUNCION')
        return
    
    def read_funcion(self,id_funcion):
        funcion = self.model.read_a_funcion(id_funcion)
        if type(funcion) == tuple:
            self.view.show_funcion_header(' Datos de la funcion '+id_funcion+' ')
            self.view.show_a_funcion(funcion)
            self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            if funcion == None:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA FUNCION')
        return
    
    def read_all_funciones(self):
        funciones = self.model.read_all_funciones()
        if type(funciones) == list:
            self.view.show_funcion_header(' Todas las funciones ')
            for funcion in funciones:
                self.view.show_a_funcion(funcion)
                self.view.show_funcion_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA')
        return

    def read_funciones_pelicula(self):
        self.view.ask('Nombre Pelicula: ')
        n_pelicula = input()
        funciones = self.model.read_funcion_pelicula(n_pelicula)
        if type(funciones) == list:
            self.view.show_funcion_header(' Funciones para pelicula '+n_pelicula+' ')
            for funcion in funciones:
                self.view.show_a_funcion(funcion)
                self.view.show_funcion_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA')
        return

    def update_funcion(self):
        self.view.ask('ID de funcion a modificar: ')
        id_funcion = input()
        funcion = self.model.read_a_funcion(id_funcion)    
        if type(funcion) == tuple:
            self.view.show_funcion_header(' Datos de la funcion '+id_funcion+' ')
            self.view.show_a_funcion(funcion)
            self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            if funcion == None:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA FUNCION')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_funcion()
        fields, vals = self.update_lists(['id_pelicula', 'id_sala', 'fecha', 'hora', 'precio', 'idioma'], whole_vals)
        vals.append(id_funcion)
        vals = tuple(vals)
        out = self.model.update_funcion(fields,vals)
        if out == True:
            self.view.ok(id_funcion, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA FUNCION. REVISA')
        return

    def delete_funcion(self):
        self.view.ask('ID de la FUNCION: ')
        id_funcion = input()
        count = self.model.delete_funcion(id_funcion)
        if count != 0:
            self.view.ok(id_funcion, 'borro')
        else:
            if count == 0:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA FUNCION')
        return


    """
    *********************************
    *   Controllers for BOLETOS     *
    *********************************
    """
    def usuario_boletos(self):
        o = '0'
        while o != '2':
            self.view.boletos_menu_usuario()
            self.view.option('2')
            o = input()
            if o == '1':
                self.agregar_boleto()
            elif o == '2':
                self.menu_usuario()
                return
            else:
                self.view.not_valid_option()
        return

    def administrador_boletos(self):
        o = '0'
        while o != '6':
            self.view.boleto_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.agregar_boleto()
            elif o == '2':
                self.read_a_boleto()
            elif o == '3':
                self.read_all_boletos()
            elif o == '4':
                self.read_boletos_funcion()
            elif o == '5':
                self.delete_funcion()
            elif o == '6':
                self.administrador_menu()
                return
            else:
                self.view.not_valid_option()
        return

    def ask_boleto(self):
        self.view.ask('ID Funcion: ')
        id_funcion = input()
        self.view.ask('ID_asiento: ')
        id_asiento = input()
      
        return [id_funcion, id_asiento]


    def agregar_boleto(self):
        self.read_all_funciones()
        self.view.ask('ID_FUNCION: ')
        id_funcion = input()
        funcion=self.model.read_a_funcion(id_funcion)
        asientos = self.model.read_asientos_sala(funcion[2])
        ocupados = self.model.asientos_funcion(id_funcion)
        desocupados = [a for a in asientos if not a in ocupados]
        self.read_asientos(desocupados)
        self.view.ask('ID_ASIENTO: ')
        id_asiento = input()
        des = []
        for i in desocupados:
            des.append(str(i[0]))
        if id_asiento in des:
            out = self.model.agregar_boleto(id_funcion, id_asiento)
            if out == True:
                self.view.ok(id_asiento,'agregado')
            else:
                self.view.error('NO SE PUDO AGREGAR EL BOLETO')
        else:
            self.view.error('ERROR AL SELECCIONAR ASIENTO')
        return


    def read_a_boleto(self):
        self.view.ask('ID Boleto: ')
        id_boleto = input()
        boleto = self.model.read_a_boleto(id_boleto)
        if type(boleto) == tuple:
            self.view.show_boleto_footer()
            self.view.show_boleto_header(' Datos de la boleto '+id_boleto+' ')
            self.view.show_boleto_footer()
            self.view.show_boleto(boleto)
            self.view.show_boleto_footer()
        else:
            if boleto == None:
                self.view.error('EL BOLETO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL BOLETO')
        return
    
    def read_all_boletos(self):
        boletos = self.model.read_all_boletos()
        if type(boletos) == list:
            self.view.show_funcion_header(' Todos los boletos ')
            for boleto in boletos:
                self.view.show_boleto(boleto)
                self.view.show_boleto_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA')
        return

    def read_boletos_funcion(self):
        self.read_all_funciones()
        self.view.ask('ID FUNCION: ')
        id_funcion = input()
        boletos = self.model.read_boletos_funcion(id_funcion)
        if type(boletos) == list:
            self.view.show_funcion_header(' Boletos de la funcion '+id_funcion+' ')
            for boleto in boletos:
                self.view.show_boleto(boleto)
                self.view.show_boleto_midder()
            self.view.show_pelicula_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS BOLETOS')
        return

    def delete_boleto(self):
        self.view.ask('ID del BOLETO: ')
        id_boleto = input()
        count = self.model.delete_boleto(id_boleto)
        if count != 0:
            self.view.ok(id_boleto, 'se borro')
        else:
            if count == 0:
                self.view.error('EL BOLETO NO EXISE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL BOLETO')
        return


    """
    *********************************
    *   Controllers for ADMINS      *
    *********************************
    """
    def administrador_admins(self):
        o = '0'
        while o != '6':
            self.view.admin_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.agregar_administrador()
            elif o == '2':
                self.read_a_administrador()
            elif o == '3':
                self.read_all_administradores()
            elif o == '4':
                self.update_administrador()
            elif o == '5':
                self.delete_administrador()
            elif o == '6':
                self.administrador_menu()
                return
            else:
                self.view.not_valid_option()
        return

    def ask_admin(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido_P: ')
        apellido_p = input()
        self.view.ask('Apellido_M: ')
        apellido_m = input()
        self.view.ask('Usuario: ')
        usuario = input()
        self.view.ask('Contraseña: ')
        contraseña = input()
      
        return [nombre, apellido_p, apellido_m, usuario, contraseña]
    
    def agregar_administrador(self):
        nombre, apellido_p, apellido_m, usuario, contraseña = self.ask_admin()
        out = self.model.agregar_administrador(nombre, apellido_p, apellido_m, usuario, contraseña)
        if out == True:
            self.view.ok(nombre,'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL ADMINISTRADOR. REVISA')
        return

    def read_a_administrador(self):
        self.view.ask('ID ADMIN: ')
        id_admin = input()
        admin = self.model.read_administrador(id_admin)
        if type(admin) == tuple:
            self.view.show_admin_header(' Datos del Admin '+id_admin+' ')
            self.view.show_a_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ADMIN. REVISA')
        return

    def read_all_administradores(self):
        admins = self.model.read_all_administradores()
        if type(admins) == list:
            self.view.show_admin_header(' Todos los administradores ') 
            for admin in admins:
                self.view.show_a_admin(admin)
                self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ADMINISTRADORES. REVISA')
        return

    def update_administrador(self):
        self.view.ask('ID del administrador a modificar: ')
        id_admin = input()
        admin = self.model.read_administrador(id_admin)    
        if type(admin) == tuple:
            self.view.show_admin_header(' Datos del admin '+id_admin+' ')
            self.view.show_a_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ADMIN')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_admin()
        fields, vals = self.update_lists(['nombre', 'apellido_p', 'apellido_m', 'usuario', 'contraseñna'], whole_vals)
        vals.append(id_admin)
        vals = tuple(vals)
        out = self.model.update_administrador(fields,vals)
        if out == True:
            self.view.ok(id_admin, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL ADMINISTRADOR. REVISA')
        return

    def delete_administrador(self):
        self.view.ask('ID del ADMIN: ')
        id_admin = input()
        count = self.model.delete_admin(id_admin)
        if count != 0:
            self.view.ok(id_admin, 'se borro')
        else:
            if count == 0:
                self.view.error('EL ADMINISTRADOR NO EXISE')
            else:
                self.view.error('PROBLEMA AL BORRAR')
        return

    def ask_login(self):
        self.view.ask('Usuario: ')
        usuario = input()
        self.view.ask('Contraseña: ')
        contraseña = input()
      
        return [usuario, contraseña]

    def login(self):
        self.view.login()
        usuario, contraseña = self.ask_login()
        login = self.model.admin_login(usuario,contraseña)
        if type(login) == tuple:
            self.view.show_admin_header(' BIENVENIDO '+login[0]+' ')
            self.view.show_admin_footer()
            self.administrador_menu()
        else:
            if login == None:
                self.view.error('CONTRASEÑA O USUARIO INCORRECTO')
            else:
                self.view.error('PROBLEMA AL INGRESAR')
        return