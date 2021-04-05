# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 18:14:06 2021

@author: dell
绘制选项卡多图
来自pyecharts官方文档示例
"""

from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Pie, Tab, Timeline, Page
from pyecharts.faker import Faker

# 2017年各省份碳排放柱状图-bar
def bar_datazoom_both() -> Bar:
    c = (
        Bar()
        .add_xaxis(
            ["山东",
            "江苏",
            "河北",
            "内蒙古",
            "广东",
            "河南",
            "山西",
            "辽宁",
            "新疆",
            "浙江",
            "安徽",
            "湖北",
            "湖南",
            "四川",
            "黑龙江",
            "陕西",
            "贵州",
            "福建",
            "江西",
            "广西",
            "吉林",
            "云南",
            "上海",
            "宁夏",
            "重庆",
            "甘肃",
            "天津",
            "北京",
            "青海",
            "海南",
        ])
        .add_yaxis('碳排放总量', 
                   [
                    806,
                    736,
                    726,
                    639,
                    542,
                    494,
                    488,
                    479,
                    404,
                    382,
                    371,
                    325,
                    310,
                    309,
                    269,
                    262,
                    255,
                    230,
                    224,
                    221,
                    204,
                    195,
                    190,
                    175,
                    158,
                    151,
                    141,
                    85,
                    53,
                    42,]
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="中国各省2017年碳排放总量"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
    )
    return c

# 中国主要碳排放物排放量逐年变化图-line
def line_markline() -> Line:
    c = (
        Line()
        .add_xaxis(['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015'])
        .add_yaxis(
            "Row Coal",
            [1767.0,
            1868.2,
            2049.3,
            2433.9,
            2772.3,
            3151.1,
            3488.1,
            3752.1,
            3872.2,
            4163.5,
            4407.8,
            4917.7,
            5076.8,
            5271.8,
            4993.9,
            4872.0,
                ],
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        )
        .add_yaxis(
            "Diesel Oil",
            [205.9,
            220.7,
            240.2,
            264.5,
            314.9,
            339.1,
            373.2,
            385.7,
            418.2,
            418.6,
            454.0,
            483.0,
            523.4,
            529.7,
            530.0,
            534.7,
            ],
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        )
        .add_yaxis(
            "Coke",
            [295.8,
            325.6,
            350.1,
            435.2,
            493.9,
            687.3,
            763.4,
            852.7,
            875.6,
            992.2,
            1071.6,
            1169.1,
            1242.0,
            1265.4,
            1294.3,
            1217.1,
            ],
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        )
        .add_yaxis(
            "Gasoline",
            [102.1,
            104.8,
            110.8,
            122.3,
            137.0,
            141.8,
            158.3,
            161.2,
            179.5,
            180.3,
            203.2,
            222.1,
            238.8,
            273.8,
            285.8,
            332.4,
            ],
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="中国主要碳排放物逐年变化情况"))
    )
    return c

# 中国2000-2015年各年碳排放量及其组成-timeline,pie
def timeline_pie() -> Timeline:
    tl=Timeline()
    attr = ['Raw Coal', 'Cleaned Coal', 'Other Washed Coal', 'Briquettes', 'Coke', 'Coke Oven Gas', 'Other Gas', 'Other Coking Products', 'Crude Oil', 'Gasoline', 'Kerosene', 'Diesel Oil', 'Fuel Oil', 'LPG', 'Refinery Gas', 'Other Petroleum Products', 'Natural Gas', ' Process']
    for i in range(2000,2016):
        pie = (
            Pie()
            .add(
                "xx",
                [list(z) for z in zip(attr, Faker.values())],
                rosetype="radius",
                radius=["30%", "55%"],
            )
            .set_global_opts(title_opts=opts.TitleOpts("中国{}年碳排放量".format(i)),
                             legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),)
            )
        tl.add(pie, "{}年".format(i))
    return tl

tab=Tab()
tab.add(bar_datazoom_both(), "中国各省2017年碳排放总量-bar")
tab.add(timeline_pie(), "中国2000-2015年各年碳排放量及其组成-timeline")
tab.add(line_markline(), "中国主要碳排放物排放量逐年变化图-line")
tab.render("./output/碳排放量_tab.html")