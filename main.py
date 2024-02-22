import os
import time

from openai import OpenAI

global_input_data = []
global_output_data = []


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


def chat_with_openai(prompt):
    # 调用OpenAI的聊天接口
    client = OpenAI(
        api_key="sk-CBlpqpCBtWS2HA0i9LdD7jfQu6Sm82sqyy64VLzjGPqGAYS4",
        base_url="https://api.moonshot.cn/v1",
    )

    response = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=[
            {"role": "system",
             "content": "你是 Kimi，由 Moonshot AI "
                        "提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一些涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI "
                        "为专有名词，不可翻译成其他语言。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content


def traverse_folder(folder_path):
    # 获取文件夹中所有文件和子文件夹的列表
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        # 构建完整的文件路径
        full_path = os.path.join(folder_path, file_name)

        # 判断是文件还是文件夹
        if os.path.isfile(full_path):
            # 如果是文件，可以进行相应的操作
            print("文件:", full_path)

            with open(full_path, 'r') as file:
                # 读取每一行内容
                lines = file.readlines()

                # 遍历每一行并进行操作
                for line in lines:
                    global_input_data.append(line)
                    print(line.strip())  # 使用strip()方法去除每行末尾的换行符

        elif os.path.isdir(full_path):
            # 如果是文件夹，递归调用函数
            print("文件夹:", full_path)
            traverse_folder(full_path)


# 调用模型对话结果函数
def get_model_result(input_data):
    response = chat_with_openai(input_data)
    global_output_data.append(response)


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # 指定要遍历的文件夹路径
    folder_path = "./examples"

    # 调用函数开始遍历
    traverse_folder(folder_path)

    timer = 0  # 计算一分钟内询问的次数

    # 调用模型将训练数据问题输入，反馈输出结果
    for single_data in global_input_data:
        get_model_result(single_data)
        print(global_output_data[-1])
        time.sleep(1)
        timer += 1

        if timer == 4:
            timer = 0
            time.sleep(60)
