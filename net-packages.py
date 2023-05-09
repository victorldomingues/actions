from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("../") if isfile(join("../", f))]

print("file")
print(onlyfiles)

print("all")
print(listdir("../"))

print("current")
print(listdir("."))