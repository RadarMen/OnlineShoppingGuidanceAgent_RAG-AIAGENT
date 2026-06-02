"""
基于Streamlit完成WEB网页上传服务
 pip install streamlit
"""
import streamlit as st

# 添加网页标题
st.title("知识库更新服务")

# file_uploader
uploader_file = st.file_uploader(
    label="请上传文件",
    type=["txt"],
    accept_multiple_files=False, # False表示只能上传一个文件，True表示可以上传多个文件
)

if uploader_file is not None:
    # 提取文件信息
    file_name = uploader_file.name
    file_size = uploader_file.size / 1024  # 转换为KB
    file_type = uploader_file.type

    st.subheader(f"文件名：{file_name}")
    st.write(f"格式：{file_type} | 大小：{file_size:.2f} KB")

    # 获取文件内容
    file_content = uploader_file.getvalue().decode("utf-8")  # 将字节流转换为字符串
    st.write(file_content)

    