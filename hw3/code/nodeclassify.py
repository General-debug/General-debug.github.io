# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 11:35:10 2021

@author: Alex

要点说明：
用第三方库pyecharts绘制关系图（Graph）,带分类节点
使用前面程序生成的红楼梦人物关系数据
数据有手工调整，增加了分类信息
"""

from pyecharts import options as opts
from pyecharts.charts import Graph
import math
##--- 第0步：准备工作
# 输入文件
node_file_name = './data/红楼梦-人物节点-分类.csv' # 手工增加家族分类
link_file_name = './data/红楼梦-人物连接.csv'
# 输出文件
out_file_name = './output/关系图-分类-红楼梦.html'

##--- 第1步：从文件读入节点和连接信息
node_file = open(node_file_name, 'r')
node_line_list = node_file.readlines()
node_file.close()
del node_line_list[0]  # 删除标题行

link_file = open(link_file_name, 'r')
link_line_list = link_file.readlines()
link_file.close()
del link_line_list[0]  # 删除标题行

##--- 第2步：解析读入的信息，存入列表
# 类别列表，用于给节点分成不同系列，会自动用不同颜色表示
categories=[{}, {'name':'贾府'}, {'name':'贾府'}, {'name':'王家'}, {'name':'薛家'}, {'name':'史家'}, {'name':'其他'}]

node_in_graph = []
for one_line in node_line_list:
    one_line = one_line.strip('\n')
    one_line_list = one_line.split(',')
    #print(one_line_list)  # 测试点
    node_in_graph.append(opts.GraphNode(
            name=one_line_list[0], 
            value=int(one_line_list[1]), 
            symbol_size=math.sqrt(int(one_line_list[1])),  # 手动调整节点的尺寸
            category=int(one_line_list[2])))  # 类别
#print('-'*20)  # 测试点
link_in_graph = []
for one_line in link_line_list:
    one_line = one_line.strip('\n')
    one_line_list = one_line.split(',')
    #print(one_line_list)  # 测试点
    link_in_graph.append(opts.GraphLink(
            source=one_line_list[0], 
            target=one_line_list[1], 
            value=int(one_line_list[2])))


##--- 第3步：画图
c = Graph()
c.add("", 
      node_in_graph, 
      link_in_graph, 
      edge_length=[1,100], 
      repulsion=5000,
      categories=categories, 
      linestyle_opts=opts.LineStyleOpts(curve=0.2),  # 增加连线弧度
      layout="force",  # "force"-力引导布局，"circular"-环形布局
      )
c.set_global_opts(title_opts=opts.TitleOpts(title="关系图-红楼梦-家族分类"))
c.render(out_file_name)