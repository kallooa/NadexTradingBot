# This module allows us to use the pop servers of Gmail
import poplib
from selenium import webdriver
from datetime import datetime, time, date
import time as tm
browser = webdriver.Chrome('chromedriver.exe')
sellRangeLower = int(input ("What is your minimum sell value: "))
sellRangeHigher = int(input ("What is your maximum sell value: "))
buyRangeLower = int(input ("What is your minimum buy value: "))
buyRangeHigher = int(input ("What is your maximum buy value: "))
gmailUser = input("Enter Gmail Email Address: ")
gmailPass = input("Enter Gmail Password: ")
popServer = "pop.gmail.com"
nadexUser = input("Enter Nadex Username: ")
nadexPass = input("Enter Nadex Password: ")


# Nadex Login Info
def nadexLogin():
    browser.get('http://www.nadex.com/login')
    #logs into the actual webpage
    usernameInput = browser.find_element_by_id('account_id')
    usernameInput.send_keys(nadexUser)
    passwordInput = browser.find_element_by_id('password')
    passwordInput.send_keys(nadexPass)
    loginButton = browser.find_element_by_id('loginbutton')
    tm.sleep(1)
    loginButton.click()
    tm.sleep(10)
    frame = browser.find_element_by_id('ifrFinder')
    browser.switch_to.frame(frame)
    fiveminbinary = browser.find_element_by_id("ygtv6")
    fiveminbinary.click()
    tm.sleep(1)
    forex = browser.find_element_by_xpath('//*[@id="ygtvc6"]')
    forex.click()


# Read incoming Gmail inbox during specified times
def readMail():
    # this is all of the login data for the mail server
    mail = poplib.POP3_SSL(popServer, 995)
    mail.user(gmailUser)
    mail.pass_(gmailPass)
    #this is where the reading of the inbox begins
    emailList = mail.list()
    emailCount = len(emailList[1])
    try:
        emailRetrieval = mail.retr(emailCount)
        # stores the email's body into a variable that contains the byte data
        emailBody = b''
        for byte in emailRetrieval[1]:
            emailBody += byte
        mail.dele(emailCount)
        mail.quit()
        print ("Latest Email has been successfully read and deleted")
    except:
        return '0'
    return emailBody.decode("UTF-8")
#reads the body to learn what currency the order is meant to be in


def readBody(rawMail):
    #this decodes the byte output of POP to a string to be used in testing later on
    body = rawMail
    if 'AUD/USD' in body:
        if 'xbuyx' in body:
            return 'AUD/BUY'
        elif 'xsellx' in body:
            return 'AUD/SELL'
        else:
            print("unexpected function (buy or sell)")
            return '0'
    elif 'EUR/JPY' in body:
        if 'xbuyx' in body:
            return 'EURJ/BUY'
        elif 'xsellx' in body:
            return 'EURJ/SELL'
        else:
            print("unexpected function (buy or sell)")
            return '0'
    elif 'EUR/USD' in body:
        if 'xbuyx' in body:
            return 'EURU/BUY'
        elif 'xsellx' in body:
            return 'EURU/SELL'
        else:
            print("unexpected function (buy or sell)")
            return '0'
    elif 'GBP/JPY' in body:
        if 'xbuyx' in body:
            return 'GBPJ/BUY'
        elif 'xsellx' in body:
            return 'GBPJ/SELL'
        else:
            print("unexpected function (buy or sell)")
            return '0'
    elif 'GBP/USD' in body:
        if 'xbuyx' in body:
            return 'GBPU/BUY'
        elif 'xsellx' in body:
            return 'GBPU/SELL'
        else:
            print("unexpected function (buy or sell)")
            return '0'
    elif 'USD/CAD' in body:
        if 'xbuyx' in body:
            return 'USDC/BUY'
        elif 'xsellx' in body:
            return 'USDC/SELL'
        else:
            print("unexpected function (buy or sell)")
            return '0'
    elif 'USD/JPY' in body:
        if 'xbuyx' in body:
            return 'USDJ/BUY'
        elif 'xsellx' in body:
            return 'USDJ/SELL'
        else:
            print("unexpected function (buy or sell)")
            return '0'
    else:
        print("Unexpected Currency")
        return '0'
# buy is right column while sell is left column


def seleniumClicksCurrencyTrade(directions):
    AUD = browser.find_element_by_xpath('//*[@id="ygtvcontentel10"]')
    EURJ = browser.find_element_by_xpath('//*[@id="ygtvcontentel14"]')
    EURU = browser.find_element_by_xpath('//*[@id="ygtvcontentel11"]')
    GBPJ = browser.find_element_by_xpath('//*[@id="ygtvcontentel15"]')
    GBPU = browser.find_element_by_xpath('//*[@id="ygtvcontentel12"]')
    USDC = browser.find_element_by_xpath('//*[@id="ygtvcontentel16"]')
    USDJ = browser.find_element_by_xpath('//*[@id="ygtvcontentel13"]')
    if directions == 'AUD/BUY':
        AUD.click()
        buyBlock()
    elif directions == 'AUD/SELL':
        AUD.click()
        sellBlock()
    elif directions == 'EURJ/BUY':
        EURJ.click()
        buyBlock()
    elif directions == 'EURJ/SELL':
        EURJ.click()
        sellBlock()
    elif directions == 'EURU/BUY':
        EURU.click()
        buyBlock()
    elif directions == 'EURU/SELL':
        EURU.click()
        sellBlock()
    elif directions == 'GBPJ/BUY':
        GBPJ.click()
        buyBlock()
    elif directions == 'GBPJ/SELL':
        GBPJ.click()
        sellBlock()
    elif directions == 'GBPU/BUY':
        GBPU.click()
        buyBlock()
    elif directions == 'GBPU/SELL':
        GBPU.click()
        sellBlock()
    elif directions == 'USDC/BUY':
        USDC.click()
        buyBlock()
    elif directions == 'USDC/SELL':
        USDC.click()
        sellBlock()
    elif directions == 'USDJ/BUY':
        USDJ.click()
        buyBlock()
    elif directions == 'USDJ/SELL':
        USDJ.click()
        sellBlock()
    else:
        print("Invalid components.")


def cleanInbox():
    mail = poplib.POP3_SSL(popServer, 995)
    mail.user(gmailUser)
    mail.pass_(gmailPass)
    emailList = mail.list()
    emailCount = len(emailList)
    for email in range(emailCount):
        try:
            mail.dele(email)
            mail.dele(email + 1)
        except:
            pass
    mail.quit()


def timecheck():
    nowTime = datetime.utcnow().time()
    nowDate = datetime.utcnow()
    if date.isoweekday(nowDate) == 1 or 2 or 3 or 4:
        seleniumClicksCurrencyTrade(readBody(readMail()))
        tm.sleep(30)
    elif date.isoweekday(nowDate)== 7: #checks if its sunday
        if nowTime.hour() > 23:
            seleniumClicksCurrencyTrade(readBody(readMail()))
            tm.sleep(30)
    elif date.isoweekday(nowDate) == 5: #checks if its friday
        if nowTime.hour() < 22:
            seleniumClicksCurrencyTrade(readBody(readMail()))
            tm.sleep(30)
        elif nowTime.hour() == 21 and nowTime.minute() < 15:
            seleniumClicksCurrencyTrade(readBody(readMail()))
            tm.sleep(30)
    else:
        cleanInbox()
        AUD = browser.find_element_by_xpath('//*[@id="ygtvcontentel10"]')
        AUD.click()
        tm.sleep(300)
def buyBlock():
    tm.sleep(1)
    browser.switch_to.default_content()
    tradingFrame = browser.find_element_by_xpath('//*[@id="ifrDealingRates"]')
    browser.switch_to.frame(tradingFrame)
    tradingTime = browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[1]/td[4]')
    tradingTimeText = tradingTime.text
    tradingTimeText = tradingTimeText[:-1]
    global counter
    if ('m' in tradingTimeText) or (int(tradingTimeText) > 30):
        try:
            buyCell1 = float(browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[1]/td[8]').text)
        except:
            pass
        try:
            buyCell2 = float(browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[2]/td[8]').text)
        except:
            pass
        try:
            buyCell3 = float(browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[3]/td[8]').text)
        except:
            pass
        try:
            buyCell4 = float(browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[4]/td[8]').text)
        except:
            pass
        try:
            buyCell5 = float(browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[5]/td[8]').text)
        except:
            pass
        try:
            buyCell5
            if (buyCell5 > buyRangeLower) and (buyCell5 < buyRangeHigher):
                buyCell5 = browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[5]/td[8]')
                buyCell5.click()
                browser.switch_to.default_content()
                tm.sleep(2)
                try:
                    betSlip = browser.find_element_by_id('ifrBetslipHolder')
                    browser.switch_to.frame(betSlip)
                    tm.sleep(3)
                    betSlipButton = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_orderTicketButton"]')
                    betSlipButton.click()
                    tm.sleep(1)
                    betSlipClose = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_OrderReceivedClose"]')
                    betSlipClose.click()
                except:
                    pass
                browser.switch_to.default_content()
                frame = browser.find_element_by_id('ifrFinder')
                browser.switch_to.frame(frame)
                counter += 1
        except:
            pass
        try:
            buyCell4
            if (buyCell4 > buyRangeLower) and (buyCell4 < buyRangeHigher):
                buyCell4 = browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[4]/td[8]')
                buyCell4.click()
                browser.switch_to.default_content()
                tm.sleep(2)
                try:
                    betSlip = browser.find_element_by_id('ifrBetslipHolder')
                    browser.switch_to.frame(betSlip)
                    tm.sleep(3)
                    betSlipButton = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_orderTicketButton"]')
                    betSlipButton.click()
                    tm.sleep(1)
                    betSlipClose = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_OrderReceivedClose"]')
                    betSlipClose.click()
                except:
                    pass
                browser.switch_to.default_content()
                frame = browser.find_element_by_id('ifrFinder')
                browser.switch_to.frame(frame)
                counter += 1
        except:
            pass
        try:
            buyCell3
            if (buyCell3 > buyRangeLower) and (buyCell3 < buyRangeHigher):
                buyCell3 = browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[3]/td[8]')
                buyCell3.click()
                browser.switch_to.default_content()
                tm.sleep(2)
                try:
                    betSlip = browser.find_element_by_id('ifrBetslipHolder')
                    browser.switch_to.frame(betSlip)
                    tm.sleep(3)
                    betSlipButton = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_orderTicketButton"]')
                    betSlipButton.click()
                    tm.sleep(1)
                    betSlipClose = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_OrderReceivedClose"]')
                    betSlipClose.click()
                except:
                    pass
                browser.switch_to.default_content()
                frame = browser.find_element_by_id('ifrFinder')
                browser.switch_to.frame(frame)
                counter += 1
        except:
            pass
        try:
            buyCell2
            if (buyCell2 > buyRangeLower) and (buyCell2 < buyRangeHigher):
                buyCell2 = browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[2]/td[8]')
                buyCell2.click()
                browser.switch_to.default_content()
                tm.sleep(2)
                try:
                    betSlip = browser.find_element_by_id('ifrBetslipHolder')
                    browser.switch_to.frame(betSlip)
                    tm.sleep(3)
                    betSlipButton = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_orderTicketButton"]')
                    betSlipButton.click()
                    tm.sleep(1)
                    betSlipClose = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_OrderReceivedClose"]')
                    betSlipClose.click()
                except:
                    pass
                browser.switch_to.default_content()
                frame = browser.find_element_by_id('ifrFinder')
                browser.switch_to.frame(frame)
                counter += 1
        except:
            pass
        try:
            buyCell1
            if (buyCell1 > buyRangeLower) and (buyCell1 < buyRangeHigher):
                buyCell1 = browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[1]/td[8]')
                buyCell1.click()
                browser.switch_to.default_content()
                tm.sleep(2)
                try:
                    betSlip = browser.find_element_by_id('ifrBetslipHolder')
                    browser.switch_to.frame(betSlip)
                    tm.sleep(3)
                    betSlipButton = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_orderTicketButton"]')
                    betSlipButton.click()
                    tm.sleep(1)
                    betSlipClose = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_OrderReceivedClose"]')
                    betSlipClose.click()
                except:
                    pass
                browser.switch_to.default_content()
                frame = browser.find_element_by_id('ifrFinder')
                browser.switch_to.frame(frame)
                counter += 1
        except:
            pass
    browser.switch_to.default_content()
    frame = browser.find_element_by_id('ifrFinder')
    browser.switch_to.frame(frame)

def sellBlock():
    tm.sleep(1)
    browser.switch_to.default_content()
    tradingFrame = browser.find_element_by_xpath('//*[@id="ifrDealingRates"]')
    browser.switch_to.frame(tradingFrame)
    tradingTime = browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[1]/td[4]')
    tradingTimeText = tradingTime.text
    tradingTimeText = tradingTimeText[:-1]
    global counter
    if ('m' in tradingTimeText) or (int(tradingTimeText) > 30):
        try:
            sellCell1 = float(browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[1]/td[7]').text)
        except:
            pass
        try:
            sellCell2 = float(browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[2]/td[7]').text)
        except:
            pass
        try:
            sellCell3 = float(browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[3]/td[7]').text)
        except:
            pass
        try:
            sellCell4 = float(browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[4]/td[7]').text)
        except:
            pass
        try:
            sellCell5 = float(browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[5]/td[7]').text)
        except:
            pass
        try:
            sellCell1
            if (sellCell1 > sellRangeLower) and (sellCell1 < sellRangeHigher):
                sellCell1 = browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[1]/td[7]')
                sellCell1.click()
                browser.switch_to.default_content()
                tm.sleep(2)
                try:
                    betSlip = browser.find_element_by_id('ifrBetslipHolder')
                    browser.switch_to.frame(betSlip)
                    tm.sleep(3)
                    betSlipButton = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_orderTicketButton"]')
                    betSlipButton.click()
                    tm.sleep(1)
                    betSlipClose = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_OrderReceivedClose"]')
                    betSlipClose.click()
                except:
                    pass
                browser.switch_to.default_content()
                frame = browser.find_element_by_id('ifrFinder')
                browser.switch_to.frame(frame)
                counter += 1
        except:
            pass
        try:
            sellCell2
            if (sellCell2 > sellRangeLower) and (sellCell2 < sellRangeHigher):
                sellCell2 = browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[2]/td[7]')
                sellCell2.click()
                browser.switch_to.default_content()
                tm.sleep(2)
                try:
                    betSlip = browser.find_element_by_id('ifrBetslipHolder')
                    browser.switch_to.frame(betSlip)
                    tm.sleep(3)
                    betSlipButton = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_orderTicketButton"]')
                    betSlipButton.click()
                    tm.sleep(1)
                    betSlipClose = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_OrderReceivedClose"]')
                    betSlipClose.click()
                except:
                    pass
                browser.switch_to.default_content()
                frame = browser.find_element_by_id('ifrFinder')
                browser.switch_to.frame(frame)
                counter += 1
        except:
            pass
        try:
            sellCell3
            if (sellCell3 > sellRangeLower) and (sellCell3 < sellRangeHigher):
                sellCell3 = browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[3]/td[7]')
                sellCell3.click()
                browser.switch_to.default_content()
                tm.sleep(2)
                try:
                    betSlip = browser.find_element_by_id('ifrBetslipHolder')
                    browser.switch_to.frame(betSlip)
                    tm.sleep(3)
                    betSlipButton = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_orderTicketButton"]')
                    betSlipButton.click()
                    tm.sleep(1)
                    betSlipClose = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_OrderReceivedClose"]')
                    betSlipClose.click()
                except:
                    pass
                browser.switch_to.default_content()
                frame = browser.find_element_by_id('ifrFinder')
                browser.switch_to.frame(frame)
                counter += 1
        except:
            pass
        try:
            sellCell4
            if (sellCell4 > sellRangeLower) and (sellCell4 < sellRangeHigher):
                sellCell4 = browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[4]/td[7]')
                sellCell4.click()
                browser.switch_to.default_content()
                tm.sleep(2)
                try:
                    betSlip = browser.find_element_by_id('ifrBetslipHolder')
                    browser.switch_to.frame(betSlip)
                    tm.sleep(3)
                    betSlipButton = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_orderTicketButton"]')
                    betSlipButton.click()
                    tm.sleep(1)
                    betSlipClose = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_OrderReceivedClose"]')
                    betSlipClose.click()
                except:
                    pass
                browser.switch_to.default_content()
                frame = browser.find_element_by_id('ifrFinder')
                browser.switch_to.frame(frame)
                counter += 1
        except:
            pass
        try:
            sellCell5
            if (sellCell5 > sellRangeLower) and (sellCell5 < sellRangeHigher):
                sellCell5 = browser.find_element_by_xpath('//*[@id="table-1linked"]/tbody/tr[5]/td[7]')
                sellCell5.click()
                browser.switch_to.default_content()
                tm.sleep(1)
                try:
                    betSlip = browser.find_element_by_id('ifrBetslipHolder')
                    browser.switch_to.frame(betSlip)
                    tm.sleep(3)
                    betSlipButton = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_orderTicketButton"]')
                    betSlipButton.click()
                    tm.sleep(1)
                    betSlipClose = browser.find_element_by_xpath('//*[@id="ticket'+ str(counter) +'_OrderReceivedClose"]')
                    betSlipClose.click()
                except:
                    pass
                browser.switch_to.default_content()
                frame = browser.find_element_by_id('ifrFinder')
                browser.switch_to.frame(frame)
                counter += 1
        except:
            pass
    browser.switch_to.default_content()
    frame = browser.find_element_by_id('ifrFinder')
    browser.switch_to.frame(frame)


def startup():
    cleanInbox()
    nadexLogin()


if __name__ == '__main__':
    startup()
    counter = 1
    while True:
        timecheck()
        tm.sleep(30)

