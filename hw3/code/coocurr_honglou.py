# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 21:57:35 2021

@author: Zhou Zixuan
对红楼梦统计人物共现情况
"""
import jieba
import jieba.posseg as pseg

# 输入文件
txt_file_name = './data/红楼梦.txt'
# 输出文件
node_file_name = './output/红楼梦-人物节点.csv'
link_file_name = './output/红楼梦-人物连接.csv'

# 由于文本较长、分析过程长，预先测试要写入的文本是否能打开，避免出现问题。
test =  open(node_file_name, 'w')
test.close()
test = open(link_file_name, 'w')
test.close()

# 打开文件，读入文字
txt_file = open(txt_file_name, 'r', encoding='utf-8')
line_list = txt_file.readlines()
txt_file.close()
# print(line_list) 测试

# 加载用户字典
jieba.load_userdict('./data/userdict.txt')

#1、生成基础数据(一个列表+一个字典)
line_name_list = [] # 统计每个段落出现的人物列表
name_cnt_dict = {} # 统计人物出现次数

# 设置忽略词列表
ignore_list=["明白","言语","冷笑","小丫头"]

# 显示处理进度
print('-'*10+'正在分段统计'+'-'*10)
print('已处理词数：')
progress = 0 # 用于计算进度条
for line in line_list: # 逐个段落循环处理
    word_gen = pseg.cut(line) # pseg.cut返回分词结果，“生成器”类型
    line_name_list.append([]) # 以段落为分割
    
    for one in word_gen:
        word = one.word
        flag = one.flag
        
        if len(word) == 1:
            continue
        
        if word in ignore_list:
            continue
        
        # 对指代同一人物的名词进行合并
        if word =="怡红公子" or word =="宝玉" or word == "宝二爷" or word == "宝兄弟":
            word = "贾宝玉"
        elif word == "黛玉" or word == '林妹妹' or  word == "林姑娘" or word == "林姐姐":
            word = '林黛玉'
        elif word == "宝钗" or word =="宝姑娘" or word == "宝钗笑" or word == "宝姐姐" or word == "宝丫头" or word == "宝钗见" or word == "宝钗忙" or word == "宝钗因" or word == "向宝钗":
            word = '薛宝钗'
        elif word == "老太太"or word =="老祖宗" or word == "贾母笑" or word == "史太君" or word == "贾母因" or word == "贾母王":
            word = "贾母"
        elif word =="凤丫头" or word =="凤姐" or word =="凤哥儿"or word =="凤辣子" or word == "凤姐儿" or word=="凤姐姐":
            word = "王熙凤"
        elif word == "蓉大奶奶" or word == "可卿" or word =="贾蓉之妻" or word == "秦氏":
            word = "秦可卿"
        elif word == "湘云" or word == "史姑娘" or word == "史大姑娘":
            word = "史湘云"
        elif word =="四姑娘" or word =="惜春":
            word = "贾惜春"
        elif word =="探春" or word =="三姑娘":
            word = "贾探春"        
        elif word =="迎春" or word == "二姑娘":
            word = "贾迎春"        
        elif word =="元春" or word == "元妃" or word == "贾妃":
            word = "贾元春"
        elif word =="巧姐儿":
            word = "贾巧姐"
        elif word =="贾政道" or word == "贾政听" or word == "贾政又" or word == "贾政笑":
            word = "贾政" 
        elif word == "琏二爷":
            word = "贾琏"
            
            
        if flag == 'nr':
            line_name_list[-1].append(word)
            if word in name_cnt_dict.keys():
                name_cnt_dict[word] = name_cnt_dict[word] + 1
            else:
                name_cnt_dict[word] = 1
                
        # 分词时间较长，打印进度条增加交互体验
        progress = progress + 1
        progress_quo = int(progress/1000)
        progress_mod = progress % 1000
        if progress_mod == 0:
            print('\r'+'-'*progress_quo+'>'+str(progress_quo)+'×10^3 ',end='')

print()
print('基础数据处理完成')

#2、用字典统计人名“共现”数量
relation_dict = {}

name_cnt_limit = 100

for line_name in line_name_list:
    for name1 in line_name:
        # 判断人物是否在字典中
        if name1 in relation_dict.keys():
            pass
        elif name_cnt_dict[name1] >= name_cnt_limit:
            relation_dict[name1]={}
        else:
            continue
        
        # 统计name1与本段的所有人名(除name1自身)的共现数量
        for name2 in line_name:
            if name2 == name1 or name_cnt_dict[name2] < name_cnt_limit:
            # 不统计name1自身，不统计出现较少的人物
                continue
            
            if name2 in relation_dict[name1].keys():
                relation_dict[name1][name2] = relation_dict[name1][name2] + 1
            else:
                relation_dict[name1][name2] = 1
            
print('共现统计完成，仅统计出现次数达到' + str(name_cnt_limit) + '及以上的人物')

#3、输出统计结果
for k,v in relation_dict.items():  # 测试点
    print(k, ':', v)
    
# 字典转成列表，按出现次数排序
item_list = list(name_cnt_dict.items())
item_list.sort(key=lambda x:x[1],reverse=True)

## 导出节点文件
node_file = open(node_file_name, 'w') 
# 节点文件，格式：Name,Weight -> 人名,出现次数
node_file.write('Name,Weight\n')
node_cnt = 0  # 累计写入文件的节点数量
for name,cnt in item_list: 
    if cnt >= name_cnt_limit:  # 只输出出现较多的人物
        node_file.write(name + ',' + str(cnt) + '\n')
        node_cnt = node_cnt + 1
node_file.close()
print('人物数量：' + str(node_cnt))
print('已写入文件：' + node_file_name)

## 导出连接文件
# 共现数可以看做是连接的权重，只导出权重达到限制数的连接
link_cnt_limit = 100
print('只导出数量达到' + str(link_cnt_limit) + '及以上的连接')

link_file = open(link_file_name, 'w')
# 连接文件，格式：Source,Target,Weight -> 人名1,人名2,共现数量
link_file.write('Source,Target,Weight\n')
link_cnt = 0  # 累计写入文件的连接数量
for name1,link_dict in relation_dict.items():
    for name2,link in link_dict.items():
        if link >= link_cnt_limit:  # 只输出权重较大的连接
            link_file.write(name1 + ',' + name2 + ',' + str(link) + '\n')
            link_cnt = link_cnt + 1
link_file.close()
print('连接数量：' + str(link_cnt))
print('已写入文件：' + link_file_name)      




















