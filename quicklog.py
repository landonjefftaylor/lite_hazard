import os

with open("for_cones/log.txt",'w') as log:
  for i in range(0,5060):
    log.write(str(i) + "\n")
