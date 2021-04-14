"""
Program określa dla wyznaczonych zadanym przez użytkownika krokiem punktów przedziału [-5; 5]
zbieżność do pierwiastków równania ((x^3)/2) - x + (1/3) = 0
"""


def f0(x):
    """
    oblicza wartość f(x) = ((x^3)/2) - x + (1/3)
    :param x: float
    :return: float
    """
    return (x ** 3) / 2 - x + (1 / 3)


def f1(x):
    """
    oblicza wartość f'(x) = ((3x^2)/2) - 1
    :param x: float
    :return: float
    """
    return (3 * x ** 2) / 2 - 1


def fpf(x):
    """
    oblicza wartość równania punktu stałego F(x) = ((x^3)/2) + (1/3)
    :param x: float
    :return: float
    """
    return (x ** 3) / 2 + (1 / 3)


def newton_iteration(x):
    """
    oblicza wartość iteracji metody Newtona x_k+1 = x_k - (f(x_k)/f'(x_k))
    :param x: float
    :return: float
    """
    return x - f0(x) / f1(x)


def newton(x):
    """
    zwraca przybliżoną wartość pierwiastka równania rozpoczynając iterację od x
    :param x: float 
    :return: float
    """
    res = newton_iteration(newton_iteration(newton_iteration(x)))
    prev1 = newton_iteration(newton_iteration(x))
    prev2 = newton_iteration(x)
    while abs(res - prev1) > 0.001 and abs(prev1 - prev2) > 0.001:
        prev2 = prev1
        prev1 = res
        res = newton_iteration(res)
    return round(res, 4)


def fpi(val):
    """
    zwraca przybliżoną wartość pierwiastka równania rozpoczynając iterację od x
    :param val:
    :return:
    """
    return fpf(val)


class Point:
    def __init__(self, val):
        """
        obiekt przechowuje wartość x_0 oraz przybliżone metodami wartości pierwiastków równania
        :param val: float
        """
        self.val = val
        self.roots = newton(val), fpi(val)

    def __repr__(self):
        return "Punkt x = " + str(self.val) + " zbiega do pierwiastka x = " + str(self.roots[0])
        # + " dla metody Newtona oraz do x = " + str(self.roots[1]) + " dla iteracji prostych"


step = int(float(input("Zadaj krok: ")) * 100)
for i in range(-500, 501, step):
    print(Point(i / 100))
