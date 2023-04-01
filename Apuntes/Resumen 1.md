# 1.0 Introducción

Aprender a partir de datos es usado donde nosotros no tenemos una solución analítica, pero nosotros tenemos datos con la que podemos construir una solución empírica.

Función desconocida, Ejemplos de entrenamiento, algoritmo de aprendizaje, hipótesis final.

![image-20230221090350064](/home/ivn/snap/typora/76/.config/Typora/typora-user-images/image-20230221090350064.png)

### Un modelo simple de aprendizaje

Dado un problema de aprendizaje específico, la función objetivo y un conjunto de entrenamiento están dichos por el problema. Sin embargo, el algoritmo de aprendizaje y el conjunto de hipótesis no lo dan. Estas son herramientas de solución que debemos de escoger. El conjunto de hipótesis y el algoritmo de aprendizaje son referidos informalmente como el modelo de aprendizaje.

La función objetivo $h(x)\in H$ que escogemos diferentes pesos a las diferentes coordenadas de $x$, devolviendo su relativa importancia hacia la decisión.

## Perceptrón PLA

$$
h(x)=sign\left(\left(\sum_{i=1}^dw_ix_i\right)+b\right)=sign(w^Tx)
$$

Este modelo de $H$ es llamado perceptrón, un nombre que tiene contexto en inteligencia artificial. Las decisiones optimas de los pesos y el bias son definidas en la hipótesis final $g\in H$ que el algoritmo produce.

![image-20230221090848421](/home/ivn/snap/typora/76/.config/Typora/typora-user-images/image-20230221090848421.png)



### Algoritmo

Mientras exista un punto desclasificado en el dataset $D$:

1. Inicializar $w(0)$ aleatoriamente

2. Computar $h(x)$ para cada $x$ en el dataset $D$

3. Tomar un punto desclasificado muestra $(x_t, y_t)$ lo llamamos $(x(t), y(t))$

4. Desde el ejemplo desclasificado, nosotros tenemos $y(t) \ne sign(w^T(t)x(t))$ después cambiando
   $$
   w(t+1) = w(t)+y(t)x(t)
   $$
   ![image-20230221091537952](/home/ivn/snap/typora/76/.config/Typora/typora-user-images/image-20230221091537952.png)

   | $X$  | $s(x)=x+2$ | $2x-4$ | $h(x)=sign(s(x))$ |
   | :--: | :--------: | :----: | :---------------: |
   |  0   |     2      |   -4   |         1         |
   |  -2  |     0      |   -8   |         0         |
   |  -4  |     -2     |  -12   |        -1         |
   |      |            |        |                   |

   

## Aprendizaje versus Diseño

- Aprendizaje es basado en datos
- Diseño es basado en especificaciones

## Tipos de aprendizaje

- Aprendizaje supervisado: Aprender de los datos
- Aprendizaje reforzado: Aprender a partir de la experiencia
- Aprendizaje no supervisado: Aprender de patrones (estructuras)

## Es aprender factible?

![image-20230223084900834](/home/ivn/snap/typora/76/.config/Typora/typora-user-images/image-20230223084900834.png)

Lo más importante es que cuando elaboremos un modelo de aprendizaje, esté debe de estar entrenado correctamente para ver sobre la predicción de nuevas características no vistas anteriormente, sin esto, no serviría nuestro modelo si sólo funciona para el conjunto de entrenamiento.

### Desigualdad de Hoeffding

$$
P[|v-\mu| > \epsilon] \le2e^{-2\epsilon^2N}
$$

Conforme $N$ se haga más grande, se hará más pequeño, por lo que es mejor tomar más muestras si se quiere tener mayor precisión.

Consideremos el error de la muestra:
$$
E_{in}=\frac 1 N \sum_{n=1}^N[h(x_n)\ne f(x_n)]
$$
Y el error fuera de la muestra como:
$$
E_{out}(h)=P[h(x_n)\ne f(x_n)]
$$
Aplicando la desigualdad:
$$
P[|v-\mu|> \epsilon] = P[|E_{in}-E_{out}|<\epsilon] \le 2e^{-2\epsilon^2N}
$$
Sin embargo, no tenemos control de $E_{in}$, ya que está basada en una hipótesis particular $h$. En un verdadero aprendizaje, nosotros exploramos el conjunto de hipótesis $H$ completo, buscando un $h\in H$ que tanga el menor error.

Consideremos un conjunto de hipótesis finito $H$ de lugar de sólo una hipótesis $h$.
$$
H=\{h_1, h_2, \cdots, h_M\}
$$
Con múltiples hipótesis en $H$, el algoritmo de aprendizaje toma la hipótesis final $g$ de acuerdo en $D$. Dado $g$ tiene que estar en $H$, entonces:
$$
\begin{eqnarray}
P[|E_{in}(g)-E_{out}(g)|<\epsilon] &\le& P[|E_{in}(h_1)-E_{out}(h_1)|<\epsilon]\\
&>& \epsilon \text{ or } P[|E_{in}(h_2)-E_{out}(h_2)| < \epsilon] \cdots\\
&\le& 2 Me^{-2\epsilon^2N}
\end{eqnarray}
$$
# Error y Ruido

Un error cuantifica qué tan buena es una hipótesis de un modelo de aproximación de una función objetivo:
$$
\text{error} = E(h, f)
$$
Mientras, $E(h, f)$ es basado enteramente de $h$ y $f$, y es casi universal basado en errores de puntos de entrada individuales $x$. Si queremos definir un error general $e(h(x), f(x))$, tomaremos el promedio de cada uno de los individuales de $x$.

## Noisy targets

En varias aplicaciones, los datos que aprendemos no son totalmente deterministas, por lo que tienen cierto ruido que no es equitativamente determinista dato otras salidas de la función $f$. Por lo que, de lugar de tener un $y=f(x)$, tenemos la distribución objetivo $P(y|x)$.

![image-20230223093934666](/home/ivn/snap/typora/76/.config/Typora/typora-user-images/image-20230223093934666.png)
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
# Entrenamientos vs Pruebas

Como hemos visto en clases anteriores, tenemos 2 tipos de predicciones con sus respectivos errores, variando por si son de entrenamiento o de prueba, ya que nuestro conjunto de datos se divide en 2, siendo el conjunto de **entrenamiento** y el conjunto de **prueba**.

La hipótesis final $g$ es avaluado en el conjunto de pruebas, y su resultado $s$ tomando para estimar $E_{out}$.

## Otros tipos de objetivos

Anteriormente definimos $E_{in}$ y $E_{out}$ como funciones binarias.
$$
E_{in}(h) = \frac 1 N \sum_{n=1}^N(h(x_n) \ne f(x_n))\\
E_{out}(h) = P(h(x) \ne f(x))
$$

Si $f$ y $h$ son funciones de los reales, se usa el error cuadrático:
$$
E_{in}(h)=\frac 1 N\sum_{n=1}^N (h(x_n)-f(x_n))^2\\
E_{out}(h)=\text{E}[(h(x)-f(x))^2]
$$


## Descomposición sesgo-varianza

Nos sirve para conocer el error de una hipótesis dado un dataset:
$$
E_{out}(g^{(D)}) = E_x\left((g^{(D)}(x)-f(x)^2)\right)
$$
Los algoritmos para encontrar una $g$ calculada, no necesariamente busca minimizar el error.

![image-20230306095602343](/home/ivn/snap/typora/76/.config/Typora/typora-user-images/image-20230306095602343.png)
$$
bias(x) = (\bar g(x)-f(x))^2\\
var(x) = \text{E}_D[g^{D}(x)^2-\bar g(x)^2]
$$
Esto nos da el error descomposición sesgo-varianza de los datos fuera de la muestra:
$$
\text{E}_D[E_{out}(g^{(D)})]= \mathbb E [bias(x)+var(x)]=bias+var
$$


## Curvas de aprendizaje

Las curvas de aprendizaje resumen el comportamiento de los errores $E_{in}$ y $E_{out}$ mientras el tamaño del conjunto de entrenamiento varía.

![image-20230306095538742](/home/ivn/snap/typora/76/.config/Typora/typora-user-images/image-20230306095538742.png)

# Modelo Lineal

Dentro del aprendizaje automático hay 3 problemas principales: la clasificación, el agrupamiento y la predicción.

## Clasificación Lineal

EL modelo lineal para clasificar datos en 2 clases usa un conjunto de hipótesis  de clasificadores lineales, donde cada $h$ tiene la forma:
$$
h(x)=sign(w,x)
$$
para algún vector $w\in \R^d$, donde $d$ es la dimensional del espacio de entrada, y añade una coordenada $x_0=1$ corresponde al sesgo o peso $w_0$.

Anteriormente mencionamos PLA, sin embargo su condición necesaria para que pueda usarse los datos deben ser linealmente separables.

## Datos no separables

A veces los datos no pueden ser linealmente separables, sin embargo el modelo puede funcionar ya que no son linealmente separables por varias causas, siendo una de ellas el ruido o los datos anómalos. Para encontrar una hipótesis con el mínimo error, $E_{in}$ necesitamos para resolver el problema de de optimización combinatoria.
$$
\min_{w\in \R^{d+1}} E_{in}(w)=\min_{w\in \R^{d+1}}\frac 1 N \sum_{n=1}^N(sign(w^T,x))
$$

### Pocket algorithm

1. Inicializar el peso del vector $\hat w$ con $w(0)$ usando PLA
2. Para $t=0,\cdots,T_1$ hacer:
   1. Ejecutar PLA por una actualización para obtener $w(t+1)$
   2. Evaluar $E_{in}(w(t+1))$
   3. Si $w(t+1)$ es mejor que $\hat w$ en términos de $E_{in}$ asignar $\hat w$ a $w(t+1)$
3. Devolver $\hat w$

## Regresión lineal

Una regresión lineal es otro modelo lineal que se aplica para funciones con funciones objetivo con valores reales. 

### El algoritmo

Buscamos obtener el mínimo del error (MSE) entre $h(x)$ y $y$.
$$
E_{out}=\frac 1 N \sum_{n=1}^N(h(x_n)-y_n)^2
$$
Donde $h(x)=w^Tx$, por lo que
$$
\begin{eqnarray}
E_{in}  &=& \frac{1}{N} \sum_{n=1}^N(w^Tx_n-y_n)^2 = \frac 1 N ||Xw-y||^2\\
&=& \frac 1 N (w^TX^TXw - 2w^TX^Ty+y^Ty)
\end{eqnarray}
$$
Finalmente, formalizamos el problema de optimización de acuerdo al siguiente problema
$$
w_{lin}=arg\min_{w\in \R^{d+1}} E_{in}(w)
$$

### Linear Regression Algorithm (OLS)

1. Construimos la matrix $X$ y el vector $y$ del dataset $(x_1, y_1), \cdots, (x_N,y_N)$ donde cada $x$ incluye la coordenada  $x_0=1$, siendo la transpuesta de los datos.
2. Calculamos la pseudoinversa de $X$
3. Retornamos $w_{lin}=X^\dagger y$

## Regresión logística

En regresión lineal, la señal por sí sola puede ser tomada como salida, lo cual es apropiado si se desea predecir una respuesta real que podría ser sin límites. Una clasificación lineal, la señal es limitada para producir salidas $\pm1$, las cuales son apropiadas para decisiones binarias.

Ahora nuestro nuevo modelo es llamado regresión logística,
$$
h(x)=\theta(w^Tx)
$$
donde $\theta$ es llamada la función logística o función sigmoide:
$$
\theta(s)=\frac{e^s}{1+e^s}
$$
donde sus salidas están entre $0$ y $1$, pudiéndose interpretar como la probabilidad para que pase un evento. La clasificación lineal trata con eventos binarios, pero la diferencia es que la clasificación en una regresión logística es permitida no ser determinista.

En este caso, la función objetivo es de probabilidad y depende de la entrada $x$. Formalmente tratamos de aprender la función objetivo:
$$
f(x)=P[y=+1|x]
$$
El error estándar es medido como $e(h(x), y)$ usado en la regresión logística basada en la noción de verosimilitud, que tan probable es que se consiga una salida $y$ dado un $x$ si la distribución objetivo $P(y|x)$ fue de hecho escrita por nuestra hipótesis $h(x)$.

Si sustituimos $h(x)$:
$$
P(y|x)=\theta(yw^Tx)
$$
Dado que los puntos $(x_1, y_1), \cdots, (x_N, y_N)$ son generadas de manera independiente, la probabilidad de obtener todas las $y's$ del conjunto de datos sería el producto:
$$
\prod_{n=1}^NP(y_n|x_n)
$$
El método de la máxima verosimilitud selecciona la hipótesis $h$ que maximiza su probabilidad, por lo que la podemos escribir:
$$
-\frac1 N \ln\left(\prod_{n=1}^NP(y_n|x_n)\right)=\frac 1 N\sum_{n=1}^N \ln\left(\frac{1}{P(y_n|x_n)}\right)=\frac 1 N\sum_{n=1}^N \ln\left(\frac{1}{\theta(yw^Tx)}\right)
$$
Sustituyendo para el error de la muestra:
$$
E_{in}(w)=\frac{1}{N}\sum_{n=1}^N\ln\left(1+e^{-y_nw^Tx_n}\right)
$$

## Gradiente descendiente

El gradiente descendiente es una técnica general para minimizar funciones diferenciales, tal que $E_{in}(w)$ en la regresión logística.

Queremos tomar un paso hacia la dirección escendente, para obtener el mejor salto, supongamos que tomamos un paso de tamaño $\alpha$ en la dirección del vector unitario $\hat{v}$. Los nuevos pesos son $w(O)+\alpha\hat v$.

Dado que $\hat v$ es un vector unitario:
$$
\hat v=-\frac{\nabla E_{in}(w(0))}{||\nabla E_{in}(w(0))||}
$$




Supongamos un conjunto de hipótesis $H= \{g_1(x) = c, \quad g_2(x)=0\}$

Por lo que:
$$
\bar g= \frac 1 2 (c+0) =\frac c 2
$$
Esta $\bar g$ no pertenece a $H$.



