# SmartShower
Equipo: Carlos Torres, Martín Terrazas y Jair Zamorano 
Hoy en día una ducha promedio utiliza 8 litros de agua por minuto. Cuando la gente se ducha, en promedio 2-3 minutos son en esperar a que salga caliente. Así, en promedio, 16-24 litros de agua son desperdiciados, por falta de energía. Ahora bien, también es evidente que hay un problema al no poder tener presente cuánta agua se utiliza al momento de ducharse. Así, podemos crear una solución que:
disminuya el tiempo de agua desperdiciada por falta de energía y
Contabilice y dé a conocer al usuario cuánta agua se ha utilizado.
La solución sería una regadera conectada a una raspberry pi para que por medio de los siguientes dos sensores:
Sensor de flujo de agua  
Sensor de temperatura de agua
pueda crear dos salidas:
Foco Led que cambie de color/parpadee cada determinado consumo de agua, e.g., cada 10L.
Cantidad de energía que debe dirigirse a las resistencias para calentar el tubo. 
Así, la regadera funcionaría de la siguiente forma:
Se prende la regadera inteligente para que vayan calentando las resistencias;
Una vez llegada la temperatura requerida, puede abrirse la toma de agua;
El agua comienza fluyendo tibia y conforme el agua aumente su temperatura por el boiler, entonces las resistencias van a disminuir su potencia. 
Mientras el sujeto se baña puede ver cómo cambia de color el foco, para saber que ha utilizado x cantidad de agua.
Como este sistema requiere mucha energía para calentar agua, se nos ocurre que la regadera tenga un cable conectado a la toma de corriente del foco inteligente.  

Este proyecto cumple con el objetivo 12 de consumo responsable de desarrollo sostenible. 
