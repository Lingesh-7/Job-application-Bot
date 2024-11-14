
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv

load_dotenv()

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=chrome_option)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3944224089&f_AL=true&geoId=103112676&keywords=Pyhton%20Developer&location=Chicago%2C%20Illinois%2C%20United%20States&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")
time.sleep(10)
login=driver.find_element(By.XPATH,value="/html/body/div[2]/a[1]")
login.click()
time.sleep(10)
email=driver.find_element(By.XPATH,value="//*[@id='username']")
email_=os.environ.get('EMAIL')
email.send_keys(f"{email_}",Keys.ENTER)
password=driver.find_element(By.XPATH,value="//*[@id='password']")
pass_=os.environ.get('PASSS')
password.send_keys(f"{pass_}",Keys.ENTER)

print("Sucess Fully Loged IN!!!")


time.sleep(60)
jobs=driver.find_elements(By.CSS_SELECTOR,value=".job-card-container--clickable")
job_name=[i.text for i in jobs]
print(len(job_name))

s=0
c=0

for job in jobs:
    time.sleep(10)
    job.click()
    # break
    time.sleep(5)
    try:
        print(f"{job.text} is opening!!!")
        easy_apply=driver.find_element(By.CSS_SELECTOR,value=".jobs-apply-button--top-card button")
        easy_apply.click()
        time.sleep(5)
        phone_num=driver.find_element(By.CSS_SELECTOR,value=".jobs-easy-apply-modal__content div div form div div div div div div div input")
        if phone_num.text==" ":
            phone_num.send_keys("9545629123")
        time.sleep(5)
        next_=driver.find_element(By.CSS_SELECTOR,value=".jobs-easy-apply-modal__content div div form footer div button")
        next_.click()
        time.sleep(5)
        next_2=driver.find_elements(By.CSS_SELECTOR,value=".jobs-easy-apply-modal__content div div form footer div button")[1]
        if next_2.text=="Review":
            print(f"{next_2.text}")
            next_2.click()
            time.sleep(5)
            submission_app=driver.find_elements(By.CSS_SELECTOR,value=".justify-flex-end button")[1]
            submission_app.click()
            time.sleep(5)
            print("Application Submitted SucesssFully!!!")
            time.sleep(10)
            done=driver.find_element(By.CSS_SELECTOR,value="#artdeco-modal-outlet div div div button")
            done.click()
            s+=1
            time.sleep(10)
            continue
        else:
            print(f"{next_2.text}")
            time.sleep(5)
            exits=driver.find_element(By.CSS_SELECTOR,value="#artdeco-modal-outlet div div button")
            exits.click()
            time.sleep(5)
            discard=driver.find_element(By.CSS_SELECTOR,value=".artdeco-modal__actionbar--confirm-dialog button")
            discard.click()
            print("Complex APPLICATION!!!")
            c+=1
        
        # print
        # continue
    except NoSuchElementException:
        s+=1
        # print(f"{job.text} is Complex")
        # # easy_apply=driver.find_element(By.CSS_SELECTOR,value=".jobs-apply-button--top-card button")
        # # easy_apply.click()
        # time.sleep(5)
        # exits=driver.find_element(By.CSS_SELECTOR,value="#artdeco-modal-outlet div div button")
        # exits.click()
        # time.sleep(5)
        # discard=driver.find_element(By.CSS_SELECTOR,value=".artdeco-modal__actionbar--confirm-dialog button")
        # discard.click()
        continue

print(f"Total application {len(job_name)}\nNumber of Application submitted {s} \nNumber of Application Complex {c}")
time.sleep(5)
driver.quit()





















    #     time.sleep(5)
    #     
    #     time.sleep(3)
    #     # next_=driver.find_element(By.CSS_SELECTOR,value=".jobs-easy-apply-modal__content div div form footer button")
    #     # next_.click()

    #     # time.sleep(3)
    #     # review=driver.find_elements(By.CSS_SELECTOR,value=".justify-flex-end button")[1]
    #     # review.click()

    #     time.sleep(3)
    #     submission_app=driver.find_elements(By.CSS_SELECTOR,value=".justify-flex-end button")[1]
    #     if submission_app.get_attribute("data-control-name")=="continue_unify":
    #         print("Complex Application,SKIPPED!!!")
    #         close_button=driver.find_element(By.CLASS_NAME,value="artdeco-modal__dismiss")
    #         close_button.click()
    #     else:
    #         submission_app.click()
    #     time.sleep(5)
    #     DONE=driver.find_element(By.CSS_SELECTOR,value=".artdeco-modal__actionbar button")
    #     DONE.click()
    
    # except NoSuchElementException:
    #     print("NO APPLICATION FOUND")
    #     continue

# time.sleep(5)
# driver.quit()







# time.sleep(60)
# # easy_apply=driver.find_element(By.XPATH,value="//*[@id='ember156']")
# # easy_apply.click()


# job=driver.find_element(By.CSS_SELECTOR,value=".jobs-apply-button--top-card button")
# job.click()
# #//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3942491466-816164661-phoneNumber-nationalNumber"]
# time.sleep(10)
# phone_num=driver.find_element(By.XPATH,value="//*[@id='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3942491466-816164661-phoneNumber-nationalNumber']")
# phone_num.send_keys("9545629123")

# next_=driver.find_element(By.CSS_SELECTOR,value=".jobs-easy-apply-modal__content div div form footer button")
# next_.click()


# next_2=driver.find_elements(By.CSS_SELECTOR,value=".jobs-easy-apply-modal__content div div form footer div button")[1]
# next_2.click()

# ans_1=driver.find_element(By.XPATH,value="//*[@id='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3942491466-816164885-numeric']")
# ans_1.send_keys("0")

# ans_2=driver.find_element(By.XPATH,value="//*[@id='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3942491466-816164877-numeric']")
# ans_2.send_keys("0")

# ans_3=driver.find_element(By.XPATH,value="//*[@id='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3942491466-816164861-numeric']")
# ans_3.send_keys("0")


# tick_1=driver.find_element(By.XPATH,value="//*[@id='radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3942491466-816164869-multipleChoice']/div[1]/label")
# tick_1.click()

# tick_2=driver.find_element(By.XPATH,value="//*[@id='radio-button-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3942491466-816164853-multipleChoice']/div[1]/label")
# tick_2.click()

# time.sleep(3)
# review=driver.find_elements(By.CSS_SELECTOR,value=".justify-flex-end button")[1]
# review.click()


# time.sleep(3)
# submission_app=driver.find_elements(By.CSS_SELECTOR,value=".justify-flex-end button")[1]
# submission_app.click()








