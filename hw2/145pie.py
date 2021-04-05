# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 

@author: dell
十四五规划词频统计-饼图
"""
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

words = [
("发展",440),
("体系",238),
("制度",167),
("国家",160),
("机制",156),
("创新",136),
("服务",133),
("安全",122),
("政策",110),
("经济",108),
("能力",104),
("产业",100),
("社会",97),
("改革",93),
("重点",85),
("战略",84),
("规划",81),
("文化",79),
("生态",79),
("企业",77),
("合作",75),
("国际",74),
("管理",74),
("科技",72),
("资源",71),
("水平",69),
("城市",67),
("农业",62),
("区域",62),
("教育",62),
("市场",62),
("地区",62),
("公共服务",60),
("基础设施",55),
("技术",55),
]

c = (
    Pie()
    .add(
        "",
        words,
        center=["40%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="十四五规划词频饼图", title_textstyle_opts=opts.TextStyleOpts(font_size=30)),
        legend_opts=opts.LegendOpts(pos_left="80%", orient="vertical"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("./output/十四五规划词频统计_pie.html")
)
