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

def view(data: List[Vector3], mat: np.ndarray) -> List[Vector4]:
    return [
        Vector4(
            matrix44.apply_to_vector(
                vec=Vector4.from_vector3(v), mat=mat
            )
        )
        for v in data
    ]

def project(data: List[Vector4], projection: np.ndarray) -> List[Vector3]:
    #return data
    return [
        Vector3.from_vector4(Vector4(
            matrix44.apply_to_vector(
                vec=v, mat=projection
            )
        ))[0]
        for v in data
    ]


def plot_cube(cube: Tuple[np.ndarray, Any], rotation: Vector3) -> None:
    rot_mat = matrix33.create_from_eulers(rotation)
    view_mat = matrix44.create_look_at(
        eye=Vector3([-10,0,0]),
        target=Vector3([0,0,0]),
        up=Vector3([0,1,0])
    )
    pro_mat = matrix44.create_perspective_projection(
        fovy=20,
        aspect=1,
        near=0.01,
        far=10
    )

    # Rotación
    rotated = rotate([Vector3(v) for v in cube[0]], rot_mat)

    # View
    viewed = view(rotated, view_mat)

    # Proyección
    projected = project(viewed, pro_mat)

    # Vértices
    plot_vertex(projected)

    # Aristas
    plot_edges([(projected[i[0]], projected[i[1]]) for i in edges])

def update_plot(data: Vector3) -> None:
    plt.clf()
    plot_cube(geometry.create_cube(), data)

    plt.axis('equal')
    plt.axis([-10,10,-10,10])


def get_rotation():
    for line in stdin:
        yield Vector3(np.fromstring(line, count = 3, sep=','))


def main() -> None:
    fig = plt.figure()

    anim = animation.FuncAnimation(
        fig,
        func=update_plot,
        frames=get_rotation,
        repeat=False
    )

    plt.show()


if __name__ == '__main__':
    main()
