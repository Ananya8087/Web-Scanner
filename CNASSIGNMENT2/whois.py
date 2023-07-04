import os
try :

    def get_whois(url):
        command="whois "+url
        process=os.popen(command)
        results=str(process.read())
        return results
    #print(get_whois('thenewboston.com'))
except:
    print("Cannot access website")
