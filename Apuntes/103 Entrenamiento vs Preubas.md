# Entrenamientos vs Pruebas

Como hemos visto en clases anteriores, tenemos 2 tipos de predicciones con sus respectivos errores, variando por si son de entrenamiento o de prueba, ya que nuestro conjunto de datos se divide en 2, siendo el conjunto de **entrenamiento** y el conjunto de **prueba**.

La hipotesis final $g$ es avaluado en el conjunto de pruebas, y su resultado s tomado para estimar $E_{out}$.

## Otros tipos de objetivos

Anteriormente definimos $E_{in}$ y $E_{out}$ como funciones binarias.
$$
E_{in}(h) = \frac 1 N \sum_{n=1}^N(h(x_n) \ne f(x_n))\\
E_{out}(h) = P(h(x) \ne f(x))
$$

## Descomposición sesgo-varianza

Nos sirve para conocer el error de una hipótesis dado un dataset:
$$
E_{out}(g^{(D)}) = E_x\left((g^{(D)}(x)-f(x)^2)\right)
$$
Los algoritmos para encontrar una $g$ calculada, no necesariamente busca minimizar el error.

![image-20230306095602343](/home/ivn/snap/typora/76/.config/Typora/typora-user-images/image-20230306095602343.png)

## Curvas de aprendizaje

Las curvas de aprendizaje resumen el comportamiento de los errores $E_{in}$ y $E_{out}$ mientras el tamaño del conjunto de entrenamiento varía.

![image-20230306095538742](/home/ivn/snap/typora/76/.config/Typora/typora-user-images/image-20230306095538742.png)

