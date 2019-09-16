# import math
# def isPP(n):
#     for base in range(2, n):
#         for power in range(0, math.ceil(math.log(n, base)) + 1):
#             print(str(base) + " raised to " + str(power))
#             if base**power == n:
#                 return [base, power]

# import math
# def isPP(n):
#     for base in range(2, n):
#         for power in range(0, int(math.log(n, 2)) + 5):
#             print(str(base) + " raised to " + str(power))
#             if base**power == n:
#                 return [base, power]

import math
def isPP(n):
    for base in range(2, n):
        power = math.log(n, base)
        if math.isclose(power, round(power), abs_tol=0.01):
            return([base, round(power)])

print(isPP(243))
