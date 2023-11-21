import os
import streamlit as st
from PIL import Image
import base64

# 设置页面配置
st.set_page_config(
     page_title="中华文化语境下的AI绘图",
     page_icon="👋",
     layout="wide",    # 'wide' or 'centered'
     initial_sidebar_state="expanded",
 )
# 页面标题
st.title('中华文化语境下的AI绘图（Demo演示版）')

# Display in two columns
col1, col2 = st.columns([1, 1])
with col1:
# 加载图像
    image = Image.open("0.jpg")
    st.image(image, use_column_width=True,width =20)
with col2:
    # 页面头部信息
    st.subheader("欢迎来到中华文化语境下的AI画图演示版，现已开放如下体验功能：")
    # st.balloons()
    st.markdown(
        """    
        - **文本 → 图片**: 输入中华文化语境下的中文自然语言文本，描述您希望生成得到的图片场景内容和风格，系统为您返回符合该文本描述的风格场景图片。
        - **图片 → 图片**: 选择上传您待修复的中华文化语境相关的图片（小于100MB，格式要求为.jpg 或.jpeg 或.png），系统为您返回该图片的修复结果图。
        """
    )
st.markdown(
        """    
        其它功能，如文本→三维场景，图片→三维场景，三维场景→三维场景正在开发中……敬请期待！如有疑问，请联系 ***jabo_Dai@163.com*** 
        """
    )

# 添加分隔线
# st.markdown("---")

# 添加空白空间
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 将附加说明内容居中显示在底部
st.markdown(
    f"""
    <div class="bg-image" style="text-align:center;">
        <p>© 2023 by Jabo </strong></p>
    </div>
    """,
    unsafe_allow_html=True
)
