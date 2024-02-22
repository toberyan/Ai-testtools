
import os
from openai import OpenAI

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
            {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一些涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content



# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

    # 示例对话
    user_input = "你好，聊天机器人！"
    while True:
        if user_input.lower() == '退出':
            break

        # 向OpenAI发送用户输入，获取回复
        response = chat_with_openai(user_input)
        print(f"机器人: {response}")

        # 用户输入下一轮对话
        user_input = input("用户: ")

    print("聊天结束！")

