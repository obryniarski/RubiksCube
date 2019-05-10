
import utils

class Side:

    def __init__(self, dimension, grid):
        self.dimension = dimension
        self.grid = grid
        assert len(self.grid) == dimension
        for i in range(self.dimension):
            assert len(self.grid[i]) == dimension

    def get_column(self, num):
        return self.grid[num]

    def get_row(self, num):
        return [self.grid[val][num] for val in range(self.dimension)]

    def __str__(self):
        res = ""
        for i in range(self.dimension):
            for val in self.get_row(self.dimension - i - 1):
                res += str(val) + " "
            res += "\n"
        return res


class Cube:

    def __init__(self, white_side, red_side, blue_side, green_side, orange_side, yellow_side):
        self.bottom_side = white_side
        self.front_side = red_side
        self.left_side = blue_side
        self.right_side = green_side
        self.back_side = orange_side
        self.top_side = yellow_side
        utils.assert_matching_dimensions(self.bottom_side, self.front_side, self.left_side, self.right_side,
                                         self.back_side, self.top_side)

        self.dimension = self.bottom_side.dimension

    def __str__(self):
        res = ""
        for i in range(self.dimension):
            res += "  " * self.dimension + " "
            for val in self.top_side.get_row(self.dimension - i - 1):
                res += str(val) + " "
            res += "  " * self.dimension * 2
            res += "\n"
        res += "\n"
        for i in range(self.dimension):
            for val in self.left_side.get_row(self.dimension - i - 1):
                res += str(val) + " "
            res += " "
            for val in self.front_side.get_row(self.dimension - i - 1):
                res += str(val) + " "
            res += " "
            for val in self.right_side.get_row(self.dimension - i - 1):
                res += str(val) + " "
            res += " "
            for val in self.back_side.get_row(self.dimension - i - 1):
                res += str(val) + " "
            res += "\n"
        res += "\n"
        for i in range(self.dimension):
            res += "  " * self.dimension + " "
            for val in self.bottom_side.get_row(self.dimension - i - 1):
                res += str(val) + " "
            res += "  " * self.dimension * 2
            res += "\n"

        return res

column = ['r', 'g', 'y', 'b']
side_example = Side(4, [column] * 4)
print(side_example.get_row(1))
print(side_example)


# utils.assert_matching_dimensions(side_example, side_example, side_example, side_example, side_example, side_example)

cube_example = Cube(side_example, side_example, side_example, side_example, side_example, side_example)
print(cube_example)
