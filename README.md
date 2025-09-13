# Sistema de Gestión de Libros
## Arquitectura del Proyecto

Este proyecto sigue una **arquitectura de monolito**, donde tanto el **frontend** como el **backend** residen en el mismo repositorio, lo que simplifica la configuración y el despliegue.

### Backend (Django & MySQL)

El **backend** está construido con el framework **Django** y utiliza **MySQL** como base de datos. Sus responsabilidades clave incluyen:

* **Manejo de Peticiones**: Recibe y procesa las peticiones HTTP desde el frontend.
* **Gestión de Datos**: Se comunica con la base de datos MySQL para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en los registros de libros.
* **Lógica de Negocio**: Implementa la validación de datos, la autenticación básica de usuarios y las reglas para manipular los libros.
* **Servicio de Datos**: Proporciona datos (a través de una API RESTful) o páginas HTML renderizadas que el frontend necesita para funcionar.

### Frontend (JavaScript)

El **frontend** está desarrollado con **JavaScript puro**, **HTML** y **CSS**. Su principal función es interactuar directamente con el usuario y consumir los servicios del backend. Sus responsabilidades incluyen:

* **Interfaz de Usuario**: Muestra la lista de libros, un formulario para agregar nuevos y controles para editar o eliminar.
* **Interactividad**: Responde a las acciones del usuario, como clics en botones o envío de formularios.
* **Comunicación con el Backend**: Realiza peticiones asíncronas (usando **Axios** o la **Fetch API**) al backend para obtener y manipular la información de los libros sin recargar la página.

## Librerías Utilizadas

* **Django REST Framework**: Una librería poderosa para construir APIs web RESTful.
* **mysqlclient**: Un paquete de Python que sirve como adaptador para que Django se conecte a MySQL.
* **HTML & CSS**: Utilizados para la estructura y el diseño visual de la interfaz.
* **Axios o Fetch API**: Herramientas para realizar peticiones HTTP al backend de manera eficiente.

### Tecnologías Utilizadas
* **Django**: Framework web de Python que facilita el desarrollo rápido y seguro.
* **MySQL**: Sistema de gestión de bases de datos relacionales, robusto y popular.
* **JavaScript**: El lenguaje de programación del lado del cliente para la interactividad.
