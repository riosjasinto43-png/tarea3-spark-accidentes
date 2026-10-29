# Tarea 3 - Procesamiento de Datos con Apache Spark

Análisis en batch del dataset **US Accidents** (muestra de 1 millón de registros) usando Apache Spark (PySpark) sobre Hadoop (HDFS).

## Problema
Entender cuándo, dónde y bajo qué condiciones ocurren los accidentes de tráfico en Estados Unidos: gravedad, año, estado, hora del día y clima.

## Archivos
- `tarea3_batch.py`: carga el CSV desde HDFS, limpia los datos (duplicados, nulos, severidad entre 1 y 4), crea columnas de año, mes, hora y día de la semana, guarda el resultado en Parquet y hace el análisis exploratorio (EDA).
- `graficos_batch.py`: genera 6 gráficos de barras (g1 a g6) con matplotlib a partir de los resultados del EDA.

## Requisitos
- Hadoop (HDFS) en ejecución
- Apache Spark 3.5.x con Python 3
- matplotlib

## Instrucciones de ejecución
1. Subir el CSV a HDFS:
