import random, numpy, math
from sklearn.linear_model import LinearRegression


if __name__ == "__main__":
    N = 40

    y_list = []
    y_lg_list = []

    for i in range(0, N):
        y = random.uniform(0, 1)
        y_list.append(y)
        y_lg_list.append(math.log(y, math.e))

    x_list = []
    x_lg_list = []

    for i in range(0, N):
        x = random.randint(10, 1000)
        x_list.append(x)
        x_lg_list.append(math.log(x, math.e))


    y_avg = sum(y for y in y_list) / len(y_list)


    y_diff = sum(math.pow(y - y_avg, 2) for y in y_list)


    reg_lg = LinearRegression().fit(numpy.array(sorted(x_lg_list)).reshape(-1, 1), numpy.array(sorted(y_list)).reshape(-1, 1))

    print("Lg regression:")
    print(f"a = {reg_lg.coef_[0][0]}, b = {reg_lg.intercept_[0]}")

    
    reg_exp = LinearRegression().fit(numpy.array(sorted(x_list)).reshape(-1, 1), numpy.array(sorted(y_lg_list)).reshape(-1, 1))
    
    print("Exponential regression:")
    print(f"a = {reg_exp.coef_[0][0]}, b = {reg_exp.intercept_[0]}") 

    reg_degree = LinearRegression().fit(numpy.array(sorted(x_lg_list)).reshape(-1, 1), numpy.array(sorted(y_lg_list)).reshape(-1, 1))
    
    print("Degree regression:")
    print(f"alpha = {reg_degree.coef_[0][0]}, beta = {reg_degree.intercept_[0]}") 
    print(f"a = {math.pow(math.e, reg_degree.intercept_[0])}, b = {reg_degree.coef_[0][0]}")