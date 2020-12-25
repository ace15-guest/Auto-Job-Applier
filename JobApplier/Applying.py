from selenium import webdriver
from Formpop import *
import time
from selenium.webdriver.remote.webelement import WebElement
from pynput.mouse import Button, Controller
import os.path
from selenium.webdriver.support.select import Select

#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
class JobApplier:
    def __init__(self):
        # self.root = Tk(root)
        # self.b=Form(root)
        # self.root.title("Stanley Black & Decker Auto Apply")
        # self.root.mainloop()

# PATH = b.Driver
        self.PATH = "C:\chromedriver"
        self.driver = webdriver.Chrome(self.PATH)
        self.goWeb("https://sjobs.brassring.com/TGnewUI/Search/home/HomeWithPreLoad?PageType=JobDetails&partnerid=165&siteid=20&jobid=857665&_ga=2.122171150.444491190.1608093494-212880056.1608093494#home")

        self.goHome()
        self.login()
        self.goHome()
        self.jobSearch()



    def goWeb(self, link): #Go to some link on SBaD
        self.driver.get(link)

    def goHome(self):
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.implicitly_wait(4)
        Home = self.driver.find_element_by_xpath("//a[@ng-if='tgSettings.JobSearchHeaderText && bShowBackButton && (standAloneGQ <= 0)']")
        Home.click()
        self.driver.implicitly_wait(4)
        print("Succesfully navigated Home")

    def jobSearch(self):
        JobFill = self.driver.find_element_by_xpath("//input[@name='keyWordSearch']")
        JobFill.send_keys("Mechanical")
        self.driver.implicitly_wait(5)
        search= self.driver.find_element_by_xpath("//button[@ng-click='searchMatchedJobs(this)']")
        search.click()
        Num_job = self.driver.find_elements_by_xpath("//a[@ng-click='handlers.jobClick($event, this)']")

        time.sleep(4)
        Num_job = self.driver.find_elements_by_xpath("//a[@ng-click='handlers.jobClick($event, this)']")
        for i in range(len(Num_job)):
            Num_job[i].click()
            self.fillInfo()
            time.sleep(2)
            print("Job Information is filled")

    def login(self):
        self.driver.implicitly_wait(1)
        e_address = self.driver.find_element_by_xpath("//input[@ng-model='loginField']")
        e_address.send_keys("Your Email")
        self.driver.implicitly_wait(1)
        p_word = self.driver.find_element_by_xpath("//input[@name='password']")
        p_word.send_keys("Your Password")
        signin = self.driver.find_element_by_xpath("//button[@type='submit']")
        signin.click()
        print("Login Complete")

    def fillInfo(self):
        #Click job# on page1
        # Num_job[i].click()
        time.sleep(4)
        self.driver.implicitly_wait(4)
        # Num_job[i].click()
        time.sleep(10)
        s_t_j = self.driver.find_element_by_id("applyFromDetailBtn")

        s_t_j.click()
        time.sleep(5)
        self.driver.implicitly_wait(3)
        time.sleep(6)
        #Lets get started
        l_g_s = self.driver.find_element_by_xpath("//button[@type='button']")
        l_g_s.click()
        time.sleep(2)
        try:
            self.WDYH()
            print("Where did you hear specified")
        except:
            print("Where Did you hear Is not a question on this application")
        try:
            self.Authorization()
            print("Authorized")
        except:
            print("They Do not care if you are authorized to work in the USA")
        try:
            self.fluency()
            print("Language Specified")
        except:
            print("No language requirements")
        try:
            self.diploma()
        except:
            print("No Diploma Needed")
        try:
            self.locpref()
            print("Location Specified")
        except:
            print("No location needed")
        time.sleep(3)
        self.nxtPg()
        self.submitApp()

        #----------resume-------------#
        U_resume = self.driver.find_element_by_xpath("//a[@id='AddResumeLink']")
        U_resume.click()
        time.sleep(3)
        self.dragRes()

    def WDYH(self):
        # ----------Where Did You Hear-------------#
        w_d = self.driver.find_element_by_xpath("//span[@class='ui-selectmenu-text']")
        w_d.send_keys("Facebook")
        print("We heard from Facebook")
    def Authorization(self):
        # ----------Authorization-------------#
        c_yes = self.driver.find_elements_by_xpath("//input[@value='Yes']")
        for i in range(len(c_yes)):
            c_yes[i].click()
    def fluency(self):
        #----fluency-----#
        drop = self.driver.find_element_by_xpath("//*[@id='jsq-862350_32296_0_fname_mslt_0_0-button']/span[1]")
        drop.click()
        english = self.driver.find_element_by_xpath("//*[@id='jsq-862350_32296_0_fname_mslt_0_0-menu']/li[1]")
        english.click()
    def diploma(self): #highschool diploma or GED
        hsd = self.driver.find_element_by_xpath("//span[@class='ui-selectmenu-text']")
        hsd.click()
    def locpref(self):
        loc = self.driver.find_element_by_xpath("//*[@id='div-50719']/div[2]/div/div[17]/div/div")
        loc.send_keys("Anywhere")

    def dragRes(self):
        #-----Make sure resume is located in upper right of screen-----#
        self.driver.set_window_position(0, 0)
        mouse = Controller()
        mouse.position=(1851,14)
        mouse.press(Button.left)
        time.sleep(2)
        mouse.move(-1435, 477)
        time.sleep(1)
        mouse.release(Button.left)
        time.sleep(5)
        self.nxtPg()
    def submitApp(self):
        sendApp = self.driver.find_element_by_xpath("//button[@type='button']")
        sendApp.click()
    def nxtPg(self):
        # ----------save and continue-------------#
        cont_link = self.driver.find_elements_by_xpath("//button[@id='shownext']")
        cont_link[0].click()
        print("done")
        time.sleep(4)


hi=JobApplier()
#---------------------------------------------#
#Applying to Job



# First_name=driver.find_element_by_xpath("input[@name='profile_1_0_firstname_txt_0']")
# First_name.send_keys("Asa")





# Br=driver.find_element_by_partial_link_text('Saved')
# dropzone = driver.find_elements_by_xpath("//*")
# print(dropzone)
# for i in range(1000):
#     for j in range(1000):
#         for q in range(len(dropzone)):
#             try:
#                 dropzone[q].drop_files("C:/Users/guest_2dn55ag/OneDrive/Desktop/Asa_Guest_Resume_9_30.docx",offsetX=i,offsetY=j)
#             except Noniterable:
#                 print(dropzone[q],"not iterable")
#             print(i,j,q)
# #--------------Gender/Race---------------#
# # gender = driver.find_elements_by_css_selector("span[class='ui-selectmenu-text']")

