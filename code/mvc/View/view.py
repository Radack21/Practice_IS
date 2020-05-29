class View:
    """
    *************************
    * A view for a cine     *
    *************************
    """
    def start(self):
        print('=====================================')
        print('=   !Bienvenidos a nuesto cine!     =')
        print('=====================================')

    def end(self):
        print('=====================================')
        print('=         !Vuelva pronto !          =')
        print('=====================================')
        exit()

    def main_menu(self):
        print('****************************')
        print('*--    Menu Principal    --*')
        print('****************************')
        print('1. Usuario')
        print('2. Administrador')
        print('3. Salir')

    def main_menu_usuario(self):
        print('******************************')
        print('*-- Usuario Menu Principal --*')
        print('******************************')
        print('1. Peliculas')
        print('2. Funciones')
        print('3. Boletos')
        print('4. Salir')

    def main_menu_admin(self):
        print('******************************')
        print('*-- Admin Menu Principal   --*')
        print('******************************')
        print('1. Peliculas')
        print('2. Salas')
        print('3. Funciones')
        print('4. Boletos')
        print('5. Administradores')
        print('6. Salir')


    def option(self, last):
        print('Selecciona una opcion (1 - '+last+'): ', end = '')

    def not_valid_option(self):
        print('!Opcion no valida! \nIntenta de nuevo')

    def ask(self, output):
        print(output, end = '')
    
    def msg(self, output):
        print(output)

    def ok(self,id,op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ !'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' !ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    """
    ***************************
    * views for peliculas        *
    ***************************
    """      
    def pelicuas_menu_usuario(self):
        print('****************************')
        print('*--  Submenu Peliculas   --*')
        print('****************************')
        print('1. Mostrar todas los peliculas')
        print('2. Mostrar peliculas por categoria')
        print('3. Regresar')

    def peliculas_menu_admin(self):
        print('****************************')
        print('*--  Submenu Peliculas   --*')
        print('****************************')
        print('1. Agregar Pelicula')
        print('2. Mostar Pelicula')
        print('3. Mostrar todas las peliculas')
        print('4. Mostrar peliculas por categoria')
        print('5. Actualizar pelicula')
        print('6. Borrar pelicula')
        print('7. Regresar')

    def show_a_pelicula(self,record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Sinopsis: ', record[2])
        print('Categoria: ', record[3])
        print('Duracion: ', record[4])

    def show_pelicula_midder(self):
        print('-'*50)
        
    def show_pelicula_header(self, header):
        print(header.center(50, '*'))
        print('-'*50)

    def show_pelicula_footer(self):
        print('*'*50)

    """
    ***************************
    * views for salas     *
    ***************************
    """   

    def sala_menu(self):
        print('****************************')
        print('*--    Submenu Salas     --*')
        print('****************************')
        print('1. Agregar Sala')
        print('2. Ver sala especifica')
        print('3. Ver todas las salas')
        print('4. Editar nombre sala')
        print('5. Agrega asientos sala')
        print('6. Eliminar asientos sala')
        print('7. Eliminar sala')
        print('8. Regresar')

    def show_a_sala(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])

    def show_a_asiento(self, record):
        print('ID: {}  | Nombre: {}'.format(record[0],record[2]))
       

    def show_sala_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)

    def show_asiento_header(self, header):
        print(header.center(48,'*'))

    def show_sala_midder(self):
        print('-'*48)

    def show_sala_footer(self):
        print('*'*48)
        print('\n')

    def show_asiento_footer(self):
        print('*'*48)

    """
    ***************************
    * views for funciones     *
    ***************************
    """   

    def funciones_menu(self):
        print('****************************')
        print('*-- Submenu Funciones     --*')
        print('****************************')
        print('1. Agregar Funcion')
        print('2. Leer funcion')
        print('3. Leer todas las funciones')
        print('4. Leer funciones por pelicula')
        print('5. Actualizar funcion')
        print('6. Borrar funcion')
        print('7. Regresar')

    def menu_funciones_usuario(self):
        print('****************************')
        print('*-- Submenu Funciones     --*')
        print('****************************')
        print('1. Ver todas las funciones')
        print('2. Ver funciones por pelicula')
        print('3. Regresar')


    def show_a_funcion(self,record):
        print('ID Funcion: ', record[0])
        print('Pelicula: ', record[7])
        print('Sala: ', record[8])
        print('Fecha: ', record[3])
        print('Hora: ', record [4])
        print('Precio: $', record[5])
        print('Idioma: ',record[6])


    def show_funcion_header(self,header):
        print(header.center(53,'*'))
        print('-'*53)

    def show_funcion_midder(self):
        print('-'*53)

    def show_funcion_footer(self):
        print('*'*53)

    """
    ***************************
    * views for boletos       *
    ***************************
    """   

    def boletos_menu_usuario(self):
        print('****************************')
        print('*-- Submenu Boletos       --*')
        print('****************************')
        print('1. Comprar Boleto')
        print('2. Regresar')

    def boleto_menu(self):
        print('****************************')
        print('*-- Submenu Boletos      --*')
        print('****************************')
        print('1. Agregar Boleto')
        print('2. Leer boleto')
        print('3. Leer todos los boletos')
        print('4. Leer boletos por funcion')
        print('5. Borrar boletos')
        print('6. Regresar')

    def show_boleto(self,record):
        print('ID Boleto:', record[0])
        print('Pelicula', record[10])
        print('Sala: ', record[9])
        print('Fecha: ', record[4])
        print('Hora: ', record [5])
        print('Precio: $', record[6])
        print('Idioma: ',record[7])
        print('Asiento: ',record[8])
        

    def show_boleto_header(self,header):
        print(header.center(45,'+'))

    def show_boleto_midder(self):
        print('/'*45)

    def show_boleto_footer(self):
        print('+'*45)

    
    """
    ********************************
    * views for administradores    *
    ********************************
    """   

    def admin_menu(self):
        print('***********************************')
        print('*-- Submenu Administradores     --*')
        print('***********************************')
        print('1. Agregar Admin')
        print('2. Leer Admin')
        print('3. Leer todos los Admin')
        print('4. Actualizar Admin')
        print('5. Borrar Admin')
        print('6. Regresar')

    def show_a_admin(self,record):
        print('ID Admin: ', record[0])
        print('Apellido Paterno: ', record[1])
        print('Apellido Materno: ', record[2])
        print('Usuario: ', record[3])
        

    def show_admin_header(self,header):
        print(header.center(53,'*'))
        print('-'*53)

    def show_admin_midder(self):
        print('-'*53)

    def show_admin_footer(self):
        print('*'*53)

    def login(self):
        print('***********************************')
        print('*--   Login Administradores     --*')
        print('***********************************')
    
    def show_login_footer(self):
        print('*'*53)
