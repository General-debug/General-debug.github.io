# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 08:51:29 2021

@author: dell

从纯文本文件中将数据生成理想的格式
"""


##-------从文件中读出城市房价------------------
src_filename = './data/userdict.txt'

src_file = open(src_filename, 'r',encoding = 'utf-8')
line_list = src_file.readlines()  #返回列表，文件中的一行是一个元素
src_file.close()

print(line_list)  # 检查读入数据的情况

# 将读入的每行数据拆分成元组
wordfreq_list = []  #用于保存元组(城市,房价)
cnt= 0
for line in line_list:
    line = line.strip()  #删除'\n'
    line_split = line.split(',') # 以空格作为标志，把字符串切分成词，存在列表中
    wordfreq_list.append((line_split[0], line_split[1]))
    cnt = cnt + 1

for items in wordfreq_list:
    #print('["{}", {}],\r'.format(items[0],items[1]))
    print('{} {}\r'.format(items[0],items[1]))


