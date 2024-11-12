## Metodos (Back):

- Conexiones de la Demanda:
- - entre demandas, nnyas, personas, etc ...
- - buscador
- - Chequear demandas con mismo DNI y relacionar (**Background automation**)
- Devolver estado constatación: si / no / *consultar opciones posibles*
- Enviar respuesta: Implementar mail service
- Sumatoria de Pesos: 
- - Se genera una sumatoria de los pesos de cada uno de los sub-tipos por cada vulneración, para tener una referencia de la gravedad de cada vulneración
- - A su vez, se genera una sumatoria de pesos de las vulneraciones asociada a una demanda, lo que sería el **score** . -->
- - Al momento de evaluar, se suman los pesos según la selección de cada sub-tipo de las evaluaciones, generando así también, un score de la evaluación, que se suma al score de la demanda. En el sheets, son los *indicadores de valoración de Amenaza/Vulneración de Derechos* . Va a haber muchos indicadores generables desde el admin, que por una tabla intermedia entre la evaluación y cada indicador, se lo va poder marcar como true/false, sumando o no de esa manera su peso asociado. Hay que hacer una *composite-key* o algo similar que  valide la *unicidad* entre esa selección y la evaluación
- Sugerencia de apertura según el score


## Validaciones (Back):
- NNyA principal no puede estar como principal en otra Demanda
- Validar que el NNyA de la vulneración principal, sea también el NNyA principal de la Demanda
- Validar en Demanda_Persona:  autordv y nnya_principal no pueden ser true simultaneamente, validar unico nnya_principal, validar unico autordv_principal
- Validar que haya una única vulneración principal por demanda
- Validar que el nnya de la vulneración tenga relación con la demanda así como también el autordv con la demanda
- Validar que T_MOTIVO_VULNERACION_DDV seleccionado pertenezca al mismo T_DDV seleccionado (es decir ingresado)
- Validar que la evaluación sea realizable solo si los *indicadores de valoración de Amenaza/Vulneración de Derechos respecto la demanda* seleccionada fueron respondidos