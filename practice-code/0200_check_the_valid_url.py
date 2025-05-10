import re

def is_valid_url(url):
    regex = re.compile(
        r'^(https?|ftp)://'  # protocol (http, https, or ftp)
        r'([a-zA-Z0-9.-]+)?'  # domain name or IP
        r'(\.[a-zA-Z]{2,})'  # top-level domain
        r'(:\d+)?'  # optional port
        r'(\/[a-zA-Z0-9@:%_+.~#?&//=]*)?$'  # path and query parameters
    )
    return re.match(regex, url) is not None


print(is_valid_url('https://www.google.com'))
print(is_valid_url('www.google'))


'''output:

True
False
'''