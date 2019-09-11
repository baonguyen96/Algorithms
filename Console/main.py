from IntroductionToAlgorithm3E.Chapter5.random_generator import get_random_number_advance


def main():
    a = 10
    b = 100

    for i in range(20):
        rand = get_random_number_advance(a, b)
        print(rand)


if __name__ == '__main__':
    main()
