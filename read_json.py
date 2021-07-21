import json
from os import write


student = {
    "age": 4,
    "name": "nick"
}

def reader():
    with open("data_base.json", "w") as f:
      write =  json.dump(student,f)














if __name__ == "__main__":
    reader()