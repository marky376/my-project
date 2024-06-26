#!/usr/bin/python3

def generate_row(n):
    row = [1]
    for k in range(1, n):
        row.append(row[-1] * (n - k) // k)
    return row


print(generate_row(5))
