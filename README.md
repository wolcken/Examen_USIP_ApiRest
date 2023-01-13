# Examen_USIP_ApiRest

1.- Una vez clonado este repositorio, para que inicie sin ningun inconveniente, instalar desde la terminal CMD la siguiente linea de codigo "pip install virtualenv", aunque es lo mas problable que ya lo tenga instalado.

2.- El script para crear la Base de Datos esta en el archivo "Python_Flask_Postgres_API_REST.sql", es necesario tener creado la base de datos para continuar, en el archivo ".env" vienen los datos de conexion del VSCode a la BD en PostgresSQL en la cual debera modificar el PGSQL_PASSWORD y PGSQL_DATABASE con los parametros q vengan en su Postgres.

3.- En el proyecto existe un archivo "requirement.txt" donde vienen listado todos los paquetes que se han usado para este proyecto.

4.- Abrir el archivo app.py y abrir una terminal desde el VSCode y ejecutar "python .\src\app.py".

5.- Para comprobar el consumo del API REST, situese en la carpeta "utils" y abra el archivo "Query.rest", en el cual vienen los curls de ejemplo de los distintos endpoints, los cuales estan listados y con comentarios, para hacerlos correr, haga click en "Send Request" que viene en cada crul creado.

6.- 100/100