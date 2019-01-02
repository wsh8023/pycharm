from urllib import request, parse

if __name__ == '__main__':
    url = 'https://kyfw.12306.cn/otn/leftTicket/init?'
    zidian = {
        'fs': '西安北,EAY',
        'ts': '北京北,AJV',
    }
    zidian1 = {
        'linktypeid': 'dc',
        'date': '2019-01-16',
        'flag': 'N,N,Y'
    }
    zidianbm = parse.urlencode(zidian)
    zidian = zidianbm + zidian1
    print(zidian)


