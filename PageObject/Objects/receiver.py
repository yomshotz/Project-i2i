import datetime

class Receiver:
    now = datetime.datetime.now()
    year = str(now.year)
    date = str(now.day)

    tab_details = "//*[@id='root']/div/div/div/div[4]/div[2]/div/div[2]" \
                  "/div/div[2]/div/div[3]/div/div[2]/div[1]/div[2]"


    #receiver
    fld_accountReceiver = "//*[@name='accountNumber']"
    fld_lastname = "//*[@name='lastName']"
    fld_firstname = "//*[@name='firstName']"
    fld_middlename = "//*[@name='middleName']"
    fld_address = "//*[@name='address']"
    fld_area = "//*[@name='city']"
    fld_area_specific = "//*[contains(text(), 'Abra')]"
    fld_barangay = "//*[@name='barangay']"
    fld_barangay_specific = "//*[contains(text(), 'Bangued')]"
    fld_nationality = "//*[@name='nationality']"
    fld_nationality_specific = "//*[contains(text(), 'Afghanistan')]"

    fld_mobile = "//*[@name='mobileNumber']"

    fld_birthday = "//*[@name='birthDate']"
    fld_year = "//*[contains(text(), '" + year + "')]"
    fld_year1 = "//*[contains(text(), '2017')]"
    fld_date = "//*[contains(text(), '" + date + "')]"
    fld_year_specific = "//*[contains(text(), '1989')]"

    fld_gender = "//*[@name='gender']"
    fld_gender_specific = "//*[contains(text(), 'Male')]"

    fld_bank = "//*[@name='bank']"
    fld_bank_specific = "//*[contains(text(), 'BANK OF THE PHILIPPINE ISLANDS')]"
    fld_bankInstapay_specific = "//*[contains(text(), 'CHINABANK')]"

    fld_birthPlace = "//*[@name='birthPlace']"
    fld_ID = "//*[@name='idType']"
    fld_ID_specific = "//div[contains(text(), 'Unified Multi-Purpose ID')]"
    fld_funds = "//*[@name='fundSource']"
    fld_funds_specific = "//*[contains(text(), 'Business')]"
    fld_email = "//*[@name='email']"
    fld_ID_number = "//*[@name='idNumber']"