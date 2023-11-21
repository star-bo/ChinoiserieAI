import os
import streamlit as st
import pandas as pd
from PIL import Image
import base64
import plotly.express as px

# 设置页面配置
st.set_page_config(
     page_title="文本描述生成",
     page_icon="👋",
     layout="wide",    # 'wide' or 'centered'
     initial_sidebar_state="expanded",
 )

# 设置页面布局
st.header('文本描述生成任务')
st.markdown(' **输入中华文化语境下的中文自然语言文本，描述您希望生成得到的图片场景内容和风格，为您返回符合该文本描述的风格场景图片。**')

# 添加边框和底色的内联CSS样式
style = """
    text-decoration: none;
    display: inline-block;
    padding: 10px 20px;
    margin: 10px;
    border: 2px solid #3498db;
    color: #3498db;
    border-radius: 5px;
    transition: background-color 0.3s, color 0.3s;
"""

# 用户输入中文文字字段
user_input = st.text_input("请输入中文字段:")
# 预设好的关键词和对应的图片路径
keyword_images = {
    "赵诘画的冬景山水图": "赵诘冬景山水图.jpg",
    "赵诘冬景山水图": "赵诘冬景山水图.jpg",
    "赵诘，冬景山水图": "赵诘冬景山水图.jpg",
    "我想了解马远所画的踏歌图": "马远踏歌图.jpg",
    "马远踏歌图": "马远踏歌图.jpg",
    "马远，踏歌图": "马远踏歌图.jpg",
    "郭熙，早春图": "郭熙早春图.jpg",
    "郭熙早春图": "郭熙早春图.jpg",
    "郭熙的早春图": "郭熙早春图.jpg",
    # 添加更多关键词和对应的图片路径
}

# 如果有输入
if user_input:
    # 用于记录是否匹配到关键词
    keyword_matched = False

    # 遍历关键词和图片路径的字典
    for keyword, image_path in keyword_images.items():
        # 如果关键词出现在用户输入中
        if keyword in user_input:
            # 显示对应的图片
            col1, col2 = st.columns([1, 1])
            with col1:
                image = Image.open(image_path)
                st.image(image, caption="相关图片", use_column_width=True)
                keyword_matched = True
            # 结束循环，只显示匹配到的第一个关键词对应的图片
            break

    # 如果没有匹配到关键词，显示提示信息
    if not keyword_matched:
        st.warning("抱歉，未匹配到相关图片，请尝试其他关键词。")

# 如果没有输入，显示提示信息
elif not user_input:
    st.warning("请输入中文文字字段")
