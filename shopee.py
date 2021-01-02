import time
import pyfiglet as f
from config import link_produk, pin_number,cookiee
import undetected_chromedriver as UC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from fake_useragent import UserAgent

UC.TARGET_VERSION = 87 # Versi chrome

options = UC.ChromeOptions()
options.headless = True
options.add_argument('--disable-extensions')
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
prefs = {'profile.default_content_setting_values': {'images': 2,
                            'plugins': 2, 'popups': 2, 'geolocation': 2,
                            'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                            'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                            'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                            'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                            'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                            'durable_storage': 2}}
options.add_experimental_option("prefs", prefs)
browser = UC.Chrome(options=options, enable_console_log=True)

def authors():
    style = f.figlet_format("Shopee Bot www.sans.eu.org")
    print(style)
    print("\033[31m----- \033[93mGithub : \033[92mhttps://github.com/ngeteng \033[31m-----")
    print("\033[31m-----  \033[93mWebsite : \033[92mhttps://www.sans.eu.org   \033[31m-----")

def load_cookies():
    browser.get("https://shopee.co.id")
    browser.add_cookie({'name': 'SPC_EC', 'value': cookiee})
    browser.get_cookies()
    time.sleep(2)
    print('\033[32m[+] Driver init suksess,...')

def tombol_beli():
    try:
#        varians = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Merlot')]")))
#        browser.execute_script("arguments[0].click();", varians) bila ada variant tinggal ganti di bagian Merlot
        beli = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]')))
        browser.execute_script("arguments[0].click();", beli)
        print("\033[32m[+] INFO: Barang terbeli! Dalam\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")
        checkout = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button/span')))
        browser.execute_script("arguments[0].click();", checkout)
        print("\033[32m[+] INFO: Barang otw Checkout!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")
        pesanan = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[4]/div[2]/div[7]/button')))
        browser.execute_script("arguments[0].click();", pesanan)
        print("\033[32m[+] INFO: Pesanan Dibuat!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")
        bayar = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.ID, 'pay-button'))).click()
        browser.execute_script("arguments[0].click();", bayar)
        print("\033[32m[+] INFO: Otw Bayar!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")
        pin_shopee = WebDriverWait(browser, 1200).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pin-popup"]/div[1]/div[3]/div[1]')))
        browser.execute_script("arguments[0].click();", pin_shopee)
        pin_shopee.send_keys(pin_number)
        print("\033[32m[+] INFO: Uhuiy,..Dapet!\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mDetik")
    except NoSuchElementException as e:
        print(e)

def main():
    minute = int(time.strftime("%M", time.localtime()))
    authors()
    time.sleep(3)
    load_cookies()
    browser.get(link_produk)
    menit = int(input("\033[32m[+] Masukan menit untuk memulai beli : "))
    Inter = 0

    while minute != menit :
        minute = int(time.strftime("%M", time.localtime()))
        Inter += 1
        if minute != menit :
            browser.refresh()
            print("\033[32m[+] INFO:\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mBelum mulai.!")
        else:
            break

    tombol_beli()

if __name__ == "__main__":
    main()
