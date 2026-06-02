"""
知识库基础服务代码
"""

def check_md5(md5_str: str):
    """
    检查传入的md5字符串是否已经被处理过了
    """
    
    pass

def save_md5():
    """
    将传入的md5字符串，记录到文件内保存
    """
    pass

def get_string_md5():
    """
    获取字符串的md5值
    """
    pass

class KnowledgeBaseService(object):
    def __init__(self):
        self.chroma = None # 向量存储的实例 Chroma数据库
        self.splitter = None # 文本分割器对象

    def upload_by_str(self, data, filename):
        """
        将传入的字符串进行向量化
        并存入向量数据库中
        """
        pass