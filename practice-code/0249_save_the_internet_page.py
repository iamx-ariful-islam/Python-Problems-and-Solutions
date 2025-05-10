# pip install pywebcopy

from pywebcopy import save_webpage


website_url     = 'https://medium.com'
download_folder = '/path/to/save'
save_webpage(website_url, download_folder)