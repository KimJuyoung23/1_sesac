# # import my_package.math_operations as math_operations
# # import 패키지.모듈 as 별칭
# from my_package import math_operations as mo
# # from 패키지 import 모듈 as 별칭

# result = mo.add(3, 5)
# print(result) # 출력: 8

# result = mo.multiply(4, 6)
# print(result) # 출력: 24

from my_package.math_operations import basic_operations, advanced_operations

result = basic_operations.add(3, 5)
print(result) # 출력: 8
result = advanced_operations.square(4)
print(result) # 출력: 16