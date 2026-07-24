from numbers import Number
from itertools import zip_longest


class Polynomial:

    def __init__(self, coefs):
        """Constructor de la clase Polynomial."""
        self.coefficients = coefs

    def __str__(self):
        """Representación en cadena del polinomio."""
        terms = []
        for i, coef in enumerate(self.coefficients):
            # si coeficiente es 0, no se agrega el término
            if coef == 0:
                continue
            # si es el primer término, se agrega sin signo
            if i == 0:
                terms.append(f"{coef}")
            # si el grado es mayor a 1, se agrega el término con x^i
            if coef > 1 and i > 1:
                terms.append(f" + {coef}x^{i}")
            elif coef < -1 and i > 1:
                terms.append(f" - {abs(coef)}x^{i}")
            # si el grado es 1, se agrega el término con x
            if coef > 1 and i == 1:
                terms.append(f" + {coef}x")
            elif coef < -1 and i == 1:
                terms.append(f" - {abs(coef)}x")
            # si el coeficiente es 1 o -1, se agrega el término con x^i
            if coef == 1 and i > 1:
                terms.append(f" + x^{i}")
            elif coef == -1 and i > 1:
                terms.append(f" - x^{i}")
        return "".join(terms)

    def __eq__(self, other):
        """Compara dos polinomios para ver si son iguales."""
        if isinstance(other, Polynomial):
            return self.coefficients == other.coefficients
        return False

    def degree(self):
        """Devuelve el grado del polinomio."""
        return len(self.coefficients) - 1

    def __add__(self, other):
        """Suma dos polinomios."""
        if isinstance(other, Polynomial):
            new_coef = tuple(a + b for a, b in zip_longest(
                self.coefficients, other.coefficients, fillvalue=0)
                )
            return Polynomial(new_coef)
        elif isinstance(other, Number):
            return Polynomial(
                (self.coefficients[0] + other,) + self.coefficients[1:]
                )
        else:
            return NotImplemented

    def __radd__(self, other):
        """Suma un número a un polinomio."""
        if isinstance(other, Number):
            return Polynomial(
                (self.coefficients[0] + other,) + self.coefficients[1:]
                )
        else:
            return NotImplemented
