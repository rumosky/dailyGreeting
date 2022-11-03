import requests
import json
from datetime import datetime
import random

def httpGet(url, params):
    r = requests.get(url, params)
    return json.loads(r.content)

def httpPost(url, params):
    r = requests.post(url, params)
    return json.loads(r.content)

# 获取微信token
def getAccessToken(appId, appSecret):
    params = {
        'grant_type': 'client_credential',
        'appid': appId,
        'secret': appSecret
    }
    url = 'https://api.weixin.qq.com/cgi-bin/token'
    return httpGet(url, params)

# 获取每日励志英语（英文）
def getDailyEnglish():
    url = 'https://api.vvhan.com/api/en'
    talk = httpGet(url, {'type': 'json'})
    return talk['data']['en']

# 获取每日励志英语（中文）
def getDailyChinese():
    url = 'https://api.vvhan.com/api/en'
    talk = httpGet(url, {'type': 'json'})
    return talk['data']['zh']

# 获取在一起天数
def getTogetherDays(togetherDay):
    togetherDay = datetime.strptime(togetherDay, '%Y-%m-%d')
    interval = datetime.now() - togetherDay
    return interval.days

# 发送模版消息
def sendTemplateMessage(content, accessToken):
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=' + accessToken
    return httpPost(url, content)

# 获取爱称
def getNickName():
    nameHub = ['安琪','安琪宝贝','Angel','安安','琪琪','琪琪子','亲爱的安琪','心爱的安琪']
    currentName = random.choice(nameHub)
    return currentName

if __name__ == '__main__':
    # 微信公众号的appId和appSecret
    appId = 'xxx'
    appSecret = 'xxx'
    # 要发送人的openId列表
    openIdList = ['xxx','xxx','xxx','xxx']
    # 模版Id
    templateId = 'xxx'
    # 在一起的时间
    togetherDay = '2022-11-01'

    accessTokenInfo = getAccessToken(appId, appSecret)
    accessToken = accessTokenInfo['access_token']
    sentenceZh = getDailyChinese()
    sentenceEn = getDailyEnglish()
    togetherDays = getTogetherDays(togetherDay)
    name = getNickName()

    for i in range(len(openIdList)):
        data = {
            'touser': openIdList[i],
            'template_id': templateId,
            'topcolor' : '#FF0000',
            'data': {
                'togetherDays': {
                    'value': togetherDays,
                    'color': '#ff4dff'
                },
                'sentenceEn': {
                    'value': sentenceEn,
                    'color': '#2e317c'
                },
                'sentenceZh': {
                    'value': sentenceZh,
                    'color': '#346c9c'
                },
                'name':{
                    'value': name,
                    'color': '#ee3f4d'
                }
            }
        }
        params = json.dumps(data)

        print(sendTemplateMessage(params, accessToken))
