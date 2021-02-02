En la carpeta working_folder tenemos 3 scripts que podemos ejecutar por consola

1. lectura_api.py --> Obtiene mediante la conexion a la api 'https://www.metaweather.com' la previsión (consolidated_weather) a 5 días para las ciudades seleccionadas, que en mi caso son: Madrid, San Francisco y New York

2. lectura_api_2.py --> Obtiene para un rango de fechas entre fecha_inicio y fecha_fin las previsiones realizadas para esos días en los días y horas previos... mismos campos que consolidated_weather de antes
			En este caso podemos elegir una fecha_inicio y una fecha_fin que se le pasan como parámetros en la llamada al .py desde la consola, tal que: ~$python lectura_api_2.py fecha_inicio fecha_fin, donde 
			fecha_inicio y fecha_fin tienen que tener el formato yyyy/mm/dd
			Si no se indican fechas, tomará por defecto 5 días entre el 1 y el 5 de Diciembre de 2020
			Estos datos obtenidos mediante la conexion request.get a la api son almacenados en 3 ficheros .csv con el nombre cada uno de la ciudad para la que se han obtenido esos datos en el working_folder

3. escritura_bbdd --> Toma los 3 ficheros .csv almacenados anteriormente en el working_folder y los sube como documentos (diccionarios) a una bbdd MongoDB Atlas llamada weather_db y creada por mí, con mi usuario y password
		  	proporcionados en el propio script

En la carpeta app dentro de la carpeta working_folder se encuentra el script:

1. api_weather.py --> se puede ejecutar desde consola ~$python api_weather.py lo que dejará ejecutando un proceso flask que nos va a servir en nuestro localhost los datos almacenados anteriormente en nuestra bbdd MongoDB Atlas
			Con ese proceso en ejecución abrir un navegador y poner: 
				
					"http://localhost/api/v1/weather/<ciudad>" donde ciudad puede ser Madrid, San_Francisco o New_York
				
			Y nos saldrá el resultado requerido... también podemos hacer desde python una llamada GET:

					"request.get("http://localhost/api/v1/weather/<ciudad>")", donde ciudad puede ser Madrid, San_Francisco o New_York


