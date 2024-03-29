"""
--Algorithm
1. อ่านค่า keyCode ที่ generate จากไฟล์ key_code_generate.json เก็บไว้ในตัวแปร dict
2. ไล่อ่านไฟล์(ไฟล์ข้อมูล) templete และ query ที่เก็บไว้ทีละไฟล์
3. เปรียบเทียบ keyCode ในไฟล์ข้อมูล และ keyCode ที่ generate ไว้ทีละตำแหน่ง
4. ตัดตำแหน่งที่ keyCode ในไฟล์ข้อมูล ไม่ตรงกับ keyCode ในไฟล์ generate ออก รวมถึงตัดค่า keyPressed และ keyReleased ในตำแหน่งเดียวกันด้วย
5. คำนวณค่า n-gram และ duration ใหม่
6. output ออกมาเป็นไฟล์ข้อมูล(Datasets)ชุดใหม่ แบ่งเป็น templete และ query เหมือนเดิม
"""

import glob
import json

def checking(read_data):
    check_length(read_data)
    backspace = 8
    index = 0
    while read_data['keyCode'].count(backspace) > 0:
        index = read_data['keyCode'].index(backspace)
        read_data['keyCode'].pop(index-1)
        read_data['keyCode'].pop(index-1)
        read_data['keyPressed'].pop(index-1)
        read_data['keyPressed'].pop(index-1)
        read_data['keyReleased'].pop(index-1)
        read_data['keyReleased'].pop(index-1)
    for i in range(1, 6):
        read_data[str(i)+"gram"] = cal_ngram(i, read_data["keyPressed"], read_data["keyReleased"])
    read_data["duration"] = cal_duration(read_data["keyPressed"], read_data["keyReleased"])
    check_length(read_data)
    return read_data

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

def printData(data):
    string = ""
    for i in range(len(data)):
        # if data['keyCode'][i] == 8:
        #     print(i)
        # print(chr(data[i]), end="")
        string += chr(data[i])
    print(string)

# read keyCode generate
# with open("key_code_generate.json") as data:
#     keyCode_gen = json.load(data)
# print(keyCode_gen)

# read file data
# with open("7_WILAWAN_EN.json") as data:
#     read_data = json.load(data)
# print(read_data)

# data_name = "en_puma"

types = "templete"
article = "th_breakfast"

read_path = "raw_data\\"+article+"\\"+types+"\\*.json"
files = glob.glob(read_path)

write_path = "new_data\\"+article+"\\"+types+"\\"

for file_name in files:
    with open(file_name) as files:
        read_data = json.load(files)

    name = file_name[file_name.rfind("\\")+1:]
    write_data = checking(read_data)
    # checking(read_data)

    write2json(write_data, write_path + name)
    # print(write_path + name)