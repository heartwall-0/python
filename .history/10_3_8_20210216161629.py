'''
Author: 零到正无穷
Date: 2021-02-16 16:15:22
LastEditTime: 2021-02-16 16:16:29
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_3_8.py
'''
'''静默失败'''
def count_words(filenames):
    '''计算文件中单词的数量'''
    try:
        with open(filenames, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        pass
        # print(f"Sorry, the file {filenames} does not exsit.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filenames} has about {num_words} words.\n")