# pip install speedtest

import speedtest as st


def speed_test():
    test = st.Speedtest()
    
    # download speed
    down_speed = test.download()
    down_speed = round(down_speed/10**6, 2)
    print('Download Speed in Mbps:', down_speed)
    
    # upload speed
    up_speed = test.upload()
    up_speed = round(up_speed/10**6, 2)
    print('Upload Speed in Mbps:', up_speed)
    
    # show the ping
    ping = test.results.ping
    print('Ping:', ping)
    
# call the function
speed_test()