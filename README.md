# Módulo Biblioteca  para Odoo

Este es un módulo personalizado para Odoo que gestiona una biblioteca. Incluye tres modelos principales:
- **Biblioteca**: Gestiona bibliotecas con campos como nombre y capacidad.
- **Autor**: Gestiona autores con campos como nombre y nacionalidad.
- **Libro**: Gestiona libros con campos como título, fecha de publicación, precio, género, biblioteca asociada, y autores.

## Características
- Menús para acceder a Bibliotecas, Autores y Libros.
- Vistas árbol y formulario para cada modelo.
- Datos precargados con dos registros por modelo.

## Instalación
1. Copia el módulo a la carpeta de addons de Odoo si usas ubuntu tienes que usar el comando si estas en ubuntu:
   ´´´sh
   sudo cp -r moduloGFB /lib/python3/dis-packages/odoo/addons
   ´´´
   si estas en windows seria ir a la ruta de instalacion de odoo y pegar en ese sitio la carpeta con los archivos del modulo.
3. Actualiza la lista de aplicaciones en Odoo: **Aplicaciones > Actualizar lista de aplicaciones**.
4. Busca `modulogfb` y haz clic en **Instalar**.
## Si el modulo ya lo tienes impotado y lo cambias
Los pasos son:
Ir a esta ruta en ubuntu
´´´sh
cd /lib/python3/dis-packages/odoo/addons
´´´
Luego eliminar de ahi el modulo en este caso moduloGFB con el comando:
´´´sh
sudo rm -r moduloGFB
´´´
Por ultimo ejecutar el comando
  ´´´sh
   sudo cp -r moduloGFB /lib/python3/dis-packages/odoo/addons
   ´´´
   este lo pega con los cambios que se hayan realizado para con los cambios se apliquen a nivel de servicio se ejecuta el comando
   ´´´sh
   sudo systemctl restart odoo
   ´´´
   luego en la interfaz grafica buscamos el modulo hacemos clic en los 3 puntos y le damos ha **informacion del modulo** si el codigo esta bien se llevara a cabo dicha actualizacion

## Problemas enfrentados
Durante el desarrollo, enfrenté varios errores, como:
- `ValueError: Wrong value for ir.ui.view.type: 'tree'`
- `ParseError: El nodo raíz de una vista list debe ser <list>, no <tree>`
- `UncaughtPromiseError: View types not defined tree found in act_window action 345`
- `ValueError: Wrong value for modulogfb.libro.genero: 'Novela'`

Estos errores se resolvieron ajustando las vistas, corrigiendo valores en campos `Selection`, y asegurándome de usar la ruta correcta del módulo.

## Autor
[Guillermo Fuentes Buenosvinos] - [(https://www.linkedin.com/in/guillermo-fuentes-buenosvinos/)]
