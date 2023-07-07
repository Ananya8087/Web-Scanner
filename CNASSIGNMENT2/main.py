from general import *
from domain_name import *
from ip_address import *
from n_map import *
from robots_txt import *
from whois import *

ROOT_DIR='companies'
create_dir(ROOT_DIR)

try:

    def gather_info(url):
        domain_name=get_domain_name(url)
        ip_address=get_ip_address(domain_name)
        n_map=get_nmap('-sS',ip_address)
        whois=get_whois(domain_name)
        robots_txt=get_robots_txt(url)
        
        create_report(domain_name,url,domain_name,ip_address,n_map,robots_txt,whois)

    def create_report(name,full_url,domain_name,ip_address,n_map,robots_txt,whois):
        project_dir=ROOT_DIR+'/'+name+'/'
        print(project_dir)
        create_dir(project_dir)
        write_file(project_dir+'full_url.txt',full_url)
        write_file(project_dir+'domain_name.txt',domain_name)
        write_file(project_dir+'ip_address.txt',ip_address)
        write_file(project_dir+'nmap.txt',n_map)
        write_file(project_dir+'whois.txt',whois)
        write_file(project_dir+'robots_txt.txt',robots_txt)
        
    a=input("Enter the url of the above website : ")
    print("\nScanning the website...\n")
    gather_info(a)
    print("Scan done. Check your directory for the reports.")
except:
    print("Site does not contain robots.txt file, check directory for other information")
