#!/usr/bin/env python3

from sys import stdin
from matplotlib import animation
from pyrr import Vector3, Vector4, geometry, matrix33, matrix44
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

def plot_vertex(data: List[np.ndarray]) -> None:
    for vertex in data:
        plt.plot(vertex[0], vertex[1], 'bo')

def plot_edges(data: List[Tuple[np.ndarray, np.ndarray]]) -> None:
    for edge in data:
        plt.plot([v[0] for v in edge], [v[1] for v in edge])

def plot_cube(cube: Tuple[np.ndarray, Any], rotation: Vector3) -> None:
    rot_mat = matrix44.create_from_eulers(rotation)
    view_mat = matrix44.create_look_at(
        eye=Vector3([-2,0,0]),
        target=Vector3([0,0,0]),
        up=Vector3([0,1,0])
    )
    pro_mat = matrix44.create_perspective_projection(
        fovy=40,
        aspect=1,
        near=0.01,
        far=10
    )

    # Proyección
    projected = [
        matrix44.apply_to_vector(mat=pro_mat, vec=
            matrix44.apply_to_vector(mat=view_mat, vec=
                matrix44.apply_to_vector(mat=rot_mat, vec=v)
            )
        )
        for v in cube[0]
    ]

    # Vértices
    plot_vertex(projected)

    # Aristas
    plot_edges([(projected[i[0]], projected[i[1]]) for i in edges])

def update_plot(data: Vector3) -> None:
    plt.clf()
    plot_cube(geometry.create_cube(), data)

    plt.axis('equal')
    plt.axis([-3,3,-3,3])


def get_rotation():
    for line in stdin:
        yield Vector3(np.fromstring(line, count = 3, sep=','))


def main() -> None:
    fig = plt.figure()

    anim = animation.FuncAnimation(
        fig,
        func=update_plot,
        frames=get_rotation,
        repeat=False,
        interval=1,
        save_count=0,
        cache_frame_data=False
    )

    plt.show()


if __name__ == '__main__':
    main()
