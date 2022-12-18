import random, numpy, math


def get_covariation_1(dataset :list):
    return numpy.cov(dataset[0], dataset[1])


def get_covariation_2(dataset :list):
    avg_x = sum(dataset[0]) / len(dataset[0])
    avg_y = sum(dataset[1]) / len(dataset[1])

    return sum((xi- avg_x)*(yi - avg_y) for (xi, yi) in zip(dataset[0], dataset[1])) / len(dataset[0])


def get_coef_correlation_1(dataset :list):
    return numpy.corrcoef(dataset[0], dataset[1])


def get_coef_correlation_2(dataset :list, cov) -> float:
    avg_x = sum(dataset[0]) / len(dataset[0])
    avg_y = sum(dataset[1]) / len(dataset[1])
    std_1 = numpy.std(dataset[0])
    std_2 = numpy.std(dataset[1])
    std_x =  math.sqrt(sum((xi - avg_x) ** 2 for xi in dataset[0]) / len(dataset[0]))
    std_y =  math.sqrt(sum((yi - avg_y) ** 2 for yi in dataset[1]) / len(dataset[1]))

    return cov / (std_1 * std_2)


if __name__ =="__main__":
    dataset_1 = []
    dataset_2 = []

    for i in range(0, 50):
        dataset_1.append(round(random.uniform(0, 1), 14))
    
    for i in range(0, 50):
        dataset_2.append(round(random.uniform(0, 1), 14))

    dataset = [dataset_1, dataset_2]

    cov_1 = get_covariation_1(dataset)
    cov_2 = get_covariation_2(dataset)
    coef_cor_1 = get_coef_correlation_1(dataset)
    coef_cor_2 = get_coef_correlation_2(dataset, cov_2)

    print(f"Covariation = {cov_2}")
    print(f"Correlation = {coef_cor_2}")
