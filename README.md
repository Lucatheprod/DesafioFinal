# Proyecto 'ThatBeer' - Estigarribia, Scardaccione, Peña Machado

## Introducción:
1 - El usuario ingresa al HOME (/AppThatBeer)

2 - En la parte superior se encuentra la barra de navegación, donde puede elegir a qué sección del sitio dirigirse (Vistas: HOME / PRODUCTOS / DISTRIBUIDORES / CLIENTES / PATROCINADORES / NOTICIAS / SOBRE NOSOTROS)

3 - Puede desplazarse por todo el Home, donde tendrá primero nuestro Slogan y un botón para conocer los productos, que dirigirá a la vista de PRODUCTOS, al igual que el botón de la barra de navegación.

4 - Luego se presenta la sección de noticias con un botón (que de momento se encuentra desactivado) para conocer la variedad de la cerveza ganadora, asi como también un botón que dirige a la sección de NOTICIAS.

5- Se presenta parte de las características que distinguen a la empresa de las demás, y un botón “CONOCÉ MÁS” que dirige hacia la sección SOBRE NOSOTROS al igual que la barra de navegación.

6- Luego presenta nuestros patrocinadores, y un pequeño formulario para un sorteo a conocer nuestra fábrica.

7- Al final del HOME, podemos ver un link para unirse a nuestro canal de Discord.

8- Adicionalmente en la url '/admin' se encuentra la base de datos de todas las clases (ver info superuser en archivo 'admin.txt')

## Funcionalidades

#### AGREGAR / CREAR:
El usuario tiene la posibilidad de insertar datos a las clases de los models (PRODUCTOS / CLIENTES / DISTRIBUIDORES / PATROCINADORES)

Dichos formularios se encuentran en sus propias vistas, a las cuales podemos acceder desde el HTML de su clase. Por ejemplo:

Para agregar un producto, ingresamos a la vista de PRODUCTOS, y clickeamos donde dice “AGREGAR PRODUCTO”. Esta acción nos dirigirá a la vista AGREGAR PRODUCTO, donde podremos realizar esta acción. 

#### BUSCAR:

Incluimos también la funcionalidad de BUSCAR PRODUCTOS (sólo aplicable a dicha clase) en la base de datos, según el atributo “VARIEDAD”. Para ello también en la vista de PRODUCTOS podemos hacerlo mediante el botón que nos dirigirá a la vista de BUSCAR PRODUCTOS.