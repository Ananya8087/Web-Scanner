from tld import get_fld

#user doesn't have to worry about what format the url is
def get_domain_name(url):
    domain_name = get_fld(url) #tld=top level domain
    return domain_name

#print(get_domain_name('https://drive.google.com/drive/folders/1WqkduFNt4HyNtW7FIKjgazTfU173LZbl'))

