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
                "content": "����һ��ְҵ���Ĺ滮ʦ����Ŀͻ���һλ���б�ҵ���������Լ�����Ȥ�ͼ���û����������ʶ��Ҳ��֪���Լ��ʺ�ѡ��ʲôרҵ������Ϊ���ҵ��ʺ��Լ���רҵ�������û�и�����ȷ�Ļ����²��Խ����RIASEC��������ĸ��Ϊ�������������ĸ�ĵ÷���Ϊ�����������ʾ����"
            },
            {
                "role": "user",
                "content": f"�ҵĻ����²��Խ����{code}"
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
                "content": "����һ��ְҵ���Ĺ滮ʦ����Ŀͻ���һλ���б�ҵ��������Ϊ�����������˽��רҵ�������û�и�����ȷ��רҵ���ƣ�����ʾ����"
            },
            {
                "role": "user",
                "content": f"����һ��{name}"
            }
        ],
        temperature=0.7,
        top_p=1
    )
    return response.choices[0].message.content
