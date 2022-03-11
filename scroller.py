import time
from selenium import webdriver

class scroller:
    def getfullhtml(URL):
        # Web scrapper for infinite scrolling page 
        driver = webdriver.Chrome(executable_path=r"/usr/bin/chromedriver")
        driver.get(URL)
        #driver.get("https://www.reddit.com/search/?q=r%2FCOVID19")

        time.sleep(2)  # Allow 2 seconds for the web page to open
        scroll_pause_time = 2.5 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
        screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
        i = 1

        while True:
            # scroll one screen height each time
            driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
            i += 1
            time.sleep(scroll_pause_time)
            # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
            scroll_height = driver.execute_script("return document.documentElement.scrollHeight")

            # Break the loop when the height we need to scroll to is larger than the total scroll height
            #print("screen_height: " +str(screen_height) +", i:"+str(i)+", scroll_height: "+str(scroll_height))
            if (screen_height) * i > scroll_height:
                break
        l = driver.find_element_by_css_selector("body")
        h= driver.execute_script("return arguments[0].innerHTML;",l)
        #print("HTML code of element: " + h)
        driver.close()

        return h