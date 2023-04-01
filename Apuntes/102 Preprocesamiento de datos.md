# Pre-procesamiento Básico de Datos

El pre procesamiento de los datos son técnicas que generalmente refiere a la adición, eliminación, transformación del conjunto de entrenamiento. Esto va a ser muy importante para crear un buen modelo. Además, hay que tener en cuenta que este proceso va a variar dependiendo de nuestro dataset.

## Transformación para características individuales

### Escalado y Centrado

Es una de las técnicas de transformación de datos más comunes para centrar a escala nuestras variables.
$$
x = \frac{x-\mu}{\sigma}
$$
Otra técnica de procesamiento es la **escala min-max** teniendo un dominio $D \in[0,1]$
$$
\hat x = \frac{x-\min(x)}{\max(x)-\min(x)}
$$

### Mejorar la Simetría (Skewness)

Este método nos sirve para transformar los datos haciendo que su distribución sea más simétrica con respecto a la media.
$$
\mathbb E \left(\left(\frac{x-\mu_x}{\sigma_x}\right)^3 \right)
$$
La regla general es considerar si el skewness está dentro de [-2, 2], los datos tienen buena simetría.

Usando la raíz cuadrada, el logaritmo o su inversa también puede ayudar a mejorar la simetría.

## Transformación para múltiples características

### Resolver los "outliers"

Definimos a los datos anómalos (outliers) que están muy lejos de ser realistas en el contexto de nuestros datos. Una de las técnicas que puede minimizar este problema es la señal espacial, este proyecta los valores de la característica a una esfera multidimensional.
$$
x_i^*=\frac{x_i}{||x_i||}
$$
Dado que este método trata de medir la distancia cuadrada al centro de la esfera, es necesario centrar o escalar los datos.

### Reducción de datos y extracción de características

Estos métodos reducen los datos para generar pequeños conjuntos de características que resuman la gran mayoría de la información de nuestras variables originales.

#### Análisis de Componentes Principales

Con el objetivo el reducir las dimensiones teniendo la mayor varianza posible.

Consideremos una matriz de datos $N \times d$ con media cero.
$$
\begin{bmatrix}
\cdots & x_{(1)}& \cdots\\
\cdots & x_{(2)}& \cdots\\
&\vdots&\\
\cdots & x_{(N)}& \cdots\\
\end{bmatrix}
$$
La transformación es definida por un conjunto de tamaño $k$ de $d$ vectores dimensionales con pesos $w_{(j)}=(w_1, w_2, \cdots, w_d)_{(j)}$ que mapea cada fila del vector $x_{(i)}$ de $X$ a un nuevo vector con las puntuaciones de com0ponentes principales $t_{(i)}=(t_1,t_2,\cdots,t_k)$ dado por:
$$
t_{j(i)}=x_{(i)}\cdot w_{(j)} \qquad \text{para todo }i=1,\cdots,N\qquad j=1,\cdots, k
$$

####  Primer componente

$$
\begin{eqnarray}
w_{(1)}&=&arg\max_{||w||=1}\left(\sum_{i=1}^N(t_1)^2_{(i)}\right)\\
&=&arg\max_{||w||=1}\left(\sum_{i=1}^N(x_{(i)} \cdot w)^2\right)\\
&=& arg\max_{||w||=1}\left(||Xw||^2\right)\\
&=& arg\max_{||w||=1}\left(w^TX^TXw\right)
\end{eqnarray}
$$

Dado que $w_{(1)}$ ha sido definido para ser un vector unitario, satisface:
$$
w_{(1)}=arg\max\left(\frac{w^TX^TXw}{w^Tw}\right)
$$
Esto se conoce como el *Rayleigh quotient*.

#### Siguientes componentes

$$
\hat X_j=X-\sum_{s=1}^{j-1}Xw_{(s)}w_{(s)}^T
$$

y después encontrar el peso del vector que extrae la máxima varianza de la nueva matriz de datos.
$$
w_{(j)}=arg\max\left(\frac{w^TX^TXw}{w^Tw}\right)
$$

## Datos faltantes

En varios casos, algunas características no tienen valores, por lo que es importante entender porqué los valores están faltando, por lo que primero vamos a buscar un patrón que tal vez caracterice a nuestros datos faltantes.

## Datos censurados

El valor exacto falta pero si se sabe algo del dato, por ejemplo en medidas de laboratorios clínicos.

En conjuntos grandes de datos, eliminar los datos faltantes no es un problema, asumiendo de que esta falta no es informativa, sin embargo, en conjuntos de datos pequeños puede significar una pérdida significante de información, por lo que se van a describir métodos para tratar este problema.

- Primero, algunos modelos predictivos puedes ayudarnos a llenar los datos faltantes
- Podemos usar Análisis de Componentes Principales para conocer si hay relaciones fuertes entre variables, en dado caso un modelo enfocado puede ser efectivo.
- Reemplazar los valores faltantes con una características estadística adecuada a ellos, por ejemplo colocando la media o la moda.

## Eliminar características

Existen ventajas potenciales al eliminar características antes del modelado.

1. Pocas características significan decremento de complejidad computacional y temporal.
2. Si 2 características están altamente correlacionadas, esto implica que ambas medidas tienen casi la misma información.

Un algoritmo para eliminar características, está dado por:

1. Calcular la matriz de correlación
2. Determinar las 2 características con mayor correlación absoluta dado un límite definido, llamando $A$ y $B$ estas características
3. Calcular el promedio de correlación entre $A$ y $B$ con las otras variables
4. Eliminar la característica con mayor promedio de correlación
5. Repetir desde el paso 2 hasta que se haya llegado al límite definido de la correlación

