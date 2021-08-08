import glob
import os
print('welcome to remdup')

files = glob.glob("*_2.jpg")

print("Total files:", len(files))

for f in files:
    print(f)
    os.remove(f)
