"""
基于Streamlit完成WEB网页上传服务
 pip install streamlit

 Streamlit: 当WEB页面元素发生变化，则代码重新执行一次
 重新运行可能会导致状态丢失，所以需要使用st.session_state来保存状态
 st.session_state是一个字典，可以用来保存状态信息，
 页面元素发生变化时st.session_state中的信息不会丢失，可以用来保存一些需要在页面元素发生变化时保持不变的信息，比如文件内容、文件名等
"""
import streamlit as st
from knowledge_base import KnowledgeBaseService

# 添加网页标题
st.title("知识库更新服务")

# file_uploader
uploader_file = st.file_uploader(
    label="请上传文件",
    type=["txt"],
    accept_multiple_files=False, # False表示只能上传一个文件，True表示可以上传多个文件
)

# 这个session_state就是一个字典，可以用来保存状态信息
if "service" not in st.session_state:
    # 创建一个KnowledgeBaseService实例，并保存到session_state中
    st.session_state["service"] = KnowledgeBaseService() 

if uploader_file is not None:
    # 提取文件信息
    file_name = uploader_file.name
    file_size = uploader_file.size / 1024  # 转换为KB
    file_type = uploader_file.type

    st.subheader(f"文件名：{file_name}")
    st.write(f"格式：{file_type} | 大小：{file_size:.2f} KB")

    # 获取文件内容
    file_content = uploader_file.getvalue().decode("utf-8")  # 将字节流转换为字符串

    result = st.session_state["service"].upload_by_str(file_content, file_name)
    st.write(result)
