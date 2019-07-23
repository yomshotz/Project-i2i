import datetime

class Sender:
    now = datetime.datetime.now()
    year = str(now.year)
    date = str(now.day)


    # sender info

    fld_accountSender = "//input[@name='accountNumber']"
    fld_lastname = "//input[@name='lastName']"
    fld_firstname = "//input[@name='firstName']"
    fld_middlename = "//input[@name='middleName']"
    fld_address = "//input[@name='address']"
    fld_area = "//div[@name='city']"
    fld_area_specific = "//div[contains(text(), 'Abra')]"
    fld_barangay = "//div[@name='barangay']"
    fld_barangay_specific = "//div[contains(text(), 'Bangued')]"
    fld_nationality = "//div[@name='nationality']"
    fld_nationality_specific = "//div[contains(text(), 'Afghanistan')]"

    fld_mobile = "//input[@name='mobileNumber']"

    fld_birthday = "//input[@name='birthDate']"
    fld_year = "//div[contains(text(), '" + year + "')]"
    fld_year1 = "//span[contains(text(), '2017')]"
    fld_date = "//span[contains(text(), '" + date + "')]"
    fld_year_specific = "//*[contains(text(), '1989')]"

    fld_gender = "//div[@name='gender']"
    fld_gender_specific = "//div[contains(text(), 'Male')]"

    fld_birthPlace = "//*[@name='birthPlace']"
    fld_ID = "//div[@name='idType']"
    fld_ID_specific = "//div[contains(text(), 'Unified Multi-Purpose ID')]"
    fld_funds = "//div[@name='fundSource']"
    fld_funds_specific = "//div[contains(text(), 'Business')]"
    fld_email = "//div[@name='email']"
    fld_ID_number = "//input[@name='idNumber']"
