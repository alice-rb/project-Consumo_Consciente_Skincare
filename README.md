'''
# CONSUMO CONSCIENTE DE 'SKINCARE'

## Descripción
Perfiles de consumidores y comportamiento de compra

Este proyecto analiza cómo distintos consumidores de productos de skincare toman decisiones de compra y cómo estos procesos de decisión se relacionan (o no) con su comportamiento de consumo, 
medido a través del gasto, la frecuencia de compra y la cantidad de productos utilizados. El objetivo central es distinguir entre la forma en que el consumidor toma la decisión (actitud) 
y la intensidad de consumo (comportamiento).
Hipótesis:
H1. Existen perfiles diferenciados en la toma de decisión de compra.
H2. Las diferencias actitudinales implican diferencias en la intensidad de consumo.
H3.  La preferencia de posicionamiento de marca se asocia con el perfil actitudinal del consumidor.

## Metodologia
El análisis se basa en datos procedentes de una encuesta online y combina técnicas de ETL, análisis exploratorio (EDA), reducción de dimensionalidad (PCA) y segmentación (clustering).

## Proceso de ETL
El archivo skincare-ETL.ipynb contiene todo el proceso de preparación de los datos. Este paso es clave para convertir las respuestas de la encuesta en variables analizables.

1️. Extracción de datos
        Los datos provienen de una encuesta creada con Google Forms
        Se cargan desde un archivo CSV 
        Se renombran las columnas para facilitar su uso en Python

2. Limpieza de datos
        Tratamiento de valores nulos (especialmente en variables condicionales)
        Mapeado de respuestas categóricas
        Eliminación de columnas no relevantes para el análisis

3. Creación de variables derivadas
   Para poder analizar el comportamiento de consumo y la toma de decisiones, se crean nuevas variables a partir de las respuestas originales.

   🔹 Variables de consumo (conductual) - Cuánto y cómo se consume
            - gasto_por_compra: conversión de rango categórico a punto medio numérico
            - compras_por_mes: transformación de la frecuencia de compra a escala mensual
            - gasto_mensual_avg: gasto mensual estimado [gasto_por_compra * compra_por_mes]
            - freq_score: frecuencia de compra en escala ordinal
            - cant_productos_uso: número de productos usados a diario

   🔹 Variables de decisión de compra (actitudinal) - Cómo decide el consumidor. Al ser la base del PCA, se han convertido a valores ordinales en la ETL
            - inci_score: lectura del INCI (Nunca / A veces / Siempre)
            - medios_score: uso de medios para informarse
            - calificacion_informado: autopercepción de conocimiento (1–5)
            - ingredientes, precio, marca, packaging, reviews, viral: importancia de cada criterio (1–5)
            - certificaciones: peso de certificaciones
            - eco_score: percepción de claims eco/natural
            - influ_score: compra influenciada por influencers (0/1)

   🔹 Variables sociodemográficas (contextual) 
            - Edad --> transformada a rango_edad
            - Sexo
            - estudios
            - ciudad --> transformada a bcn_s_n
            - lugar_compra 
            - perfil (tipo de marca preferida: dermo, lujo, natural, trendy)

4. Guardado de datos
            Los dataframes limpios se guardan en formato pickle para facilitar su reutilización.

## DataFrames principales
A lo largo del proyecto se trabajan varios dataframes, cada uno con un objetivo concreto:

🔹 df (completo)
DataFrame base tras la limpieza
Contiene todas las variables originales y derivadas

🔹 consumo
DF centrado en variables de comportamiento de consumo
Usado para EDA de gasto, frecuencia y productos

🔹 pca
Contiene los componentes principales (PC1, PC2, PC3)
Incluye la asignación de cluster a cada id

🔹 clusters
DataFrame final para análisis por perfiles
- perfil de cluster
- variables de decisión
- variables de consumo

Existen, además, otros dataframes con las variables organizadas para mejor manejo a la hora de realizar los análisis y las visualizaciones: usuarios, influencia, informado.
Se ha realizado también la creación de dos tablas puente con dimensiones para las variables con contenido múltiple.

## PCA y segmentación de consumidores
El archivo skincare-PCA_cluster.ipynb contiene el análisis principal del proyecto.

  1. PCA (Análisis de Componentes Principales)
    Se aplica PCA únicamente sobre variables de decisión de compra, con el objetivo de:
        Reducir dimensionalidad
        Identificar ejes latentes de decisión
        Interpretación de componentes (total acumulado = 53%):
        - PC1 (27%) – Implicación informada: peso en ingredientes, certificaciones, INCI y reviews
        - PC2 (17%) – Técnico vs Marketing: Lados extremos entre argumentos técnicos y factores de viralidad
        - PC3 (10%) – Influencia digital: Peso en influencers y exposición en redes

  2. Clustering
    El clustering se aplica sobre los tres ejes identificados en el PCA.
    Se identifican tres perfiles actitudinales principales:
    - Pragmático: decisión funcional y poco informada
    - Informado: decisión analítica con mucha atención a ingredientes y certificacioes
    - Alta exigencia: decisión compleja que combina calidad, reputación y coherencia

## Análisis exploratorio y resultados
Se utilizan gráficos para explorar distribuciones generales y comparar el comportamiento entre perfiles, así como ayudar a visualizar la segmentación.
Principales gráficos:
- Distribución de gasto mensual
- Frecuencia de compra
- Cantidad de productos usados
- Scatter PC1 vs PC2 con perfiles
- Heatmap de gasto y frecuencia por perfil
- Heatmap de pesos del PCA
- Barplot agrupado de posicionamiento de marca por perfil

## Conclusión
El proyecto distingue de forma explícita entre variables de decisión (cómo se compra) y variables de consumo (cuánto se compra).  
Esta separación permite mostrar que existen perfiles claros de decisión de compra, y que estas diferencias actitudinales no se traducen necesariamente en diferencias significativas en la intensidad de consumo.
Sin embargo, sí se observa una asociación entre los perfiles de decisión y el posicionamiento de marca preferido. Cada perfil muestra patrones distintos de preferencia, lo que indica que la estructura de decisión influye en qué tipo de marca se elige, aunque no determine cuánto se consume.
En conjunto, los resultados sugieren que el consumo en skincare se mantiene relativamente estable entre perfiles, mientras que las actitudes influyen principalmente en la forma en que se decide y en el posicionamiento de marca elegido.

'''
