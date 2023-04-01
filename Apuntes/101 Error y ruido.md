# Error y Ruido

Un error cuantifica qué tan buena es una hipótesis de un modelo de aproximación de una función objetivo:
$$
\text{error} = E(h, f)
$$
Mientras, $E(h, f)$ es basado enteramente de $h$ y $f$, y es casi universal basado en errores de puntos de entrada individuales $x$. Si queremos definir un error general $e(h(x), f(x))$, tomaremos el promedio de cada uno de los individuales de $x$.

## Noisy targets

En varias aplicaciones, los datos que aprendemos no son totalmente deterministas, por lo que tienen cierto ruido que no es equitativamente determinista dato otras salidas de la función $f$. Por lo que, de lugar de tener un $y=f(x)$, tenemos la distribución objetivo $P(y|x)$.

![image-20230223093934666](/home/ivn/snap/typora/76/.config/Typora/typora-user-images/image-20230223093934666.png)