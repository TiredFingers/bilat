import decimal


def ema(today, pema, days=1, smooth=2) -> decimal.Decimal:
    return (today * (smooth / (1+days))) + pema * (1 - (smooth / (1+days)))


if __name__ == '__main__':

    data = [
        10254.92, 10171.06, 9998.87, 10010.53, 9706.93, 8499.75, 8436.75, 8067.78, 8187.15, 8206.39
    ]

    ema_list = [0]

    for chart in data:

        ema_list.append(ema(chart, ema_list[-1], smooth=2))

    print(ema_list)

