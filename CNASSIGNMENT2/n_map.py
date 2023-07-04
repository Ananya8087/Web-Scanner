import os 

#tool that allows you to scan a server and find out what processes are running and what ports are in
#nmap -F scans quickly. common ports.
try :

    def get_nmap(options,ip):
        command = "sudo nmap " + options + " " + ip
        process = os.popen(command)
        results = str(process.read())
        return results

    #print(get_nmap('-sS','142.250.192.110'))
except:
    print("Cannot access website")