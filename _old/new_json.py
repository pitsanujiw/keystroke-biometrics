import json

path = "data\\th2\\templete\\32_NUTTAWUT_TH2.json"

with open(path) as f:
    data = json.load(f)

for i in data:
    print(str(i) + " " + str(len(data[i])))