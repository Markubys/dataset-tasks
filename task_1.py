import random, numpy, math


def get_average(dataset :list) -> float:
    return sum(dataset)/len(dataset)


def get_dispersion_1(dataset :list) -> float:
    return numpy.var(dataset)


def get_dispersion_2(dataset :list, average :float) -> float:
    return sum((xi - average) ** 2 for xi in dataset) / len(dataset)


def get_std_1(dataset :list) -> float:
    return numpy.std(dataset)


def get_std_2(dispersion :float) -> float:
    return math.sqrt(dispersion)


def get_coef_var(std :float, average : float) -> float:
    return std / average


if __name__ =="__main__":
    dataset = []

    for i in range(0, 50):
        dataset.append(round(random.uniform(0, 1), 14))

    average = get_average(dataset)
    dispersion_1 = get_dispersion_1(dataset)
    dispersion_2 = get_dispersion_2(dataset, average)
    std_1 = get_std_1(dataset)
    std_2 = get_std_2(dispersion_2)
    coef_var = get_coef_var(std_2, average)

    print(f"Average = {average}")
    print(f"Dispersion = {dispersion_2}")
    print(f"Std = {std_2}")
    print(f"Coef var = {int(round(coef_var, 2) * 100)}%")

