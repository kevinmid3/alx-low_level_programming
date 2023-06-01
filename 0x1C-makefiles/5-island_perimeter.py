#!/usr/bin/python3
""" Defines Island Perimeter """

def island_perimeter(grid):
    """ Calculate perimeter of grid """
    p_meter = 0
    for k in range(len(grid)):
        for m in range(len(grid[0])):
            if grid[k][m] == 1:

                if k == 0 or grid[k - 1][m] == 0:
                    p_meter += 1

                if k == (len(grid) - 1) or grid[k + 1][m] == 0:
                    p_meter += 1

                if m == 0 or grid[k][m - 1] == 0:
                    p_meter += 1

                if m == (len(grid[0]) - 1) or grid[k][m + 1] == 0:
                    p_meter += 1
    return p_meter
