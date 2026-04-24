"""
为整个工程提供统一的绝对路径
"""
import os
def get_project_root_path():
    """
    获取项目根目录
    :return:字符串根目录
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_abs_path(relative_path):
    """
    获取绝对路径
    :param relative_path: 相对路径
    :return: 绝对路径
    """
    return os.path.join(get_project_root_path(), relative_path)

