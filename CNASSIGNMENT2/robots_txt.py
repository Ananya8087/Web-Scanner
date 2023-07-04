
import urllib.request
import io
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
try :

    def get_robots_txt(url):
        if url.endswith("/"):
            path = url
        else:
            path = url + '/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        req = urllib.request.Request(path + "robots.txt", data=None, headers=headers)
        try:
            data = io.TextIOWrapper(urllib.request.urlopen(req), encoding='utf-8')
            return data.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print("Error 404: The resource was not found.")
            else:
                print("HTTP Error:", e.code, e.reason)

    #print(get_robots_txt('https://www.pesuacademy.com'))
except:
    print("Cannot access website")
