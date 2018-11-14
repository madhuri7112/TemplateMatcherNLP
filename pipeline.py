
def pipeline(data):


with open("data") as data_file:
    data = json.loads(data_file.read())

pipeline(data)