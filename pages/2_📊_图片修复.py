import os
import streamlit as st
from PIL import Image

# 设置页面配置
st.set_page_config(
    page_title="图片修复",
    page_icon="👋",
    layout="wide",    # 'wide' or 'centered'
    initial_sidebar_state="expanded",
)

# 设置页面布局
st.header('图片修复任务')
st.markdown(' **选择上传您待修复的中华文化语境相关的图片（小于100MB，格式为.jpg/.jpeg/.png），为您返回该图片的修复结果图。**')

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

# 上传图片
uploaded_file = st.file_uploader("请上传图片", type=["jpg", "jpeg", "png"])

# 预定义的图片路径字典
image_paths = {
    "山东武梁祠拓本": {"before": "山东武梁祠拓本.png", "after": "Demo1-1.png", "title": "山东武梁祠拓本(部分)"},
    "河北磁县湾漳村北齐高洋墓壁画": {"before": "河北磁县湾漳村北齐高洋墓壁画.jpg", "after": "Demo2-2.jpg", "title": "河北磁县湾漳村北齐高洋墓壁画(畏兽)"},
    "克孜尔77号洞窟伎乐天": {"before": "克孜尔77号洞窟伎乐天.png", "after": "Demo3-3.png", "title": "克孜尔77号洞窟伎乐天(局部)"},
    # 添加更多图片路径
}

# 如果有上传图片
if uploaded_file:
    # 获取上传文件的文件名
    uploaded_filename = uploaded_file.name.split(".")[0]

    # 如果上传的图片在预定义的图片路径字典中
    if uploaded_filename in image_paths:
        st.success("图片已上传！")
        # 使用 st.beta_columns 进行外部分栏对齐
        col1, col2 =  st.columns([4, 3])
        with col1:
            # 显示原始上传图片
            st.markdown(
                f"<p style='color: #f9f9f9; font-size: 18px;'><strong>{image_paths[uploaded_filename]['title']} - 原始上传图片<strong></p>",
                unsafe_allow_html=True)
            original_image = Image.open(image_paths[uploaded_filename]["before"])
            st.image(original_image, caption="原始上传图片", use_column_width=True)
        with col2:
            # 添加按钮
            if st.button("查看修复结果"):
                # 显示AI修复结果
                st.markdown(
                    f"<p style='color: #f9f9f9; font-size: 18px;'><strong>{image_paths[uploaded_filename]['title']} - AI修复结果<strong></p>",
                    unsafe_allow_html=True)
                repaired_image = Image.open(image_paths[uploaded_filename]["after"])
                st.image(repaired_image, caption="AI修复结果", use_column_width=True)

    else:
        st.warning("抱歉，暂无法处理该图片，请尝试上传其他图片。")

# 如果没有上传图片，显示提示信息
elif not uploaded_file:
    st.warning("请上传图片")
