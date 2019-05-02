def is_luhn_valid(n):
    evens = []
    odds = []
    doubled_evens = []
    doubled_odds = []

    listed = list(str(n))

    if len(listed) % 2 == 0:
        for index in range(1, len(listed), 2):
            evens.append(int(listed[index]))
        for index in range(0, len(listed), 2):
            if int(listed[index]) * 2 > 9:
                doubled_odds.append(int(listed[index]) * 2 - 9)
            else:
                doubled_odds.append(int(listed[index]) * 2)
        if (sum(evens) + sum(doubled_odds)) % 10 == 0:
            return True
        else:
            return False
    else:
        for index in range(0, len(listed), 2):
            odds.append(int(listed[index]))
        for index in range(1, len(listed), 2):
            if int(listed[index]) * 2 > 9:
                doubled_odds.append(int(listed[index]) * 2 - 9)
            else:
                doubled_evens.append(int(listed[index]) * 2)
        if (sum(odds) + sum(doubled_evens)) % 10 == 0:
            return True
        else:
            return False
