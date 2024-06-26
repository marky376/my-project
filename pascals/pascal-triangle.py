#!/usr/bin/python3

def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        if i == 0:
            row = [1]
        else:
            row = [1] + [triangle[i-1][j-1] + triangle[i-1][j] for j in range(1, i)] + [1]
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(row)


# Generate and print Pascal's Triangle with 5 rows
triangle = generate_pascals_triangle(20)
print_pascals_triangle(triangle)

