from selenium import webdriver
import time

PATH = "/Users/anojshrestha/Documents/codes/selenium/chromedriver"
driver = webdriver.Chrome(PATH)

url = 'https://login.seek.com/login?state=g6Fo2SBjdTE5d2lrLWVMREpLVm9mdnpMTGgzbnFXRlN3UXRJU6N0aWTZIENDNTliZU12OGRzNU1kWnFfd0JBOVdBMzUtRlZpeTU5o2NpZNkgeUdCVmdlNjZLNU5KcFNONXU3MWZVOTBWY1RsRUFTTnU&client=yGBVge66K5NJpSN5u71fU90VcTlEASNu&protocol=oauth2&redirect_uri=https%3A%2F%2Fwww.seek.com.au%2Foauth%2Fcallback%2F&scope=openid%20profile%20email%20offline_access&audience=https%3A%2F%2Fseek%2Fapi%2Fcandidate&fragment=%2Flogin%3Fadobe_mc%3DMCMID%253D49652475129246558591094335418071761441%257CMCORGID%253D199E4673527852240A490D45%2540AdobeOrg%257CTS%253D1618128929&JobseekerSessionId=8efed278c66266be4bfe7575689e5c8d&response_type=code&response_mode=query&nonce=X3Jqam1aS1FaUjJ1TWZZRzRLfkVRTW9XWmNWOW93N2JhUFNMMUc0MEVQRA%3D%3D&code_challenge=vAZvLgLB4gg60LbD3U81ys1foy8nppTL-hq6Jh4djj4&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtc3BhLWpzIiwidmVyc2lvbiI6IjEuMTMuNiJ9#/?adobe_mc=MCMID%3D49652475129246558591094335418071761441%7CMCORGID%3D199E4673527852240A490D45%40AdobeOrg%7CTS%3D1618128929'
driver.maximize_window()
driver.get(url) 
time.sleep(10)
app = driver.find_element_by_id('app').find_element_by_class_name('FYwKg _3ftyQ _1lyEa _1N8Dy _14Ywq_4')
# first_class = app.find_element_by_class_name('FYwKg _3ftyQ _1lyEa _1N8Dy _14Ywq_4')

# small = browser.findElement(new ByChained(By.xpath("//div[contains(@class,'Big')]"),By.xpath("//div[contains(@class,'Medium')]"),By.xpath("//div[contains(@class,'Small')]")));

# login_email.clear()
# login_email.send_keys('bandimpal1@gmail.com')
# driver.close()
# driver.quit()