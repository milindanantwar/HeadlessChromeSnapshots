from Screenshot import Screenshot_Clipping
from selenium import webdriver



ob=Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome(r"C:\Users\MilindAnantwar\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\chromedriver")
url = "https://webglsamples.org/blob/blob.html"
driver.get(url)
img_url=ob.full_Screenshot(driver, save_path=r'D:\Python', image_name='Myimage.png')
print(img_url)
driver.close()

driver.quit()
