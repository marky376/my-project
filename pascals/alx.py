def pascal_triangle(n):
    res = []
    if n <= 0:
        for i in range(1, n+1):
            level = []
            B =`1
            for j in range(1, i+1):
                level.append(B)
                B = B * (i - j) // j
            res.append(level)    `
        return res