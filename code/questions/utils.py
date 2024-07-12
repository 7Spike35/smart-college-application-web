# coding=gbk
from openai import OpenAI
import os


def answer_1(code):
    os.environ["http_proxy"] = "http://localhost:7890"
    os.environ["https_proxy"] = "http://localhost:7890"
    client = OpenAI(api_key='xxx')
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "你是一个职业生涯规划师，你的客户是一位高中毕业生，他对自己的兴趣和技能没有清晰的认识，也不知道自己适合选择什么专业。请你为他找到适合自己的专业。如果他没有给你正确的霍兰德测试结果（RIASEC中三个字母作为结果或是六个字母的得分作为结果），请提示他。"
            },
            {
                "role": "user",
                "content": f"我的霍兰德测试结果是{code}"
            }
        ],
        temperature=0.7,
        top_p=1
    )
    return response.choices[0].message.content


def answer_2(name):
    os.environ["http_proxy"] = "http://localhost:7890"
    os.environ["https_proxy"] = "http://localhost:7890"
    client = OpenAI(api_key='xxx')
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "你是一个职业生涯规划师，你的客户是一位高中毕业生，请你为他介绍他想了解的专业。如果他没有给你正确的专业名称，请提示他。"
            },
            {
                "role": "user",
                "content": f"介绍一下{name}"
            }
        ],
        temperature=0.7,
        top_p=1
    )
    return response.choices[0].message.content
