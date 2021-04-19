"""
Program określa dla wyznaczonych zadanym przez użytkownika krokiem punktów przedziału [-5; 5]
zbieżność do pierwiastków równania ((x^3)/2) - x + (1/3) = 0
"""
import xlsxwriter as xwt
import os

# ścieżka oraz nazwa pliku wynikowego programu
OUTDIR = 'Dokumentacja'
OUTPUT = OUTDIR+'/output.xlsx'


def output_check():
    """
    tworzy ścieżkę dla pliku wynikowego, oraz usuwa istniejące pliki wynikowe
    :return: None
    """
    if not os.path.exists(OUTDIR):
        os.mkdir(OUTDIR)
        print("Utworzono ścieżkę dla pliku wynikowego programu.")
    else:
        print("Ścieżka dla pliku wynikowego już istnieje.")
        try:
            os.remove(OUTPUT)
            print("Usunięto stary plik wynikowy.")
        except FileNotFoundError:
            print("Nie znaleziono pliku wynikowego programu.")


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

    while abs(res - prev1) > 0.00001 or abs(prev1 - prev2) > 0.00001:
        prev2 = prev1
        prev1 = res
        res = newton_iteration(res)

    return round(res, 5)


def fpi(x):
    """
    zwraca przybliżoną wartość pierwiastka równania rozpoczynając iterację od x
    :param x: float
    :return: string or float0.
    """
    res = fpf(fpf(fpf(x)))
    prev1 = fpf(fpf(x))
    prev2 = fpf(x)

    try:
        while abs(res - prev1) > 0.00001 or abs(prev1 - prev2) > 0.00001:
            prev2 = prev1
            prev1 = res
            res = fpf(res)

    except OverflowError:
        return "Wyznaczony ciąg x_k jest rozbieżny"

    return round(res, 5)


class Point:
    def __init__(self, val):
        """
        obiekt przechowuje wartość x_0 oraz przybliżone metodami wartości pierwiastków równania
        :param val: float
        """
        self.val = val
        self.roots = newton(val), fpi(val)

    def __repr__(self):
        return "x= "+str(self.val)+" Newton: "+str(self.roots[0])+" IP: "+str(self.roots[1])
    

def create_points():
    """
    funkcja tworzy określoną przez użytkownika listę obiektów typu Point
    :return: list(Point) 
    """
    print("OSTRZEŻENIE: Program pobiera dane z dokładnością do dwóch miejsc po przecinku!")

    range_a = int(float(input("Podaj początek przedziału badania: ")) * 100)
    range_b = int(float(input("Podaj koniec przedziału badania: ")) * 100) + 1
    step = int(float(input("Zadaj krok: ")) * 100)

    return [Point(i/100) for i in range(range_a, range_b, step)]


def generate_output(results):
    """
    tworzy plik wynikowy badania
    :param results: list(Point)
    :return: None
    """
    wb = xwt.Workbook(OUTPUT)
    sh = wb.add_worksheet()

    sh.write('A1', 'x')
    sh.write('B1', 'Newton')
    sh.write('C1', 'IP')

    for a in range(len(results)):
        sh.write('A' + str(a + 2), results[a].val)
        sh.write('B' + str(a + 2), results[a].roots[0])
        sh.write('C' + str(a + 2), results[a].roots[1])

    wb.close()


def examine():
    output_check()
    generate_output(create_points())


if __name__ == '__main__':
    examine()
