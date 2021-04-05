# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 

@author: dell
地理连线图
绘制出全国五大机场、2020寒暑期热门航线
"""
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType


c = (
    Geo()
    .add_schema(# 设置地图及背景
            maptype="china",
            itemstyle_opts=opts.ItemStyleOpts(color="grey", border_color="black"),)
    .add(# 特效画点-全国五大机场
        "",
        [("广州", "白云"), ("成都", "双流"), ("深圳", "宝安"), ("上海", "浦东"), ("北京", "首都")],
        type_=ChartType.EFFECT_SCATTER,
        color="white",
    )
    .add(# 画点-大机场
        "",
        [("昆明", "长水"), ("杭州", "萧山"), ("海口", "美兰"), ("重庆", "江北"), ("西双版纳", "嘎洒"),],
         #城市标记参数是由元组项组成的列表
        type_=ChartType.SCATTER,
        color="white",
    )
    .add(# 连线
        "2021春节TOP5航线",
        [("重庆", "深圳"), ("成都", "深圳"), ("广州", "重庆"),
         ("广州", "成都"), ("广州", "海口")],
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="white"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.4),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(# 连线
        "2020暑期热门航线",
        [("深圳", "上海"), ("广州", "上海"), ("广州", "成都"),
         ("深圳", "成都"), ("成都","深圳"), ("重庆","深圳"), ("深圳", "重庆"), ("成都","广州"),("杭州", "广州"), ("昆明", "西双版纳")],
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        # 设置不同参数避免重合
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="2020寒暑期热门航线"))
    
    .render('./output/2020寒暑期热门航线.html')
)

