#myfile = open("fruits.txt")
#content = myfile.read()
#myfile.close()

"""with open("fruits.txt") as myfile:
    content = myfile.read()

print(content)"""

import os
import time
import pandas

# while True:
#     if os.path.exists("fruits.txt"):
#         with open("fruits.txt") as file:
#             print(file.read())
#     else:
#         print("File does not extist")
#     time.sleep(10)    

#with open("data.txt", "a+") as myfile:
#    myfile.seek(0)
#    content = myfile.read()
#    myfile.write("\n"+content)
#    myfile.write("\n"+content)

while True:
    if os.path.exists("temps_today.csv"):
        data = pandas.read_csv("temps_today.csv")
        print(data.mean())
        print(data.mean()["st1"])
    else:
        print("File does not extist")
    time.sleep(10)