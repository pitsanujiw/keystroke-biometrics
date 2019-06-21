import glob
import json

def modified(read_data, keyCode_len):
    # check_length(read_data)
    if len(read_data['keyCode']) > keyCode_len:
        read_data['keyCode'] = read_data['keyCode'][0:keyCode_len]
        read_data['keyPressed'] = read_data['keyPressed'][0:keyCode_len]
        read_data['keyReleased'] = read_data['keyReleased'][0:keyCode_len]
    elif len(read_data['keyCode']) < keyCode_len:
        keyPressed_avg = average(read_data['keyPressed'])
        keyReleased_avg = average(read_data['keyReleased'])
        while len(read_data['keyCode']) < keyCode_len:
            read_data['keyCode'].append(32)
            read_data['keyPressed'].append(read_data['keyPressed'][-1]+keyPressed_avg)
            read_data['keyReleased'].append(read_data['keyReleased'][-1]+keyReleased_avg)
    for i in range(1, 6):
        read_data[str(i)+"gram"] = cal_ngram(i, read_data["keyPressed"], read_data["keyReleased"])
    read_data["duration"] = cal_duration(read_data["keyPressed"], read_data["keyReleased"])
    return read_data

def average(lst): 
    return sum(lst) / len(lst)

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

def check_length(read_data):
    if len(read_data['keyCode']) == len(read_data['keyPressed']) == len(read_data['keyReleased']):
        print(read_data['name'], len(read_data['keyCode']))
    else:
        print(read_data['name'], ": Error length")

def write2json(write_data, path):
    with open(path, "w") as files:
        json.dump(write_data, files)
        print(path + " -> write success")

# read keyCode generate
with open("key_code_generate.json") as data:
    keyCode_gen = json.load(data)
# print(keyCode_gen)

types = "templete"
article = "th_breakfast"

read_path = "raw_data\\th_breakfast\\"+types+"\\*.json"
files = glob.glob(read_path)

write_path = "new_data\\"+article+"\\"+types+"\\"

keyCode_len = len(keyCode_gen[article])
# print(keyCode_len)

for file_name in files:
    with open(file_name) as files:
        read_data = json.load(files)

    name = file_name[file_name.rfind("\\")+1:]
    write_data = modified(read_data, keyCode_len)
    modified(read_data, keyCode_len)

    write2json(write_data, write_path + name)
    print(write_path + name)

# modified(read_data, keyCode_len)