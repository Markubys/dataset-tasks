import random, numpy
from sklearn.linear_model import LinearRegression

def transpose(m):
    return list(map(list, zip(*m)))


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print("\n")


if __name__ == "__main__":
    N = 100
    one_list = [1 for i in range(0, N)]

    x_list = []

    for i in range(0, N):
        x_list.append(random.uniform(0, 1))

    matrix = [x_list, one_list]
    
    y_list = []

    for i in range(0, N):
        y_list.append(random.randint(10, 100))

    t_matrix = transpose(matrix)

    two_x_two = numpy.matmul(matrix, t_matrix)
    two_x_two_inv = numpy.linalg.inv(two_x_two)
    two_x_one = numpy.matmul([y_list], t_matrix)
    a_b = numpy.matmul(two_x_one, two_x_two_inv)
    
    reg = LinearRegression().fit(numpy.array(y_list).reshape(-1, 1), numpy.array(x_list).reshape(-1, 1))
    print(f"a = {reg.coef_[0][0]}, b = {reg.intercept_[0]}")