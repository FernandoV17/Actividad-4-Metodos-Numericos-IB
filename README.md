# Resolución de Ecuación Diferencial por Método de Euler

Este repositorio contiene un programa desarrollado como parte de la **PIA** del curso de Métodos Numéricos. El objetivo es resolver una ecuación diferencial ordinaria utilizando el **Método de Euler**, implementado en **Python**. El programa realiza cálculos iterativos y muestra los resultados paso a paso en consola, proporcionando una aproximación numérica a la solución de la ecuación diferencial.

## Ecuación Diferencial a Resolver

La ecuación diferencial planteada es:

\[
\frac{dw}{dx} = -0.02 \cdot w
\]

sujeta a la condición inicial:

\[
w(0) = 1000
\]

El programa calcula la solución aproximada en el intervalo \([0, 30]\) con un total de 100 iteraciones.

## Estructura del Código

El programa está organizado en las siguientes secciones:

1. **Encabezado del Programa:** Se imprime al inicio para describir el propósito del programa y los integrantes del equipo.
2. **Definición de Parámetros:** Incluye los valores iniciales de la ecuación diferencial, el intervalo \([a, b]\), el número de iteraciones \(N\), y la condición inicial \(w(0)\).
3. **Implementación del Método de Euler:** Una función que realiza la aproximación numérica utilizando la fórmula iterativa del método de Euler.
4. **Resultados Iterativos:** Se imprimen los valores aproximados de \(x\) y \(w(x)\) en cada iteración.

## Ejecución

### Requisitos

- **Python 3.x**
- Módulo estándar `math` (ya incluido en Python).

### Cómo ejecutar

1. Clona este repositorio:

   ```bash
   git clone https://github.com/FernandoV17/Actividad-4-Metodos-Numericos-IB.git
   cd Actividad-4-Metodos-Numericos-IB
   ```

2. Ejecuta el script principal:

```bash
python3 main.py
```

### Ejemplo de Salida

```bash
El programa imprimirá lo siguiente en consola:

##########################################################################

# PIA: Resolución de Ecuación Diferencial por método de Euler

##########################################################################

Métodos Numéricos: AD2024

Integrantes:
Fernando Villarreal Castillo 2049219
Julio Alejandro Galindo Estrada 1945686
Oscar Eduardo Reyes Pereyra 2109292

Aproximación por método de Euler

x = 0.30 f(x) = 996.004000
x = 0.60 f(x) = 992.023984
...
x = 30.00 f(x) = 548.811636
```

## Explicación del Método de Euler

El **Método de Euler** es un procedimiento numérico para resolver ecuaciones diferenciales ordinarias. Se basa en la aproximación:

\[
w\_{i+1} = w_i + h \cdot f(x_i, w_i)
\]

Donde:

- \(h\) es el tamaño del paso, calculado como \(h = \frac{b-a}{N}\).
- \(w_i\) es el valor de la función en el paso \(i\).

Este método proporciona una solución iterativa aproximada de la ecuación diferencial.

## Resultados

El programa calcula los valores de \(x\) y \(w(x)\) iterativamente y los muestra en consola. Los resultados pueden utilizarse para construir gráficos o análisis adicionales, dependiendo de los requisitos del proyecto.

## Autor

Este código fue desarrollado por:

- **Fernando Villarreal Castillo** (2049219)
- **Julio Alejandro Galindo Estrada** (1945686)
- **Oscar Eduardo Reyes Pereyra** (2109292)

### Universidad Autónoma de Nuevo León

**Curso:** Métodos Numéricos para IB
**Catedrático:** Dr. Miguel Mata Pérez  
**Fecha de entrega:** 25 de noviembre de 2024
