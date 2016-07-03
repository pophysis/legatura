import selenium.webdriver as webdriver
import contextlib
from pyvirtualdisplay import Display
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import time

#set webdriver logging preferences
caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}

#get time to use for file name
timeStamp = time.time()

#get url
getUrl = raw_input("Please enter the URL: ")

print "Getting URL " + getUrl

#setup display and hide so we don't see the browser
display = Display(visible=0, size=(1024, 768))
display.start()

@contextlib.contextmanager
def urlize(browser):
    yield browser
    browser.quit()


with urlize(webdriver.Chrome(desired_capabilities=caps)) as driver:
    #driver.implicitly_wait(10)
    driver.get(getUrl)
    title = driver.title
    driver.get_screenshot_as_file('/tmp/'+str(timeStamp)+' '+title+'.png') 
    # driver.save_screenshot('/tmp/google.png')
    for entry in driver.get_log('performance'):
	data = json.loads(entry['message'])
	try:
	   mime =  data['message']['params']['response']['mimeType']
	   print mime
	except:
           pass
	if(mime and mime == "text/html"):
	   try:
	      print data['message']['params']['response']['url']
           except:
	      pass
display.stop()

