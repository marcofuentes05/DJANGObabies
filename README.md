# DJANGO Babies


<h2 align = "center"> Laboratorio No. 4 </h2>
<h2 align = "center"> Marco Fuentes - 18188 </h2>

## Para poder usar

Seguir estos comandos en terminal de linux (si usa windows puede cambiar)
```bash
$ python3 -m venv venv #Crear entorno virtual

$ source venv/bin/activate # Iniciar entorno virtual

$ (venv) cd babies

$ pip3 install -r requirements.txt #Instalar las dependencias

$ python3 manage.py runserver 8000
```

## Para probar el API rest

### Login

En postman (u otros software similar), hacer un _request_ de tipo POST a este URL: 
```localhost:8000/api-auth ```
con un body así: 
```JSON
username: Marco
password: 12345678
```
- O sea, el usuario con _username_ 'Marco' y con _password_ '12345678'
Este _request_ retornará un JSON de la forma 
```JSON
"token": {'el-token-aqui'}
```

Este token debe ir como _Header_ de los próximos requests. De lo contrario, el API retornará ```"Authentication credentials were not provided"```


### Funcionalidades con _request_ de tipo GET

```Marco``` es el único que existe en el sistema, tiene un ```id``` de 1  y tiene como hijos a los ```baby``` con _id_ 's 1,4,5, y 6.

- ``` localhost:8000/api/v1/parent/1/babies``` le enseña los bebés del usuario
- ``` localhost:8000/api/v1/baby/1 ``` le enseña los datos del ```baby``` con id 1. Como éste si es hijo del usuario, le muestra los datos, si prueba con un id de, por ejemplo, 2, retornará ```You do not have permission to perform this action```
- ``` localhost:8000/api/v1/baby/1/events ``` retorna los eventos del ```baby``` con id 1. Igualmente, verifica permisos.

### Funcionalidades con _request_ de tipo POST

Además de agregar el token como _header_ del _request_, estas funciones necesitan de un _body_
- ```localhost:8000/api/v1/events/``` crea un evento, y necesita un _body_ de tipo:
```JSON
etype: El tipo de evento
comment: Algun comentario del evento
bid: 1 (el id el bebe que hizo el evento)
```


- ``` localhost:8000/api/v1/baby/ ``` crea un ```baby```, y necesita un _body_ de tipo: 
```JSON

name: Juanito (nombre del bebe) 
pid: 1 (el id del papa)

 ```