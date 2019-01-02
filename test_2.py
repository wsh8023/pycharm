import urllib.request
from urllib import parse
if __name__ == "__main__":
    url = 'https://www.baidu.com/s?'
    wd = input('input your keyword:')

    qs = {
        'wd': wd
    }
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    rsp = urllib.request.urlopen(fullurl)
    html = rsp.read()
    print(html)

