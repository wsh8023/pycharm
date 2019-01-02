from urllib import request, error

if __name__ == "__main__":
    url = 'http://www.baidu.com'

    proxy = {'http':"140.227.202.8:3128	"}
    proxy_handler = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_handler)
    request.install_opener(opener)

    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
