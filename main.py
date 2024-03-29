red = "\033[31m"
blue = "\033[34m"
white = "\033[37m"
green = "\033[32m"
purple = "\033[35m"
yellow = "\033[33m"
reset = "\033[0m"

viewlist = []
title = f"{red}={blue} ToDo List Manager {red}={reset}"
print(f"{title: ^60}")
print()

def printList():
  print() 
  for item in viewlist:
    print(f"{yellow}{item}{reset}")
  print() 

while True:
  options = input("Do you want view, add or edit ToDo list?: ")
  if options == "view":
    printList()
  elif options == "add":
    item = input("What would you like to ADD to ToDo list?: ")
    viewlist.append(item)
  elif options == "remove":
    reitem = input("What would you like to REMOVE to ToDo list?: ")
    if reitem in viewlist:
      viewlist.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()

