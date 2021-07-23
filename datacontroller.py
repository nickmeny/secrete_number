import json



# with this .py file we can load the "data base". The "data base" is a .json file
#and we can do things, for example, we can write and load informations : e.x.
#score, users, passwords and more.




def create():
     with open("base.json", "w") as f:
       json.dump(0,f)
       


def writer(score):
   with open("base.json", "w") as f:
      write =json.dump(score,f)
    

def reader():
  with open("base.json") as r:
   load = json.load(r)
  return load





if __name__ == "__main__":
  reader()