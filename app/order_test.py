# Reduce splinter to 0.12 to avoid bug https://stackoverflow.com/questions/60332505/unboundlocalerror-when-running-splinter-browser
import time
import logging
from splinter import Browser

logger = logging.getLogger("order_test")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("order_test.log")
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

logger.info("Open browser")
# Chrome
browser = Browser('chrome')
# Firefox
# browser = Browser()

try:
    browser.visit("https://pinggo.vn/")
    logger.info("browser title %s", browser.title)

    # Scroll a litter bit to avoid click into signup page
    logger.info("Scroll")
    browser.execute_script("window.scrollTo(200, document.body.scrollHeight);")

    # Click first item
    logger.info("Click first element")
    browser.find_by_xpath(
        "// *[ @ id = \"box-top-branch\"] / div / div[2] / div[1] / div[2] / div / div[1] / div / a").click()
    time.sleep(3)

    # Click buy now
    logger.info("Click buy")
    browser.find_by_xpath("//*[@id=\"footer-product-detail\"]/div/div[2]/a[1]").click()
    time.sleep(3)

    # Click buy now pop up
    logger.info("Click buy now")
    buy_now_button = browser.find_by_xpath(
        "/ html / body / div[1] / div[1] / div / div[1] / div / div[2] / div / div[4] / a[1]")
    buy_now_button.click()
    time.sleep(3)

    # Click process order
    logger.info("Click process order")
    browser.find_by_xpath("//*[@id='footer-cart']/div/a").click()
    time.sleep(3)

    # Fill order address and click deliver to this address
    logger.info("Fill order address and click deliver")
    browser.find_by_name("name")[1].fill("The Bot")
    browser.find_by_name("phone")[1].fill("0919999999")
    browser.find_by_name("address")[1].fill("58 Tố Hữu - Quận Nam Từ Liêm")

    print(browser.find_by_id("select-region").value)
    element_region = browser.find_by_id("select-region").first  # Running version with 1 element
    element_region.select_by_text("Hà Nội")

    time.sleep(3)

    # browser.find_by_id("select-district").fill("42")
    element_district = browser.find_by_id("select-district").first
    element_district.select_by_text("Quận Nam Từ Liêm")

    time.sleep(3)

    element_ward = browser.find_by_id("select-ward").first
    element_ward.select("660")
    browser.find_by_xpath("// *[ @ id = \"footer-button\"] / div / a").click()

    # Click Finish
    browser.find_by_xpath("/html/body/div[1]/footer/div/div/form/button").click()

    time.sleep(30)
except Exception as e:
    logger.warning(e)
finally:
    logger.info("Close browser")
    browser.quit()
