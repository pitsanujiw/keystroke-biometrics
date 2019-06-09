import json
import glob

def write2json(write_data, path):
    with open(path, "w") as files:
        json.dump(write_data, files)
        print(path + " -> write success")

def cal_ngram(ngram, pressed, released):
    length = len(pressed)
    result = []
    for i in range(0, length-ngram, ngram):
        result.append(abs(released[i]-pressed[i+ngram]))
    return result

def cal_duration(pressed, released):
    length = len(pressed)
    result = []
    for i in range(length):
        result.append(abs(released[i]-pressed[i]))
    return result

def new_json(read_data, name):
    write_data = {}

    write_data.update({"name": name})
    write_data.update({"article": data_name})
    write_data.update({"keyCode": read_data["KeyCode"]})
    write_data.update({"keyPressed": read_data["KeyPressed"]})
    write_data.update({"keyReleased": read_data["KeyReleased"]})
    for i in range(1, 6):
        write_data.update({str(i)+"gram":cal_ngram(i, read_data["KeyPressed"], read_data["KeyReleased"])})
    write_data.update({"duration": cal_duration(read_data["KeyPressed"], read_data["KeyReleased"])})

    return write_data

data_name = "th_breakfast"

read_path = "data\\th2\\templete\\*.json"
files = glob.glob(read_path)

write_path = "new_data\\th2\\templete\\"

for file_name in files:
    with open(file_name) as files:
        read_data = json.load(files)

    name = file_name[file_name.find("_")+1:file_name.rfind("_")]
    write_data = new_json(read_data, name)

    # print(write_path + name + ".json")
    name = file_name[file_name.find("_")-2:file_name.rfind("_")]
    write2json(write_data, write_path + name + ".json")