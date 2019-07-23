import datetime

class AmountAndPurpose:
    now = datetime.datetime.now()
    year = str(now.year)
    date = str(now.day)

    # sender info
    fld_amount = "//input[@name='amount']"
    fld_beneficiary = "//input[@name='beneficiaryRelation']"
    fld_purpose = "//div[@name='purpose']"
    fld_purpose_specific = "//div[contains(text(), 'Allowance')]"