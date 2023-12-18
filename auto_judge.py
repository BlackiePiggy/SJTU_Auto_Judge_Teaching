from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# 创建Edge WebDriver实例
driver = webdriver.Edge()

# 打开网页
driver.get("http://yjs.sjtu.edu.cn/gsapp/sys/wspjapp/*default/index.do?EMAP_LANG=zh#/wspj")

# 等待用户登录
time.sleep(2)

username = driver.find_element(By.ID, "user")
username.send_keys("jason_lee")
psswd = driver.find_element(By.ID, "pass")
psswd.send_keys("Noreason12345")

#等待输入验证码
time.sleep(7)

while True:
    try:
        # 关闭弹窗
        close_button = driver.find_element(By.ID, "guideShut")
        close_button.click()
    except NoSuchElementException:
        pass

    # 找到所有标记为"未评教"的元素并点击
    panels = driver.find_elements(By.CLASS_NAME, "sc-panel-diagonalStrips")
    for panel in panels:
        if "未评教" in panel.text:
            panel.click()
            break

    # 等待新页面加载
    time.sleep(2)

    try:
        # 关闭弹窗
        close_button = driver.find_element(By.ID, "guideShut")
        close_button.click()
    except NoSuchElementException:
        pass

    # 对所有的评教选项进行操作
    radio_divs = driver.find_elements(By.CLASS_NAME, "bh-radio.bh-radio-group-v")
    for div_son_index in len(radio_divs)-1:
        scroll_ref = driver.find_element_by_xpath("//radio_divs[div_son_index]/../span[1]").text
        first_label = radio_divs[div_son_index].find_element(By.TAG_NAME, "label")
        driver.execute_script("arguments[0].scrollIntoView();", first_label)
        first_label.click()

    # 填写评教文本
    textarea = driver.find_element(By.CSS_SELECTOR, "textarea[role='pj_form_text']")
    textarea.send_keys("老师非常棒，期待下次再上老师的课！")

    # 提交评教
    submit_button = driver.find_element(By.CSS_SELECTOR, "a[data-action='提交']")
    submit_button.click()

    time.sleep(0.5)

    # 确认提交
    confirm_button = driver.find_element(By.CSS_SELECTOR, "a.bh-dialog-btn.bh-bg-primary.bh-color-primary-5")
    confirm_button.click()

    # 等待页面跳转
    time.sleep(5)