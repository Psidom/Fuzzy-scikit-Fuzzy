import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz


# Generate trapezoidal membership function on range [0, 1]
x = np.arange(0, 5.05, 0.1)
""""
A função arange cria um arranjo contendo uma seqüência de valores especificados em um intervalo com início e fim dados, espaçados de maneira uniforme. Os dados podem ter qualquer tipo numérico, especificado pelo argumento dtype. Esta função vai devolver um arranjo unidimensional que pode ser usado em qualquer operação que exija arranjos.

start
Este argumento é opcional. Se ele for omitido, admite-se que o início do intervalo é 0. Se for especificado, o primeiro elemento do arranjo terá esse valor.
stop
Indica o final do intervalo. Como é característica da linguagem, este último valor não vai fazer parte do arranjo retornado. É importante notar essa distinção. Se é necessário que esse valor seja parte do intervalo, utilize a função numpy-linspace .
step
Este argumento indica o intervalo entre cada elemento do arranjo. Pode ser um valor em ponto flutuante. Este argumento pode ser omitido, e nesse caso, admite-se o intervalo entre os elementos iguais a um.
dtype
Indica o tipo numérico dos elementos do arranjo resultante. Se for omitido, os dados terão o tipo mais simples possível para representar os números.
"""
mfx = fuzz.trapmf(x, [2, 2.5, 3, 4.5])# Variavel mfx recebe um trapezio fuzzificado.
"""
    Trapezoidal membership function generator.

    Parameters
    ----------
    x : 1d array
        Independent variable.
    abcd : 1d array, length 4
        Four-element vector.  Ensure a <= b <= c <= d.

    Returns
    -------
    y : 1d array
        Trapezoidal membership function.

"""

# Defuzzify this membership function five ways
defuzz_centroid = fuzz.defuzz(x, mfx, 'centroid')  # Same as skfuzzy.centroid
defuzz_bisector = fuzz.defuzz(x, mfx, 'bisector')
defuzz_mom = fuzz.defuzz(x, mfx, 'mom')
defuzz_som = fuzz.defuzz(x, mfx, 'som')
defuzz_lom = fuzz.defuzz(x, mfx, 'lom')
"""
    Defuzzification of a membership function, returning a defuzzified value
    of the function at x, using various defuzzification methods.

    Parameters
    ----------
    x : 1d array or iterable, length N
        Independent variable.
    mfx : 1d array of iterable, length N
        Fuzzy membership function.
    mode : string
        Controls which defuzzification method will be used.
        * 'centroid': Centroid of area
        * 'bisector': bisector of area
        * 'mom'     : mean of maximum
        * 'som'     : min of maximum
        * 'lom'     : max of maximum

    Returns
    -------
    u : float or int
        Defuzzified result.

    See Also
    --------
    skfuzzy.defuzzify.centroid, skfuzzy.defuzzify.dcentroid
    """

# Collect info for vertical lines - coletando informacao para montar o grafico
labels = ['centroid', 'bisector', 'mean of maximum', 'min of maximum',
          'max of maximum']
xvals = [defuzz_centroid,
         defuzz_bisector,
         defuzz_mom,
         defuzz_som,
         defuzz_lom]
colors = ['r', 'b', 'g', 'c', 'm']
ymax = [fuzz.interp_membership(x, mfx, i) for i in xvals]

# Display and compare defuzzification results against membership function
plt.figure(figsize=(8, 5))

plt.plot(x, mfx, 'k')
for xv, y, label, color in zip(xvals, ymax, labels, colors):
    plt.vlines(xv, 0, y, label=label, color=color)
plt.ylabel('Fuzzy membership')
plt.xlabel('Universe variable (arb)')
plt.ylim(-0.1, 1.1)
plt.legend(loc=2)

plt.show()