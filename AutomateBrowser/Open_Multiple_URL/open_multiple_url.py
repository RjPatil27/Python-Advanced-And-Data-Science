''' This code is for opening multiple URLs in required browser
here we are using selenium.webdriver module for opening multiple URLs in Mozilla browser.
main motto is to open text file which contain database of multiple URLs in browser and find out its opening time, closing time
and complete time to open website. And write all this data into another text file.
'''

#time library for calculating start and end time 
import time
#selenium gives us features to automate the browser.
from selenium import webdriver

file = open("url.txt", 'r')
file2 = open('urltime.txt','w')
numlines = 0
print(file)

with file as f:
    content = f.readlines()

print(content)

'''
Actually The Selenium client bindings tries to locate the "geckodriver" executable from the system PATH.
You will need to add the directory containing the executable to the system path.
donwload this file and store it folder and pass the path of geckodriver to webdriver.Firefox()
''
driver =webdriver.Firefox(executable_path='//home/sai//Music//Rajat//geckodriver-v0.23.0-linux64//geckodriver')

for i in range(0,3):
    start = time.time()
    print(start)
    url = content[i].rstrip()
    #open_page(url)
    driver.get(url)
    print(url)
    end = time.time()
    print(end)
    print("time taken to start URL  = ", end - start)
    file2.writelines(url + '\t' + str(start) + '\t' + str(end) + '\t' + str(end-start))
    file2.writelines('\n')
#quit the opening driver of browser
driver.quit()
