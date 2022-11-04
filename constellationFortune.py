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

# 获取运势标题
def getFortuneTitle():
    url = 'https://api.vvhan.com/api/horoscope'
    talk = httpGet(url, {'type': 'aries','time':'today'})
    return talk['data']['title']

# 获取幸运颜色
def getLuckyColor():
    url = 'https://api.vvhan.com/api/horoscope'
    talk = httpGet(url, {'type': 'aries','time':'today'})
    return talk['data']['luckycolor']

# 获取幸运数字
def getLuckyNumber():
    url = 'https://api.vvhan.com/api/horoscope'
    talk = httpGet(url, {'type': 'aries','time':'today'})
    return talk['data']['luckynumber']

# 获取速配星座
def getLuckyConstellation():
    url = 'https://api.vvhan.com/api/horoscope'
    talk = httpGet(url, {'type': 'aries','time':'today'})
    return talk['data']['luckyconstellation']

# 获取短评
def getShortComment():
    url = 'https://api.vvhan.com/api/horoscope'
    talk = httpGet(url, {'type': 'aries','time':'today'})
    return talk['data']['shortcomment']

# 获取综合运势
def getFortuneText():
    url = 'https://api.vvhan.com/api/horoscope'
    talk = httpGet(url, {'type': 'aries','time':'today'})
    return talk['data']['fortunetext']['all']

# 获取爱情运势
def getFortuneLove():
    url = 'https://api.vvhan.com/api/horoscope'
    talk = httpGet(url, {'type': 'aries','time':'today'})
    return talk['data']['fortunetext']['love']

# 获取学业运势
def getFortuneWork():
    url = 'https://api.vvhan.com/api/horoscope'
    talk = httpGet(url, {'type': 'aries','time':'today'})
    return talk['data']['fortunetext']['work']

# 获取财富运势
def getFortuneMoney():
    url = 'https://api.vvhan.com/api/horoscope'
    talk = httpGet(url, {'type': 'aries','time':'today'})
    return talk['data']['fortunetext']['money']

# 获取健康运势
def getFortuneHealth():
    url = 'https://api.vvhan.com/api/horoscope'
    talk = httpGet(url, {'type': 'aries','time':'today'})
    return talk['data']['fortunetext']['health']

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
    fortuneTitle = getFortuneTitle()
    luckyColor = getLuckyColor()
    luckyNumber = getLuckyNumber()
    luckyConstellation = getLuckyConstellation()
    shortComment = getShortComment()
    fortuneText = getFortuneText()
    fortuneLove = getFortuneLove()
    fortuneWork = getFortuneWork()
    fortuneMoney = getFortuneMoney()
    fortuneHealth = getFortuneHealth()


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
