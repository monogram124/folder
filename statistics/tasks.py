# import math

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
def reverse(x: int):
    if str(x)[0] == "-":
        x = str(x) - "-"
        x = "-" + str(x)

        return x
    else:
        print(str(x)[-1])
    
    
print(reverse("-321"))