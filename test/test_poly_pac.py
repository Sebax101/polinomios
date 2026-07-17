from poly_pac import Polynomial

def test_polynomial_str():
    p = Polynomial([1, 0, -2, 3])
    assert str(p) == "1 - 2x^2 + 3x^3"
    assert p.degree() == 3