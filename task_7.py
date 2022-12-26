import random, math, numpy


def polynomial_regression(x_mattr, y_list):
    xt_x = numpy.dot(numpy.array(x_mattr), numpy.array(x_mattr).T)
    xt_x_inv = numpy.linalg.inv(xt_x)
    xt_y = numpy.matmul(numpy.array(y_list), numpy.array(x_mattr).T)
    x_p = numpy.dot(xt_x_inv, xt_y)

    return x_p


if __name__ == "__main__":
    N = 60
    x_list = []

    for i in range(0, N):
        x_list.append(random.randint(100, 2000))

    x_list = sorted(x_list)
    
    one_list = [1 for i in range(0, N)]

    x_2_list = [math.pow(x, 2) for x in x_list]
    x_3_list = [math.pow(x, 3) for x in x_list]
    x_4_list = [math.pow(x, 4) for x in x_list]

    x_mattr = [one_list, x_list, x_2_list, x_3_list, x_4_list]
    y_list = [5 * math.sin(x/250) + random.uniform(0,1) for x in x_list]


    x_p_1 = polynomial_regression(x_mattr , y_list)
    x_p_2 = polynomial_regression(x_mattr[0:4], y_list)
    x_p_3 = polynomial_regression(x_mattr[0:3], y_list)

    print(f"X_P_1:{x_p_1}")
    print(f"X_P_2:{x_p_2}")
    print(f"X_P_2:{x_p_3}")