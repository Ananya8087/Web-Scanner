
from socket import gethostbyname
try:

    def get_ip_address(url):
        return gethostbyname(url)

    #print(get_ip_address('thenewboston.com'))
except :
    print("Cannot access website")