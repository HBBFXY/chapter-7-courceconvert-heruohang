# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 以下内容自行完成
import keyword
import re

def convert_non_keywords_to_upper(input_file, output_file):
    # 读取原文件内容
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 正则匹配标识符（Python标识符规则：字母/下划线开头，后跟字母/数字/下划线）
    pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'

    def replace_word(match):
        word = match.group()
        # 是保留字则不转换，否则转大写
        return word if keyword.iskeyword(word) else word.upper()

    # 替换非保留字的标识符
    processed_content = re.sub(pattern, replace_word, content)

    # 保存结果
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(processed_content)

# 调用函数（输入文件、输出文件）
convert_non_keywords_to_upper("random_int.py", "random_int_upper_v2.py")