def credit(r,n,p,k):

    """function to calculate percent of """
    if r < n * 3:
        print('Мы не можем предоставить вам кредит :(')
    elif r < n * 4:
        n = n * (0.01*p)
        period = n / (k*12)
        print(period)


def main():
    credit(r = int(input('Введите вашу годовую заработную плату:')),
           n = int(input('Введите сумму, запрашиваемую в банке: ')),
           p = float(input('Введите процент по кредиту: ')),
           k = input('Введите предпологаемый период выплаты кредита(лет): '))

if __name__ == '__main__':
    main()