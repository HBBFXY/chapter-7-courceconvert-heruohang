# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 以下内容自行完成
import keyword
import re

def convert_python_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 获取Python保留字集合
    reserved_words = set(keyword.kwlist)

    # 正则模式：优先匹配字符串、注释，再匹配标识符
    pattern = r'''
        (r?["']{1,3}.*?["']{1,3})  # 匹配字符串（单/双/三引号，支持r前缀）
        |
        (#.*$)                     # 匹配单行注释
        |
        (\b[a-zA-Z_][a-zA-Z0-9_]*\b)  # 匹配Python标识符（字母/下划线开头）
    '''

    def replace_match(match):
        # 字符串和注释直接保留原样
        if match.group(1) or match.group(2):
            return match.group()
        # 标识符判断是否为保留字
        elif match.group(3):
            word = match.group(3)
            return word if word in reserved_words else word.upper()
        # 其他内容（符号、数字等）直接保留
        return match.group()

    # 执行替换（忽略大小写+多行+verbose模式）
    processed_content = re.sub(
        pattern, replace_match, content,
        flags=re.IGNORECASE | re.MULTILINE | re.VERBOSE
    )

    # 写入输出文件
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(processed_content)

# 执行转换
convert_python_file('random_int.py', 'random_int_uppercase.py')