'''
Author: 零到正无穷
Date: 2021-02-16 16:15:22
LastEditTime: 2021-02-16 16:26:51
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_3_8.py
'''
'''静默失败'''
file_name = 'write.txt'
def count_words(filenames):
    '''计算文件中单词的数量'''
    try:
        with open(filenames, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        with open(file_name, 'w') as file:
            file.write(f"{filenames}")
        pass
        # print(f"Sorry, the file {filenames} does not exsit.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filenames} has about {num_words} words.\n")

filenames = ['alice.txt', 'siddhartha.txt', 'little_women.txt', 'moby_dick.txt']
for filename in filenames:
    count_words(filename)