#!/usr/bin/env python3

from sys import stdin
from pyrr import Vector3, geometry, matrix33
from typing import List, Tuple, Any

import matplotlib.pyplot as plt
import numpy as np

def side_edge(side: int) -> List[Tuple[int, int]]:
    offset = side*4

    return [(e[0]+offset, e[1]+offset) for e in [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
    ]]

edges: List[Tuple[int, int]] = [e for s in range(6) for e in side_edge(s)]

def plot_vertex(data: List[Vector3]) -> None:
    for vertex in data:
        plt.plot(vertex.x, vertex.y, 'bo')

def plot_edges(data: List[Tuple[Vector3, Vector3]]) -> None:
    for edge in data:
        plt.plot([v.x for v in edge], [v.y for v in edge])


def rotate(data: List[Vector3], rotation: np.ndarray) -> List[Vector3]:
    return [
        Vector3(matrix33.apply_to_vector(vec=v, mat=rotation))
        for v in data
    ]


def plot_cube(cube: Tuple[np.ndarray, Any], rotation: Vector3) -> None:
    rot_mat = matrix33.create_from_eulers(rotation)

    # Rotación
    rotated = rotate([Vector3(v) for v in cube[0]], rot_mat)

    # TODO Proyección

    # Vértices
    plot_vertex(rotated)

    # Aristas
    plot_edges([(rotated[i[0]], rotated[i[1]]) for i in edges])

def update_plot(data: Vector3) -> None:
    plot_cube(geometry.create_cube(), data)

    plt.show()

def main() -> None:
    for line in stdin:
        update_plot(Vector3(np.fromstring(line, count = 3, sep=',')))


if __name__ == '__main__':
    main()
