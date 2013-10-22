def romafy(num):

    if num < 5:
        if num == 4:
            return 'IV'
        else:
            return 'I' * num

    if num == 5:
        return 'V'

    if num < 10:
        if num == 9:
            return 'IX'
        else:
            return 'V' + ('I' * (num - 5))

    if num == 10:
        return 'X'

    if num < 50:
        if num == 40:
            return 'XL'
        else:
            return 'X' * (num/10)

    if num == 50:
        return 'L'

    if num < 100:
        if num == 90:
            return 'XC'
        else:
            return 'L' + ('X' * ((num - 50)/10))

    if num == 100:
        return 'C'

    if num < 500:
        if num == 400:
            return 'CD'
        else:
            return 'C' * (num/100)

    if num == 500:
        return 'D'

    if num < 1000:
        if num == 900:
            return 'CM'
        else:
            return 'D' + ('C' * ((num - 500)/100))

    return 'M' * (num/1000)


def dec2rom(dec):
    digits = str(dec)
    orders = []

    for i in xrange(len(digits)):
        n = int(digits[i])
        p = 10 ** (len(digits) - i - 1)
        orders.append(n * p)

    return ''.join(map(romafy, orders))

