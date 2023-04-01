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
