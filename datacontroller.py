import json



# with this .py file we can load the "data base". The "data base" is a .json file
#and we can do things, for example, we can write and load informations : e.x.
#score, users, passwords and more.


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def create():
  with open("base.json", "w") as f:
    try:
      json.dump(0,f)
      print(colored(51,251,51,"DATABASE CREATED SUCCESSFUL"))
    except:
       print(colored(162,12,12,"DATABASE FAILED TO CEATED"))




       


def writer(score):
   with open("base.json", "w") as f:
      write =json.dump(score,f)
    

def reader():
  with open("base.json") as r:
   load = json.load(r)
  return load





if __name__ == "__main__":
  reader()