"""
--Algorithm
1. อ่านค่าบทความ(ทั้ง 3 บทความ) จากไฟล์ .txt เก็บไว้ในตัวแปร str
2. แปลงค่าแต่ละตัวอักษรเป็น ascii code แล้วเก็บไว้ในตัวแปร list(ทำทั้ง 3 บทความ)
3. เก็บ list ทั้ง 3 ชุด ลงในตัวแปร dict ที่มี key เป็นชื่อของบทความ
4. เขียนข้อมูลจากตัวแปร dict ลงไฟล์ .json
"""

import glob
import json

def loadArticle(path, article_name, extension):
    articles = []
    for name in article_name:
        with open(path+name+extension, encoding="utf8") as data:
            articles.append(data.read())
    return articles

if __name__ == '__main__':
    path = "articles/"
    article_name = ["en_puma", "th_breakfast", "th_font_test"]
    extension = ".txt"

    articles = loadArticle(path, article_name, extension)
    keyCode = {}

    i=0
    for article in articles:
        temp_list = []
        for char in article:
            temp_list.append(ord(char))
        keyCode.update({article_name[i]:temp_list})
        i += 1
        # temp_list.clear()  # เอาไว้ตรงนี้ไม่ได้ ไม่รู้ทำไม

    # en_puma test
    # en_puma_keyCode = list(range(65, 90+1)) + list(range(97, 122+1)) + [32, 39, 44, 45, 46]
    en_shift = list(range(65, 90+1))
    # print(en_puma_keyCode, len(en_puma_keyCode))
    temp_list = []
    # print(len(keyCode['en_puma']))
    for code in keyCode['en_puma']:
        if code in en_shift:
            # print(code, chr(code))
            temp_list.append(16)
            temp_list.append(code)
        else:
            temp_list.append(code)
    keyCode['en_puma'] = temp_list
    # print(keyCode['en_puma'])
    # print(len(keyCode['en_puma']))

    # th_font_test test
    th_font_test_keyCode = list(range(3585, 3660+1)) + [10, 32]
    th_shift = [3589, 3590, 3593, 3595, 3596, 3597, 3598, 3599, 3600, 3601, 3602, 3603, 3608, 3620, 3622, 3624, 3625, 
    3628, 3630, 3641, 3650, 3655, 3658, 3659, 3660]
    # print(th_font_test_keyCode, len(th_font_test_keyCode))
    temp_list = []
    # print(len(keyCode['th_font_test']))
    for code in keyCode['th_font_test']:
        if code in th_shift:
            # print(code, chr(code))
            temp_list.append(16)
            temp_list.append(code)
        else:
            temp_list.append(code)
    keyCode['th_font_test'] = temp_list
    # print(keyCode['th_font_test'])
    # print(len(keyCode['th_font_test']))

    # th_breakfast
    temp_list = []
    print(len(keyCode['th_breakfast']))
    for code in keyCode['th_breakfast']:
        if code in th_shift:
            print(code, chr(code))
            temp_list.append(16)
            temp_list.append(code)
        else:
            temp_list.append(code)
    keyCode['th_breakfast'] = temp_list
    # print(keyCode['th_breakfast'])
    print(len(keyCode['th_breakfast']))