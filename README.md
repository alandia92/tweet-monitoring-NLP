# Tweet-monitoring-NLP
## PRUEBA TÉCNICA
### Caso de uso
Tenemos el caso de uso de un cliente (@TheBridge_Tech) que desea desarrollar una
monitorización de las redes sociales para medir el impacto de su marca y acciones
comerciales.
Tendrás que realizar las siguientes tareas:
1. Recopilar los tweets donde se mencione la cuenta de @TheBridge_Tech desde el
día que comenzaste el bootcamp (13 Febrero) hasta el último día de clase (22
Mayo). Se recomienda utilizar la API v2 de Twitter. Se deberá recoger:\
a. Id del mensaje\
b. Cuerpo del texto del mensaje\
c. Fecha del tweet\
d. Id del autor\
e. Nombre del autor\
f. Nombre de usuario del autor\
g. Métricas públicas del tweet (retweet, reply, like, quote)
2. Almacenarlos en una base de datos SQL no alojada en local en 2 tablas
normalizadas: (tweets, usuarios)
3. Realizar un pequeño análisis donde se respondan a las siguientes preguntas de
negocio:\
a. ¿Cuál es el tweet con mayor repercusión social?\
b. ¿Cuál es el usuario que más menciona a la escuela?\
c. ¿En qué mes se concentra el mayor número de tweets?\
d. ¿Qué palabras son más frecuentes?\
e. ¿Qué tipo de correlación matemática encuentras entre las métricas públicas?\
f. ¿Has sacado alguna conclusión extra en tu análisis?\
4. Utiliza el modelo pre entrenado que se te ha facilitado de análisis de sentimiento
para determinar el sentimiento de los tweets. Preguntas:\
a. ¿Cuáles son las predicciones? Interpreta los resultados.\
b. ¿Qué variables son las más importantes del modelo?\
c. ¿Cómo podrías mejorar el modelo?\
d. ¿Qué otras oportunidades se te ocurren donde se podrían aplicar otros\
modelos de ML?
5. Despliega el modelo pre entrenado a través de un endpoint utilizando una API.
