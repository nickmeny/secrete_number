import json

# with this .py file we can load the "data base". The "data base" is a .json file
#and we can do things, for example, we can write and load informations : e.x.
#score, users, passwords and more.



def writer(score):
   with open("data_base.json", "w") as f:
      write =  json.dump(score,f)
    


def reader():
  with open("data_base.json", "r") as f:
    write =  json.load(f)
  return write





if __name__ == "__main__":
    reader()