from numbers import Number
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Polynomial:

    def __init__(self, coefs):
        """Constructor de la clase Polynomial."""
        self.coefficients = np.array(coefs)

    def __str__(self):
        """Representación en cadena del polinomio."""
        terms = []
        for i, coef in enumerate(self.coefficients):
            # si coeficiente es 0, no se agrega el término
            if coef == 0:
                continue
    # si es el primer término, se agrega sin signo
            elif i == 0:
                terms.append(f"{coef}")
    # si el grado es mayor a 1, se agrega el término con x^i
            elif coef > 1 and i > 1:
                terms.append(f" + {coef}x^{i}")
            elif coef < -1 and i > 1:
                terms.append(f" - {abs(coef)}x^{i}")
    # si el grado es 1, se agrega el término con x
            elif coef > 1 and i == 1:
                terms.append(f" + {coef}x")
            elif coef < -1 and i == 1:
                terms.append(f" - {abs(coef)}x")
    # si el grado es 1 y el coeficiente es 1 o -1, se agrega el término con x
            elif coef == 1 and i == 1:
                terms.append(" + x")
            elif coef == -1 and i == 1:
                terms.append(" - x")
    # si el coeficiente es 1 o -1, se agrega el término con x^i
            elif coef == 1 and i > 1:
                terms.append(f" + x^{i}")
            elif coef == -1 and i > 1:
                terms.append(f" - x^{i}")

            text = "".join(terms)
            text = text.strip()
        if text[0] == "+":
            text = text[1:]
        return text

    def __repr__(self):
        """Representación en cadena del polinomio para depuración."""
        return self.__str__()

    def __eq__(self, other):
        """Compara dos polinomios para ver si son iguales."""
        if isinstance(other, Polynomial):
            return np.array_equal(self.coefficients, other.coefficients)
        return False

    def degree(self):
        """Devuelve el grado del polinomio."""
        return len(self.coefficients) - 1

    def __add__(self, other):
        """Suma dos polinomios o de un Polinomio con un número."""
        if isinstance(other, Polynomial):
            len_self = len(self.coefficients)
            len_other = len(other.coefficients)
            max_len = max(len_self, len_other)

            c1 = np.pad(self.coefficients, (0, max_len - len_self), 'constant')
            c2 = np.pad(other.coefficients, (0, max_len - len_other), 'constant')

            new_coef = np.add(c1, c2)
            return Polynomial(new_coef)
        elif isinstance(other, Number):
            new_coef = self.__add__(Polynomial((other,)))
            return new_coef
        return NotImplemented

    def __radd__(self, other):
        """Suma un número a un polinomio."""
        if isinstance(other, Number):
            new_coef = self.__add__(Polynomial((other,)))
            return new_coef
        return NotImplemented

    def __sub__(self, other):
        """Resta dos polinomios o de un Polinomio con un número."""
        if isinstance(other, Polynomial):
            len_self = len(self.coefficients)
            len_other = len(other.coefficients)
            max_len = max(len_self, len_other)

            c1 = np.pad(self.coefficients, (0, max_len - len_self), 'constant')
            c2 = np.pad(other.coefficients, (0, max_len - len_other), 'constant')

            new_coef = np.subtract(c1, c2)
            return Polynomial(new_coef)
        elif isinstance(other, Number):
            new_coef = self.__sub__(Polynomial((other,)))
            return new_coef
        return NotImplemented

    def __rsub__(self, other):
        """Resta un polinomio a un número."""
        if isinstance(other, Number):
            new_coef = Polynomial((other,)).__sub__(self)
            return new_coef
        return NotImplemented

    def __mul__(self, other):
        """Multiplica dos polinomios o de un Polinomio con un número."""
        if isinstance(other, Polynomial):
            new_coef = np.polymul(self.coefficients, other.coefficients)
            return Polynomial(new_coef)
        elif isinstance(other, Number):
            new_coef = self.coefficients * other
            return Polynomial(new_coef)
        return NotImplemented

    def __rmul__(self, other):
        """Multiplica un número a un polinomio."""
        if isinstance(other, Number):
            new_coef = self.coefficients * other
            return Polynomial(new_coef)
        return NotImplemented

    def graph(self, x_range=(-10, 10)):
        """Grafica el polinomio en un rango de valores de x."""

        x = np.linspace(x_range[0], x_range[1], 10000)
        y = np.polyval(self.coefficients[::-1], x[:])

        sns.set_style("darkgrid")

        sns.lineplot(x=x, y=y, color='C0', linewidth=1.5, zorder=3)

        plt.axvline(
            x=0, color='black', linewidth=1.0, linestyle='--', alpha=0.4, zorder=2
            )
        plt.axhline(
            y=0, color='black', linewidth=1.0, linestyle='--', alpha=0.4, zorder=2
            )

        plt.title(f"Polynomial: {self}", fontsize=14, fontweight='bold')
        plt.xlabel("x", fontsize=12, fontweight='semibold')
        plt.ylabel("f(x)", fontsize=12, fontweight='semibold')

        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        plt.ylim(top=max(y))

        plt.show()
