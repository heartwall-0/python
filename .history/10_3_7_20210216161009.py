'''
Author: 零到正无穷
Date: 2021-02-16 16:07:31
LastEditTime: 2021-02-16 16:10:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_3_7.py
'''
'''使用多个文件'''

def count_words(filenames):
    '''计算文件中单词的数量'''
    try:
        with open(filenames, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        print(f"Sorry, the file {filenames} does not exsit.")

    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filenames} has about {num_words} words.")
