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

# 获取天气
def getWeather(abCode, key):
    url = 'https://restapi.amap.com/v3/weather/weatherInfo'
    params = {
        'key': key,
        'city': abCode,
        'extensions': 'base',
        'output': 'JSON',
    }
    return httpGet(url, params)

# 获取一句情话
def getMorningGreeting():
    url = 'https://api.vvhan.com/api/love'
    love = httpGet(url, {'type': 'json'})
    return love['ishan']

# 获取生日倒计时
def getBirthDays(birthDay):
    currentDate = str(datetime.now())
    temp = currentDate[:4]
    tempBirthday = temp + '-' + birthDay
    currentbirthDay = datetime.strptime(tempBirthday, '%Y-%m-%d')
    interval = currentbirthDay - datetime.now()
    if (interval.days >= 0):
        leftDay = interval.days + 1
    else:
        temp = int(temp) + 1
        tempBirthday = str(temp) + '-' + birthDay
        birthDay = datetime.strptime(tempBirthday, '%Y-%m-%d')
        interval = birthDay - datetime.now()
        leftDay = interval.days + 1
    return leftDay

# 获取在一起天数
def getTogetherDays(togetherDay):
    togetherDay = datetime.strptime(togetherDay, '%Y-%m-%d')
    interval = datetime.now() - togetherDay
    return interval.days

# 发送模版消息
def sendTemplateMessage(content, accessToken):
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=' + accessToken
    return httpPost(url, content)

# 获取星期
def getWeek():
    w = datetime.now().strftime('%w')
    data = {
        0: '天',
        1: '一',
        2: '二',
        3: '三',
        4: '四',
        5: '五',
        6: '六'
    }
    return data[int(w)]

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
    # 高德天气API key
    gaoDeKey = 'xxx'
    # 所在地点abCode（高德后台可以获取 https://a.amap.com/lbs/static/amap_3dmap_lite/AMap_adcode_citycode.zip）
    abCode = '610113'
    # 填写公历生日的日期，月-日
    birthDay = '11-01'
    # 在一起的时间
    togetherDay = '2022-11-01'

    accessTokenInfo = getAccessToken(appId, appSecret)
    accessToken = accessTokenInfo['access_token']
    weatherInfo = getWeather(abCode, gaoDeKey)
    weather = weatherInfo['lives'][0]
    sentence = getMorningGreeting()
    birthDays = getBirthDays(birthDay)
    togetherDays = getTogetherDays(togetherDay)
    week = getWeek()
    name = getNickName()

    for i in range(len(openIdList)):
        data = {
            'touser': openIdList[i],
            'template_id': templateId,
            'topcolor' : '#FF0000',
            'data': {
                'date': {
                    'value': datetime.now().strftime('%Y-%m-%d'),
                },
                'province': {
                    'value': weather['province']
                },
                'city': {
                    'value': weather['city']
                },
                'temperature': {
                    'value': weather['temperature'],
                    'color': '#4d79ff'
                },
                'humidity': {
                    'value': weather['humidity'],
                    'color': '#4d79ff'
                },
                'winddirection': {
                    'value': weather['winddirection'],
                },
                'windpower': {
                    'value': weather['windpower']
                },
                'togetherDays': {
                    'value': togetherDays,
                    'color': '#ff4dff'
                },
                'birthDays': {
                    'value': birthDays,
                    'color': '#ff4dff'
                },
                'week': {
                    'value': week,
                },
                'sentence': {
                    'value': sentence,
                    'color': '#ed556a'
                },
                'name':{
                    'value': name,
                    'color': '#ee3f4d'
                }
            }
        }
        params = json.dumps(data)

        print(sendTemplateMessage(params, accessToken))
