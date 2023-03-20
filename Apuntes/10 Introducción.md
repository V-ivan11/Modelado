# 1.0 Introducción

>  Learning from data, Mustafa

## El problema del aprendizaje

Aprender a partir de datos es usado donde nosotros no tenemos una solución analítica, pero nosotros tenemos datos con la que podemos construir una solución empírica.

Función desconocida, Ejemplos de entrenamiento, algoritmo de aprendizaje, hipótesis final.

![image-20230221090350064](/home/ivn/snap/typora/76/.config/Typora/typora-user-images/image-20230221090350064.png)

### Un modelo simple de aprendizaje

Dado un problema de aprendizaje específico, la función objetivo y un conjunto de entrenamiento están dichos por el problema. Sin embargo, el algoritmo de aprendizaje y el conjunto de hipótesis no lo dan. Estas herramientas de solución son las que debemos de escoger. El conjunto de hipótesis.

La función objetivo $h(x)\in N$ que escogemos diferentes pesos a las diferentes coordenadas de $x$, devolviendo su relativa importancia hacia la decisión.

## Perceptrón PLA

$$
h(x)=sign\left(\left(\sum_{i=1}^dw_ix_i\right)+b\right)=sign(w^Tx)
$$

Este modelo de $H$ es llamado perceptrón, un nombre que tiene contexto en inteligencia artificial. Las decisiones optimas de los pesos y el bias defina a hipótesis final $g\in H$ que el algoritmo produce.

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