import random, numpy

def get_matrix_minor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def get_matrix_deternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*get_matrix_deternminant(get_matrix_minor(m,0,c))
    return determinant


def get_numpy_determinant(m):
    return numpy.linalg.det(m)


def transpose(m):
    return list(map(list, zip(*m)))


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print("\n")


def get_x(matrix, b):
    det = get_matrix_deternminant(matrix)

    local_det = []
    for i in range(0, N):
        m = transpose(matrix)
        m[i] = b
        m = transpose(m)

        local_det.append(get_matrix_deternminant(m))

    x = []

    for l_d in local_det:
        x.append(l_d / det)

    return x

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


    det = get_matrix_deternminant(matrix)
    det_numpy = get_numpy_determinant(matrix)

    x_list = get_x(matrix, b)

    for i, x in enumerate(x_list):
        print(f"X{i+1} = {x}")