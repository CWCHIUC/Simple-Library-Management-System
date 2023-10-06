import json

# Books Class retrieving from json file
class Books():
  def __init__(self):
    pass

  def init(self):
    with open('json/books.json') as database:
      database = json.load(database)
    return(database)

# DVD Class retrieving from json file
class DVD():
  def __init__(self):
    pass

  def init(self):
    with open('dvd.json') as database:
      database = json.load(database)
    return(database)