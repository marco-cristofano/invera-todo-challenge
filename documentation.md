### Instalación

##### Requerimientos:

- Docker (y docker-compose)

##### Versiones principales
- Python: 3.13
- Django: 5.2 (LTS)

#### Infraestructura

La infraestructura es muy simple, consta del servidor backend y de la BDD Postgres. No lo quise complejizar de más añadiendo un servidor nginx pero debería si se quiere desplegar en un entorno productivo.

##### Guía
1. Acceder a la carpeta docker y ejecutar:
   ```bash
   cd docker
   ```
2. Ejecutar:
   ```bash
   docker-compose up --build
   ```
   Se levantarán dos contenedores, uno con la BDD Postgres y el restante con el propio backend desarrollado en python (puerto 8001).

    Si es la primera vez que se levanta puede suceder que la BDD tarde mas en desplegarse que el backend y arroje error. En ese caso, volver a ejecutar el comando *docker-compose --build*

3. Para ejecutar test:
   ```bash
   docker exec -it todochallenge_backend bash
   cd todochallenge
   python manage test --parallel
   ```

#### Consideraciones

- La acción de completar una tarea (tasks/{PK}/completed) podría desarrollarse utilzando PATCH o PUT. La decisión del POST es arbitraria.
- No permitir en la creación y actualización la elección del usuario tambien fue una desición arbitraria. Podría hasta ser controversial considerando que si es posible actualizar, borrar o completar una tarea ajena. 

