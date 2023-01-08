

def test_sma_is_decimal():

    import decimal
    from bilat.sma import sma

    data = [10, 10, 12, 324, 12, 11, 124, 555, 222, 847, 8, 10, 10, 12, 324, 12, 11, 124, 555, 222, 847, 8, 88, 232,
               11]

    res = sma(data)

    assert isinstance(res, decimal.Decimal)


def test_sma_float_window():

    from bilat.sma import sma

    data = [10, 10, 12, 324, 12, 11, 124, 555, 222, 847, 8, 10, 10, 12, 324, 12, 11, 124, 555, 222, 847, 8, 88, 232,
            11, 232, 55, 87]

    for i in range(3):
        assert sma(data, length=25, shift=i) == sum(data[i:25+i]) / len(data[i:25+i])


def test_ema():

    from bilat.ema import ema

    data = [
        10254.92, 10171.06, 9998.87, 10010.53, 9706.93, 8499.75, 8436.75, 8067.78, 8187.15, 8206.39
    ]

    correct_ema = [
        0, 10254.92, 10171.06, 9998.87, 10010.53, 9706.93, 8499.75, 8436.75, 8067.78, 8187.15, 8206.39
    ]

    ema_list = [0]

    for chart in data:
        ema_list.append(ema(chart, ema_list[-1]))

    for aema, cema in zip(correct_ema, ema_list):

        assert aema == cema
