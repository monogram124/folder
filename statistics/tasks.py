import math

# data = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]

# def get_sd(nums):
#     D = 0
#     M = sum(data) / len(data)
#     n = len(data)

#     for i in data:
#         D += (i - M)**2

#     D = D / (n - 1)
#     sd = math.sqrt(D)

#     return sd

# print(get_sd(data))
# def reverse(x: int):
#     if str(x)[0] == "-":
#         x = str(x) - "-"
#         x = "-" + str(x)

#         return x
#     else:
#         print(str(x)[-1])
    
    
# print(reverse("-321"))

# стандартное отклонение
def sd(a: list):
    x = sum(a) / len(a)

    diff = []
    for num in a:
        diff.append((num - x)**2)

    sd = math.sqrt((sum(diff)) / len(a))

    return sd

print(sd([1, 2, 3, 4, 5]))