# Proyecto-Redes-Antivirus-
Software antivirus elaborado por Maria Orocú,José Quirós, Jonathan Castro y Pablo Castillo

Requerimentos para ejecutar correctamente este proyecto:


Python 3.9.0:
https://www.python.org/downloads/

Se puede utilizar cualquier ide desarrollo que utilice python y en este caso ejecute dicho lenguaje, nosotros para la utilizacion utilizamos IDLE, entorno de desarrollo de Python,IDLE el cual sus siglas significan Integrated DeveLopment Environment for Python es un entorno gráfico de desarrollo elemental que permite editar y ejecutar programas en Python
En Windows, IDLE se distribuye junto con el intérprete de Python, es decir, al instalar Python en Windows también se instala IDLE.
![image](https://user-images.githubusercontent.com/37676810/98873379-e3e56a00-243d-11eb-974f-b3c3957e79e3.png)



Para poder ejecutar un programa creado en IDLE, se puede ejecutar mediante la opción del menú Run > Run module, mediante este se puede abrir el proyecto creado.

![image](https://user-images.githubusercontent.com/37676810/98873452-0bd4cd80-243e-11eb-8c94-e21439c4dbfe.png)

Otra herramienta que dejamos a disposicion es pycharm, en el siguiente enlace esta disponible la opcion Community
https://www.jetbrains.com/es-es/pycharm/download/#section=windows

Como mencionamos en la descripcion el proposito de este proyecto es almacenar la firma de los archivos en el servidor, el cual las recibe desde un cliente que se encuentra registrado, Este cliente se encuentra almacenado en una base de datos Mysql creada por nosotros los desarrolladores, para su conexion desde python se necesita un driver que permita conectarse desde su computador, esto se puede realizar al digitar una linea de comando para que asi la computadora cuente con este driver y desde el proyecto solo importe su libreria.
python -m pip install pymysql

![image](https://user-images.githubusercontent.com/37676810/98874623-358ef400-2440-11eb-86a5-978a5bb8aa58.png)

En la imagen anterior se utiliza otra linea de comando, si la suministrada no llega a descargar el driver, favor utilizar la de la imagen.

Concluido todo esto, se tiene lo necesario para ejecutar el proyecto.
