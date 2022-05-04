import os
import time
import random

#Did the ivy_check action return an error?
def check_failed(file_name):
  with open(file_name, 'r') as read_obj:
    for line in read_obj:
      if "error:" in line:
        print("IVY RETURNED ERROR")
        return True
      if "not found: " in line:
        print("IVY RETURNED NOT FOUND")
        return True
  return False

#Did the ivy_check action return a passing trace?
def check_pass(file_name):
  with open(file_name, 'r') as read_obj:
    for line in read_obj:
      if "PASS" in line:
        return True
  return False

class Node:
  #Create a node:
  def __init__(self, data):
    self.children = []
    self.data = data
  #Add a child to a node:
  def add_kid(self, newNode):
    self.children.append(newNode)

def print_tree(root, ofile):
  path = []
  print("printing tree!")
  print_rec(root, path, 0, ofile)

def print_rec(node, path, path_len, ofile):
  if node is None:
    return
  
  if (len(path) > path_len):
    path[path_len] = node.data
  else:
    path.append(node.data)
  
  if (len(node.children) == 0):
    print_path(path, ofile)
  else:
    for child in node.children:
      print_rec(child,path, path_len + 1, ofile)

def print_path(path, cone):
  # with open(ofile, 'a') as cone:
  for i in range(2, len(path)):
    cone.write(str(path[i]) + " ")
  cone.write("\n")

#Welcome and initialization
print("LET'S MAKE SOME CONES! Your folder options are:")
path = '.'
directory_contents = os.listdir(path)
for item in directory_contents:
  if os.path.isdir(item):
    print(item)
print("")

foldername = input("Input the name of the folder: ")

#Initialize the backward folder elements
print("Now building the cone. This may take a few minutes.")
root = Node("")
finished = False
index = 0
log = open(foldername + "/log.txt")

#Use the lines from the log (created earlier) to get more paths
for logline in log: 
  
  #Housekeeping
  tracefile = foldername + "/" + str(index) + ".txt"
  if check_failed(tracefile):
    print("\033[0;30;41mFAILURE: IVY ERROR!!! Big oops.\033[0m")
    exit()
  elif check_pass(tracefile):
    print("Finishd item " + str(index - 1) + ".")
    if index == 0:
      print("\033[0;30;42mNOTHING FOUND!\033[0m")
    break
  
  #Set up folders and files
  bfolder = foldername + "/" + str(index)

  #Housekeeping
  subindex = 0
  finished = False

  #Find all the backward-steps up to k away
  while True:
    
    #Check in IVy
    tracefile = bfolder + "/" + str(subindex) + "_abr.txt"
    if not(os.path.isfile(tracefile)):
      # finished = True
      break
    #Check for errors or passing 
    elif check_failed(tracefile):
      print("\033[0;30;41mFAILURE: IVY ERROR!!! Big oops.\033[0m")
      exit()
    elif check_pass(tracefile):
      print("Testing has completed.")
      if subindex == 0:
        print("\033[0;30;42mNOTHING FOUND 2!\033[0m")
      # finished = True
      break

    #Add to the cone
    with open(tracefile) as abr:
      currstate = root
      for abrline in abr:
        newkid = True
        transition = abrline.replace("\n","").split()[10][1:-1].replace(".","_")
        for child in currstate.children:
          if transition in child.data:
            currstate = child
            newkid = False
            break
        if newkid:
          currstate.add_kid(Node(transition))
          currstate = currstate.children[len(currstate.children) - 1]

    subindex = subindex + 1

  index = index + 1
log.close()

#Write the cone and wrap up

with open(foldername + "/conefile_allstates.txt", 'w') as conefile:
  conefile.write("")
  print_tree(root, conefile)



# with open(foldername + "/conefile_allstates.txt", 'w') as conefile:
#   conefile.write(print_tree(root))

print("FINISHED!")
print("\n\n###################################################################################")
print("###################################################################################")
print("###################################################################################\n\n")
