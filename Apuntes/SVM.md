# Máquinas de vectores de soporte

## Separando hiperplanos
COnsideremos un hiperplano $h=(b, w)$. Que separa los datos si y sólo si para $n=1,2,\cdots, N$
$$
y_n(w^Tx_n+b)>0
$$
La señal $y_n$ es positiva para cada punto, sin embargo, la magnitud de la señal no es significante por si misma desde que puede ser pequeña..

> El hiperplano $h$ separa los datos si y sólo so este puede ser representado por sus pesos $(b, w)$ que satisface:
> $$\min_{}$$

## Margen del hiperplano
Para calcular el margen para separar un hiperplano, nosotros necesitamos calcular la distancia del hiperplano hacia el punto más cercano.

Como al principio, vamos a calcular la distancia de un punto arbitrario x al separar el hiperplano $h=(b,w)$. Denotando su distancia por $dist(x,h)$.

Sea $x'$ cualquier punto del hiperplano, que significa $w^Tx'+b=0$. Sea $u$ el vector unitario que es normal al hiperplano $h$. entonces:
$$
dist(x,h)=|u^T(x-x')|
$$
Podemos calcular la distancia para cada punto ahora?
$$
dist(x,h)=\frac{|w^Tx-w^Tx'|}{||w||}
$$

Al multiplicarlo por las etiquetas queda igual ya que estás son de $0,1$, haciendo al mismo tiempo siempre positivo por lo que se omite el valor absoluto.

$$
dist(x,h)=\frac{y_n(w^Tx_n+b)}{||w||}
$$
Por lo que queremos minimizar la distancia:
$$
\min_{n=1,\cdots,N}dist(x_n, h)=\frac{1}{||w||}\min_{n=1,\cdots, N}y_n(w^Tx_n+b)= y_n(w^Tx_n+b)
$$
## Separando el hiperplano más ancho
$$
\text{minimizar}_{b,w} \qquad\qquad \frac 1 2w^Tw
$$
$$
\text{sujeto a} \qquad y_n(w^Tx_n+b) \ge 1
$$
Este problema se resuelve con programación cuadrática en el ámbito de optimización, similar al método simplex.

1. Sea $p=0_{d+1}$ y $c=1_{n}$.  Construir matrices $Q$ y $A$, donde:
$$
Q = \begin{bmatrix}0 & 0_d^T\\ 0_d& I_d\end{bmatrix} \qquad \qquad
A = \begin{bmatrix}y_1&-yx_1^T-\\ \vdots & \vdots\\
y_N & -y_Nx_N^T-\end{bmatrix}
$$
2. Calcular:
$$
\begin{bmatrix}b^*\\w*\end{bmatrix} = u^*\leftarrow QP(Q, p, A, c)
$$
3. Devolver la hipótesis $g(X)=sign(w^{*T}x+b)$

## Formulación dual de SVM

La formulación dual va a tener el mismo objetivo a resolver el problema, y es más fácil de resolver, sin embargo el problema va a quedar con $d+1$ dimensiones.

Ahora el problema dual está dado de la siguiente manera:
$$
\text{minimizar}_{w\in\R^d}\qquad \frac 1 2 u^TQu+p^Tu+\max_{\alpha\le 0}\alpha(c-a^Tu)
$$
Esta función es conocida como la función Lagrangiana.
$$
\mathcal{L}(u, \alpha) = \frac 1 2 u^TQu+p^Tu+\alpha(c-a^Tu)
$$
en términos de $\mathcal{L}$ el problema de optimización queda como:
$$
\min_u\max_{\alpha \le 0}\mathcal{L}(u,\alpha)
$$




