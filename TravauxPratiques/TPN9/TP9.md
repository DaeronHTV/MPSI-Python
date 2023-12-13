# TP I.P.T 9 - Intégration Numérique

Au cours de cette séance de travaux pratiques, nous allons intéresser à différentes méthodes d'intégration numérique
ainsi qu'à leurs propriétés.

## 1. Méthode générale

Il s'agit ici de calculer une valeur numérique approchée de I = <code>**&#8747;f(x)dx**</code>, par deux méthodes : la
méthode des rectangles ainsi qu'à leurs propriétés.

### Principe des algorithmes

Il s'agit de calculer la valeur de l'intégrale, qui correspond à l'aire sous la courbe représentative de **f(x)** sur
l'intervalle **[a,b]**, en la remplaçant par une somme de rectangles ou de trapèzes.

TODO - Mettre les graphes

On part de l'intervalle **[a,b]** que l'on découpe en n parties égales de longueur <code>**h = (b-a)/n**</code>. Si l'on
approche la valeur de l'intégrale par une somme de rectangles, on aura alors :

<center><code>I &#8776; (b-a)/n &#8721;<sup>n-1</sup>f(a<sub>k</sub>) + f(a<sub>k+1</sub>)/2</code></center>

où les **a<sub>k</sub>** représentent les abscisses des points situés entre **a** et **b**.

1. Ecrire une fonction **rectangles(f,a,b,n)** et une fonction **trapezes(f,a,b,n)** permettant le calcul de 

### Application

## 2. Application

### Pour s'entrainer

### Mini-Projet