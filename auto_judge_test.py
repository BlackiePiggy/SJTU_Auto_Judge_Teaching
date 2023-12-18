from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 创建Edge WebDriver实例
driver = webdriver.Edge()

# 打开网站
driver.get("http://yjs.sjtu.edu.cn/gsapp/sys/wspjapp/*default/index.do?")

# 无限等待，用户可以与网页进行交互
input('Press Enter to quit...')

# 关闭浏览器
driver.quit()
