#!/usr/bin/env python3

import numpy as np
import sys


# TODO Esto debería leer un ángulo de euler y dibujarlo.
def updatePlot(data: np.ndarray) -> None:
    print(data, end='')


def main() -> None:
    for line in sys.stdin:
        updatePlot(np.fromstring(line, count = 3, sep=','))


if __name__ == '__main__':
    main()