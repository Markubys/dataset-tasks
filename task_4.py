import numpy, random

def get_x(matrix, b):
    return numpy.linalg.inv(matrix).dot(numpy.array(b))


if __name__ == "__main__":
    matrix = []
    N = 7
    M = 7

    for i in range(0, N):
        row = []
        for j in range(0, M):
            row.append(random.randint(-10, 10))
        matrix.append(row)

    b = []
    for i in range(0, N):
        b.append(random.randint(-10, 10))

    x_list = get_x(matrix, b)
    
    for i, x in enumerate(x_list):
        print(f"X{i+1} = {x}")