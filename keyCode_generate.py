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

    # print(keyCode)
    # for i in range(65, 84):
    #     print(chr(i))
    # print(ord(' '), ord('z'), ord('ก'), ord('ฮ'))
    for code in keyCode['en_puma']:
        print(code, chr(code))
    print(len(keyCode['en_puma']))