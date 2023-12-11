# from csv_validator import *
# result = read_data("Test.csv")
# print(result)
# print(validate_data(result))

# import Arithmetics as arith

# print(arith.add(2,3))
# print(arith.sub(2,3))
# print(arith.mul(2,3))
# print(arith.div(2,3))

# import merge_files as merge
# merge.merge_files(["t1.txt","t2.txt","t3.txt"],[0,2,1])

import secure_password as sp
password = sp.create_password(16,True,True,True)
print(password)