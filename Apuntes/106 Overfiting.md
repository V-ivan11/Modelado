# Overfitting

El overfitting es un fenómeno donde hay un sobreajuste en los datos observados a parit de un modelo.

![image-20230316084134765](/home/ivn/snap/typora/76/.config/Typora/typora-user-images/image-20230316084134765.png)

![image-20230316084931176](/home/ivn/snap/typora/76/.config/Typora/typora-user-images/image-20230316084931176.png)

La figura anterior muestra un ejemplo de overfitting en modelos polinomiales.

## Selección del modelo

La parte más importante de la validación es la selección del modelo. Para ello supongamos que tenemos $M$ modelos $H_1, H_2, \cdots, H_M$. Usando el conjunto de entrenamiento $D_{train}$ para aprender la hipótesis final $g_m$ para cada modelo. Ahora evaluamos cada modelo.

Dado que escogemos el modelo con el menor error de validación $E_m$, tendremos un bias optimista.

Por lo tanto, el objetivo principal es seleccionar el mejor modelo y mejores resultados de la mejor hipótesis del modelo.

## Cross-validation

Tenemos $N$ maneras de partir los datos a un conjunto de tamaño $N-1$ y el conjunto de validación con tamaño $1$.
$$
D_n= \{(x_1, y_1), \cdots, (x_{n-1},y_{n-1}), (x_{n+1},y_{n+1}), \cdots,(x_N,y_N)\}
$$
Sea $e_n$ el error hecho por el conjunto de validación:



