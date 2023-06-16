from fractions import Fraction
from sympy import *
from matplotlib import mlab
import numpy
import math
from sqr import *
# from PyQt5 import uic
# from PyQt5.QtWidgets import QApplication
#
# Form, Window = uic.loadUiType("GUI.ui")
#
# app = QApplication([])
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
# app.exec()


def integral(fun, a, b, n=100):
    print(fun)
    print(type(fun))
    result = 0.0
    step = (b - a) / n
    for x in numpy.arange(a, b - step, step):
        result = result + step * fun(x + step / 2)
    return result


def main():
    func = input("Введите функцию: y = ")
    a = float(input("a = "))
    b = float(input("b = "))
    # s = integral(lambda x: eval(func), a, b)
    # print(f"S={s}")
    result = 0.0
    step = (b - a) / 400
    for x in numpy.arange(a, b, step):
        result = result + step * eval(func)
    print(result)
if __name__ == '__main__':
    main()

