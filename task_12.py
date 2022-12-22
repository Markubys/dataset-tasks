import random, numpy, math

if __name__ == "__main__":
    N = 500

    dx = 0.01
    x0 = -2.5
    t = 5

    x_list = [round(i, 2) for i in numpy.arange(-t/2, t/2 + 0.01, 0.01)] 
    y_list = [math.sin(2 * math.pi * (x/t)) * math.cos(2 * math.pi * 3 * (x/t) + random.uniform(0, 0.1)) for x in x_list] 
    
    a0 = 2 * sum(y *dx for y in y_list) / t
    a1 = 2 * sum(y * math.cos(2 * math.pi * x / t) * dx for (x, y) in zip(x_list, y_list)) / t 
    b1 = 2 * sum(y * math.sin(2 * math.pi * x / t) * dx for (x, y) in zip(x_list, y_list)) / t
    a2 = 2 * sum(y * math.cos(2 * math.pi * 2 * x / t) * dx for (x, y) in zip(x_list, y_list)) / t
    b2 = 2 * sum(y * math.sin(2 * math.pi * 2 * x / t) * dx for (x, y) in zip(x_list, y_list)) / t

    model = []

    for x in x_list:
        model.append(a0 / 2 + a1 * math.cos(2 * math.pi * x / t) + 
        b1 * math.sin(2 * math.pi * x / t) + a2 * math.cos(2 * math.pi * 2 * x / t) + b2 * math.sin(2 * math.pi * 2 * x / t))

    y_diff = sum(math.pow(y - m, 2) for (y, m) in zip(y_list, model))

    print(f"Sum of squared deviations from calculated = {y_diff}")