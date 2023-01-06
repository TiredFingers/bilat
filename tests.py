

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
