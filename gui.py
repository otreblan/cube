#!/usr/bin/env python3

from sys import stdin
from pyrr import Vector3, geometry
from typing import List, Tuple, Any

import matplotlib.pyplot as plt
import numpy as np

def plot_vertex(data: List[Vector3]) -> None:
    for vertex in data:
        plt.plot(vertex.x, vertex.y, 'bo')

def plot_edges(data: List[Tuple[Vector3, Vector3]]) -> None:
    print(data)


def plot_cube(cube: Tuple[np.ndarray, Any], rotation: Vector3) -> None:
    # TODO Proyección
    # TODO Rotación

    # Vértices
    plot_vertex([Vector3(v) for v in cube[0]])

    # TODO Aristas

def update_plot(data: Vector3) -> None:
    plot_cube(geometry.create_cube(), data)

    plt.show()

def main() -> None:
    for line in stdin:
        update_plot(Vector3(np.fromstring(line, count = 3, sep=',')))


if __name__ == '__main__':
    main()
