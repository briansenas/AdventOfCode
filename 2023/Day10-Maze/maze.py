from __future__ import annotations

import argparse
from collections import deque


class Index:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __add__(self, other):
        return Index(self.i + other.i, self.j + other.j)

    def __sub__(self, other):
        return Index(self.i - other.i, self.j - other.j)

    def __neg__(self):
        return Index(-self.i, -self.j)

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __lt__(self, other):
        return self.i < other.i and self.j < other.j

    def __le__(self, other):
        return self.i <= other.i and self.j <= other.j

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.i}:{self.j}"

    def __hash__(self):
        return hash((self.i, self.j))


Displacements = {
    "|": {Index(1, 0), Index(-1, 0)},
    "J": {Index(1, 0), Index(0, 1)},
    "L": {Index(1, 0), Index(0, -1)},
    "7": {Index(-1, 0), Index(0, 1)},
    "F": {Index(-1, 0), Index(0, -1)},
    "-": {Index(0, -1), Index(0, 1)},
    ".": [],
    "S": {Index(i, j) for i in range(-1, 2) for j in range(-1, 2)},
}


class Maze:
    def __init__(self, maze: list[str], position: Index = Index(0, 0)):
        self.maze = maze
        self.position = position
        self.max_value = 0

    def __getitem__(self, index: Index):
        if isinstance(index, int):
            return self.maze[index]
        elif isinstance(index, Index):
            return self.maze[index.i][index.j]
        else:
            raise IndexError

    def __setitem__(self, index: Index, value):
        if isinstance(index, int):
            self.maze[index] = value
        elif isinstance(index, Index):
            self.maze[index.i][index.j] = value
            self.max_value = max(value, self.max_value)
        else:
            raise IndexError

    def move(self, position):
        self.position = position
        return self

    def __len__(self):
        return len(self.maze)

    def __repr__(self):
        return str(self)

    def __str__(self):
        str_copy = ["." for _ in range(len(self.maze))]
        for i in range(len(self.maze)):
            str_copy[i] = ["." for _ in range(len(self.maze[i]))]
            for j in range(len(self.maze[i])):
                if Index(i, j) == self.position:
                    str_copy[i][j] = "H"
                else:
                    str_copy[i][j] = str(self.maze[i][j])
        return "\n".join(["".join(x) for x in str_copy])


def read_file(input_file):
    maze = []
    start_index = Index(0, 0)
    with open(input_file) as file:
        row = 0
        while line := file.readline():
            line = line.strip("\n")
            start_point = line.find("S")
            if start_point != -1:
                start_index = Index(row, start_point)
            maze.append(line)
            row += 1

    return Maze(maze, start_index)


def get_4dof_neighbours(maze, point):
    return filter(
        lambda x: x.i >= 0 and x.i < len(maze) and x.j >= 0 and x.j < len(maze.maze[0]),
        [
            Index(point.i + 1, point.j),
            Index(point.i, point.j + 1),
            Index(point.i - 1, point.j),
            Index(point.i, point.j - 1),
        ],
    )


def can_move_to(maze: Maze, from_: Index, to_: Index):
    for displacement in Displacements[maze[from_]]:
        if Index(0, 0) <= from_ - displacement < Index(len(maze), len(maze.maze[0])):
            if (
                from_ - displacement == to_
                and -displacement in Displacements[maze[to_]]
            ):
                return True
    return False


def transverse_maze(maze):
    neighbours = get_4dof_neighbours(maze, maze.position)
    neighbours = deque(
        filter(lambda x: can_move_to(maze, maze.position, x), neighbours),
    )
    mapped_maze = Maze(
        [[0 for _ in range(len(maze.maze[0]))] for _ in range(0, len(maze))],
        maze.position,
    )
    visited = set()
    visited.add(maze.position)
    for neighb in neighbours:
        mapped_maze[neighb] = 1
    while len(neighbours) > 0:
        neighb = neighbours.popleft()
        visited.add(neighb)
        new_neighs = get_4dof_neighbours(maze, neighb)
        new_neighs = list(filter(lambda x: can_move_to(maze, neighb, x), new_neighs))
        valid_neighs = list(filter(lambda x: x not in visited, new_neighs))
        for valid in valid_neighs:
            mapped_maze[valid] = mapped_maze[neighb] + 1
            neighbours.append(valid)
    return mapped_maze.max_value


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="input.txt")
    parser.add_argument("--part-two", action="store_true")
    input_args = parser.parse_args()
    maze = read_file(input_args.input)
    max_distance = transverse_maze(maze)
    print(max_distance)
