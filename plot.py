#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys


# TODO Esto debería leer un cuaternión y dibujarlo.
def updatePlot(data: str) -> None:
    print(data, end='')


def main() -> None:
    for line in sys.stdin:
        updatePlot(line)


if __name__ == '__main__':
    main()
