# sistema gestión de libros Web
---
## Arquitectura del Proyecto
Este proyecto sigue una arquitectura monolítica donde todo el desarrollo (lógica del servidor y presentación de la interfaz de usuario) se realiza con Python y el framework Django. No se utiliza una capa de frontend separada con JavaScript para la lógica de la interfaz.

### Backend & Frontend (Django & Python)
Todo el proyecto reside en el backend de Django, que utiliza Python como su lenguaje principal y MySQL como base de datos. Sus responsabilidades clave incluyen:

* **Manejo de Peticiones:** Recibe y procesa las peticiones HTTP desde el navegador.

* **Gestión de Datos:** Se comunica con la base de datos MySQL para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

* **Lógica de Negocio:** Implementa la validación de datos, la autenticación de usuarios y las reglas para manipular los libros.

* **Renderización de Páginas:** Genera y envía directamente las páginas HTML renderizadas al navegador del usuario, combinando la lógica de Python con las plantillas HTML para mostrar la interfaz completa.

---

## Librerías Utilizadas
* **Django REST Framework:** Una librería para construir APIs web RESTful, si se requiere en el futuro.

* **mysqlclient:** Un paquete de Python que sirve como adaptador para que Django se conecte a MySQL.

* **HTML & CSS:** Utilizados para la estructura y el diseño visual de la interfaz que Django renderiza.

--- 

## Tecnologías Utilizadas
* **Django:** Framework web de Python que facilita el desarrollo rápido y seguro.

* **Python:** Lenguaje de programación del lado del servidor.

* **MySQL:** Sistema de gestión de bases de datos relacionales, robusto y popular.

---

## Arquitectura de la Base de Datos

Para entender la estructura de los datos del proyecto, puedes consultar los siguientes diagramas.

* [**Diagrama Entidad-Relación (E-R)**](https://lucid.app/lucidchart/4bc6c982-cf0e-4d66-b9e9-07d0cec2561d/edit?viewport_loc=204%2C188%2C1896%2C866%2C0_0&invitationId=inv_235a1c0f-5469-4f5a-9c74-a5c69b50a363)
* [**Diagrama Relacional**](https://miro.com/welcomeonboard/d3BpUXVlTm5ZUFFoUXJYaWRTOVd2RzV6SzJMSFhCL1FjNFNrQkNEMTBtejhkdHpUenN2SGNUZ1lsSzl0WnpzOTR1Ty9QanB2M0VRMEZFTXVOMGlBNlkxTG9nOGE0SlFqZ04yS1BrMGg3Q1A4S2txZDdQWkFKNThwMmh4SWt1dmh0R2lncW1vRmFBVnlLcVJzTmdFdlNRPT0hdjE=?share_link_id=594487681649)

---

## Funcionalidades Principales

* **Sistema de Autenticación:** Registro de nuevos usuarios y un sistema de inicio de sesión seguro.
* **Panel Administrativo:** Un panel restringido para administradores que muestra una lista completa de usuarios y sus préstamos.
* **Catálogo de Libros:** Los usuarios pueden ver una lista de todos los libros disponibles y los detalles de cada uno.
* **Base de Datos Relacional:** El proyecto está conectado a una base de datos MySQL para una gestión de datos eficiente y escalable.
