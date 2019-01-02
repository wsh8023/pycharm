from urllib import request,parse

if __name__ == '__main__':
    url = 'https://kyfw.12306.cn/otn/leftTicket/init?'
    zidian = {
        'linktypeid': 'dc',
        'fs': '西安北,EAY',
        'ts': '北京北,AJV',
        'date': '2019-01-16',
        'flag': 'N,N,Y'
    }
    zidianbm = parse.urlencode(zidian)
    fullurl = url + zidianbm
    rsp = request.urlopen(fullurl)
    html = rsp.read()
    html = html.decode()
    print(html)rom urllib import request,parse

if __name__ == '__main__':
    url = 'https://kyfw.12306.cn/otn/leftTicket/init?'
    zidian = {
        'linktypeid': 'dc',
        'fs': '西安北,EAY',
        'ts': '北京北,AJV',
        'date': '2019-01-16',
        'flag': 'N,N,Y'
    }
    zidianbm = parse.urlencode(zidian)
    fullurl = url + zidianbm
    rsp = request.urlopen(fullurl)
    html = rsp.read()
    html = html.decode()
    print(html)
