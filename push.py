import os

for i in range(9,-1,-1):
  for j in range(0,10):
    ii = str(i)
    jj = str(j)
    if i == 0:
      ii = ""
    print("pushing file " + ii + jj + " now...")
    try:
      os.system("git add for_cones/" + ii + jj + "*.ivy")
      os.system("git commit -m 'make cone 1'")
      os.system("git push origin main")
    except FileNotFoundError:
      print("not found")

for i in range(9,-1,-1):
  for j in range(0,10):
    ii = str(i)
    jj = str(j)
    if i == 0:
      ii = ""
    print("pushing folder " + ii + jj + " now...")
    try:
      os.system("git add for_cones/" + ii + jj + "*/*")
      os.system("git commit -m 'make cone 1'")
      os.system("git push origin main")
    except FileNotFoundError:
      print("not found")


