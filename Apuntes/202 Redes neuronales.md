# Neural Networks

| Nombre      | Símbolo       | Dimensiones                       |
| ----------- | ------------- | --------------------------------- |
| signals in  | $s^{\{l\}}$   | $d^{\{l\}}$                       |
| outputs     | $x^{\{l\}}$   | $d^{\{l\}}$+1                     |
| weights in  | $W^{\{l\}}$   | $(d^{\{l-1\}}+1)\times d^{\{l\}}$ |
| weights out | $W^{\{l+1\}}$ | $(d^{\{l\}}+1)\times d^{\{l\}}$   |

## Forward Propagation to compute $h(x)$

1. $x^{\{0\}} \leftarrow x$
2. $for \quad l$

Si queremos calcular el error $E_{in}$ lo que tenemos que hacer es $h(x_n)$
$$
\begin{eqnarray}
E_{in} &=& \frac 1 N \sum_{n=1}^N(h(w_n;w)-y_n)^2\\
&=& \frac 1 N \sum_{n=1}^N
\end{eqnarray}
$$

## Backpropagation Algorithm

$$
\frac{\partial E_{in}}{\partial W^{\{l\}}} =  \frac{1}{N} \sum_{n=1}^N\frac{\partial e_n}{\partial W^{\{l\}}}
$$

**Input:** A data point $(x,y)$

1. RUn forward propagation on $x$ to calculate and save
   $$
   s^{\{l\}}\quad \text{for } l=1,\cdots, L\\
   x^{\{l\}}\quad \text{for } l=1,\cdots, L
   $$

2. $\delta^{\{L\}} \leftarrow 2 (x^{\{L\}}-y)\theta'(s^{\{L\}})$

3. $\text{for } l = L-1\text{ do:}$

   Compute the sensitivity $\delta^{\{l\}}$ from $\delta^{\{l\}}$

   

## Validation and regularization

