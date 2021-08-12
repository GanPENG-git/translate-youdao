import requests
from bs4 import BeautifulSoup
import re

# 访问内容
def getResponse(inputword):
    # 有道地址
    baseurl = 'https://www.youdao.com/w/%s/' % inputword
    response = requests.get(baseurl)
    return response

# 获取内容
def getContent(response):
    soup = BeautifulSoup(response,'html.parser')
    needcontent = soup.find("div",class_="trans-container")
    content = re.findall(filt,str(needcontent))
    return content

# 输出翻译结果
def outputResult(content):
    for each in content:
        print(each)
    return

def main(inputword):
    response = getResponse(inputword)
    response = response.text
    content = getContent(response)
    outputResult(content)
    return

# 提示
print('——————英文<->中文——————\n输入“end”结束程序')
inputword = str(input('请输入单词:'))
while inputword != "end":
    if re.match('[a-zA-Z]',inputword) != None:
        filt = re.compile(r'<li>(.*?)</li>')
    else:
        filt = re.compile(r'translation">(.*?)</a>')
    main(inputword)
    inputword = str(input('\n请输入单词:'))
else:
    print("程序结束！")