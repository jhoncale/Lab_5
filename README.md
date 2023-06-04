# Laboratorio #5
En la siguiente práctica de laboratorio se tuvo como objetivo principal determinar el modelo cinemático inverso del robot Phantom X para generar trayectorias a partir de este. De esta forma, que el robot Phantom X fuera capaz de realizar las trayectorias utilizando ROS.
### Herramienta. 


### Cinemática Inversa.
Se realizó la cinemática inversa del robot Phantom X que posee 4 GDL. Uno de los métodos que facilitan la elaboración de esta cinemática, es combinar el modelo geométrico con el desacople de la muñeca. Esto se hizo con el fin de determinar la conjuración articular del manipulador dada una determinada posición.


#### Metodología: 

1.	WorkSpace: para iniciar la generación de trayectorias deseadas, se ubicaron puntos en el rango de alcance del robot para definir sus arcos mínimos y máximos del workspace. Cabe resaltar que esta fue la trayectoria más sencilla de realizar debido a que el robot solo requiere mover una articulación, de tal manera que se facilitan en gran escala el proceso.

![image](https://github.com/jhoncale/Lab_5/assets/38961990/65e6b7e7-7fbf-4418-8593-bb00e708dc7e)
2.	Definición de trayectorias: una vez se tenía el espacio de trabajo en el que tiene alcance el efector final del robot, se dibujaron tres diferentes figuras: letra J con curvatura, un rectángulo, y una casa compuesta por un cuadrado en la parte inferior con un triángulo encima.
  
  
![image](https://github.com/jhoncale/Lab_5/assets/38961990/579051ca-70b6-41e7-9e31-2469451473f5)
![image](https://github.com/jhoncale/Lab_5/assets/38961990/8512a031-fca4-4341-a361-d2b2e9b2a66c)
![image](https://github.com/jhoncale/Lab_5/assets/38961990/e95200eb-e930-46fb-9989-319d689fd57b)
![image](https://github.com/jhoncale/Lab_5/assets/38961990/55b0d5ba-7d44-43ba-8974-0836b4a22675)

Y con ayuda de un flexómetro se tomó las coordenas x,y de varios puntos de las figuras realizadas. Para facilitar este proceso, en cuanto a las lineas rectas, se intentaron que fueran lo más paralelas posibles a la base (eje x o y) del robot phantomX. Esto pensando en que era más sencillo mantener la posición sobre una misma linea para evitar tener que mover más articulaciones del manipulador. 

3.	Manipulación de datos en Matlab: con los puntos previamente determinados de cada trayectoria, se realizó un script en Matlab el cual fuera capaz de entregar un vector de ángulos q = [theta1, theta2, theta3, theta4, theta5] dado una combinación de puntos (x,y). 

Cabe resaltar que, para el valor necesario de z, se utilizó un valor de 5 cm debido a la altura en la que iba a agarrar el griper al marcador. Así mismo, un valor determinado de 100 en theta5 para todo vector de ángulos.  

La razón por la que se decidió sacar vectores de ángulos en Matlab y luego pasarlos al script en Python que leería ROS, fue para seguir utilizando la interfaz realizada en el laboratorio 4, en donde ahora en vez de recibir solo un vector de posición, ahora recibirá una lista de vectores que leerá a través de un for, de tal manera que logre hacer la trayectoria de escritura realizada.
4.	Base porta herramientas: se utilizó la mitad de un rollo de cartón para sostener el marcador en su estado de reposo, esto pensado en que debía ser una base que fuera considerablemente alta para el alcance del efector final a la mitad del marcador.
![image](https://github.com/jhoncale/Lab_5/assets/38961990/953b49bb-3770-406b-ad4b-3e8b48362a6e)
5.	Rutinas de acercamiento agarre del marcador (cargada o descargada): para esto nuevamente fue necesario la toma de puntos, de tal manera que cuando se acercara totalmente a la base porta herramienta abriera o cerrara el griper según se necesitara. 

La generación de esta trayectoria se realizó con la toma de solo una vez los datos (cargada), y para la descarga, se manipularon los vectores de tal forma que el último fuera el primero y así sucesivamente (se cambió el orden), y así mismo, se hizo el cambio del ángulo del griper a 30 para que este fuera abierto. 

6.	Resultados de trayectorias: las trayectorias generadas por el robot no fueron totalmente lo esperado, en cuanto a la carga y descarga del marcador sí se obtuvo una eficacia de lo propuesto con lo obtenido, sin embargo, en cuanto a la escritura, se atribuye su inexactitud a las grandes distancias que se presentaron entre punto y punto, generando que el robot hiciera movimientos articulares inesperados. 

No obstante, la letra J sí fue dibujada con una línea recta y con la curvatura deseada, debido a que las distancias entre puntos fueron casi que mínimas. Es decir, los resultados obtenidos pueden ser arreglados si se toman más puntos en cada trayectoria, porque igualmente el robot pudo escribir en el lugar indicado y teniendo una similitud a las figuras propuestas en un principio. 

![image](https://github.com/jhoncale/Lab_5/assets/38961990/2cda73ee-9a90-4d5e-9b78-21423ad3a02b)
![image](https://github.com/jhoncale/Lab_5/assets/38961990/99d87ad5-0008-4e42-85e9-4caa359f65fe)
![image](https://github.com/jhoncale/Lab_5/assets/38961990/02d09c95-1b30-4fe7-81c8-b59f80234d7f)



#### Verificación trayectorias:.

Se ejecutó aproximadamente tres veces la misma rutina y siempre dibujaba en el mismo lugar, es decir el trazo realizado era exactamente el mismo, esto asociado a que el robot siempre tomaba el mismo valor de vector de ángulos dado la cinemática inversa. 
En cuanto a la precisión y calidad del trazo, como se mencionó anteriormente, la falta de distancias pequeñas entre puntos generó que no se tuviera ni precisión, ni calidad en el caso del rectángulo y en cierta parte de la casita. En el caso de la J, estas dos variables sí se cumplieron en una mayor proporción. 

![image](https://github.com/jhoncale/Lab_5/assets/38961990/5b45ac27-05bd-424e-b798-943d6d0a4a1c)
![image](https://github.com/jhoncale/Lab_5/assets/38961990/559ac8d7-2b00-4b14-8d66-440512cdf55d)



#### Videos
En cada uno de los videos es posible observar el cumplimiento de los objetivos planteados, donde en cada rutina el brazo se desplaza hacia la base porta herramientas, sujeta el marcador cerrando el griper y se ubica en la posición Home, posteriormente realiza su rutina de dibujo, regresa nuevamente a Home y se desplaza hacia la base para descargar el marcador abriendo el griper.


#### HMI:

Para la creación de esta HMI se utilizó como base la realizada en el laboratorio pasado que permitía seleccionar una rutina para ejecutar la cual tenía su imagen correspondiente, y la muestra de la posición actual de las articulaciones del brazo. 
  
  
![image](https://github.com/jhoncale/Lab_5/assets/38961990/114f4dba-da15-4e36-a0ff-a86d447831aa)

Se agregaron funciones como mostrar el tiempo de duración de cada una de las rutinas.
  
  
![image](https://github.com/jhoncale/Lab_5/assets/38961990/152748fe-884c-4852-8090-2ad265012cde)
  
  
El estado de la herramienta si estaba cargada o descargada (cuando el ángulo del griper cambiaba a 30°, la variable de estado cambiaba a descargada, y en 100° cambiaba a cargada).
  
  
![image](https://github.com/jhoncale/Lab_5/assets/38961990/4dfb62e2-1710-4d01-8074-94179fd0c7cf)
  
  
Mostrar la rutina seleccionada: cuando se oprimía un button de la HMI, se cambiaba el string de la variable rutina por el nombre del button (rutina) seleccionada.
  
  
![image](https://github.com/jhoncale/Lab_5/assets/38961990/ea44090b-30df-44a8-b5bb-c90a7269968c)
  
  
Indicación y control de parada de herramienta: esto se realizó de tal manera que cuando fuera presionado el button correspondiente, se cortara la comunicación entre el puerto serial y el brazo del robot. 
  
  
![image](https://github.com/jhoncale/Lab_5/assets/38961990/22933180-0a76-4547-8234-a221a8e32339)
  
  
Cuando tiene problemas para conectarse con el robot, salta la alarma: 
  
  
![errorConexc](https://github.com/jhoncale/Lab_5/assets/38961990/e244eb11-bfb8-4c62-80cb-a3e3117574d2)
  
  
HMI completa seleccionar rutina
  
  
![oprimir rutina](https://github.com/jhoncale/Lab_5/assets/38961990/18c8d4fc-41e9-4bd4-b2c3-2abe7df97f7b)

#### Videos:




https://github.com/jhoncale/Lab_5/assets/38961990/fcc5a4ca-4806-4eb5-a37d-ea6ae739963c



https://github.com/jhoncale/Lab_5/assets/38961990/64398c9a-bc95-4fe6-80b5-94cb01b2eade

cale/Lab_5/assets/38961990/4cb2cc6e-922b-4070-b016-47f3803471fd


https://github.com/jhoncale/Lab_5/assets/38961990/950a9430-1819-4812-99fb-3828e3bda8db




https://github.com/jhoncale/Lab_5/assets/38961990/89810ea1-6628-44c7-8a52-707254ae3d8a





https://github.com/jhoncale/Lab_5/assets/38961990/aac7cb60-8365-4ac9-91e5-a803ab8baf47

