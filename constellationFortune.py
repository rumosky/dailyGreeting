import requests
import json
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

# 获取运势信息
def getFortuneData():
    url = 'https://api.vvhan.com/api/horoscope'
    data = httpGet(url, {'type': 'sagittarius','time':'today'})
    return data

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
    openIdList = ['xxx','xxx']
    # 模版Id
    templateId = 'xxx'

    accessTokenInfo = getAccessToken(appId, appSecret)
    accessToken = accessTokenInfo['access_token']
    name = getNickName()
    fortuneData = getFortuneData()
    fortuneTitle = fortuneData['data']['title']
    luckyColor = fortuneData['data']['luckycolor']
    luckyNumber = fortuneData['data']['luckynumber']
    luckyConstellation = fortuneData['data']['luckyconstellation']
    shortComment = fortuneData['data']['shortcomment']
    fortuneText = fortuneData['data']['fortunetext']['all']
    fortuneLove = fortuneData['data']['fortunetext']['love']
    fortuneWork = fortuneData['data']['fortunetext']['work']
    fortuneMoney = fortuneData['data']['fortunetext']['money']
    fortuneHealth = fortuneData['data']['fortunetext']['health']


    for i in range(len(openIdList)):
        data = {
            'touser': openIdList[i],
            'template_id': templateId,
            'topcolor' : '#FF0000',
            'data': {
                'name':{
                    'value': name,
                    'color': '#ee3f4d'
                },
                'fortuneTitle':{
                    'value': fortuneTitle,
                    'color': '#282c34'
                },
                'luckyColor':{
                    'value': luckyColor,
                    'color': '#065279'
                },
                'luckyNumber':{
                    'value': luckyNumber,
                    'color': '#4b5cc4'
                },
                'luckyConstellation':{
                    'value': luckyConstellation,
                    'color': '#e06c75'
                },
                'shortComment':{
                    'value': shortComment,
                    'color':'#4c8dae'
                },
                'fortuneText':{
                    'value': fortuneText,
                    'color': '#db5a6b'
                },
                'fortuneLove':{
                    'value': fortuneLove,
                    'color': '#801dae'
                },
                'fortuneWork':{
                    'value': fortuneWork,
                    'color': '#21a675'
                },
                'fortuneMoney':{
                    'value': fortuneMoney,
                    'color': '#f2be45'
                },
                'fortuneHealth':{
                    'value': fortuneHealth,
                    'color': '#b36d61'
                }
            }
        }
        params = json.dumps(data)

        print(sendTemplateMessage(params, accessToken))
