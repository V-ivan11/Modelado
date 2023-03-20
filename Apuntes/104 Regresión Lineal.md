# Regresión Lineal

Dentro del aprendizaje automático hay 3 problemas principales: la clasificación, el agrupamiento y la predicción.

## Clasificación Lineal

EL modelo lineal para clasificar datos en 2 clases usa un conjunto de hipótesis  de clasificadores lineales, donde cada $h$ tiene la forma:
$$
h(x)=sign(w,x)
$$
para algún vector $w\in \R^d$, donde $d$ es la dimensional del espacio de entrada, y añade una coordenada $x_0=1$ corresponde al sesgo o peso $w_0$.

Anteriormente mencionamos PCA, sin embargo su condición necesaria para que pueda usarse los datos deben ser linealmente separables.

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
E_{in}=\frac 1 N \sum_{n=1}^N(h(x_n)-y_n)^2
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
