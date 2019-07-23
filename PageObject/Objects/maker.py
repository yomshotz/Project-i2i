import datetime

class Maker:

    now = datetime.datetime.now()
    year = str(now.year)
    date = str(now.day)

    tab_wallet = "//div[contains(text(), 'Wallet')]"
    tab_nrps = "//div[contains(text(), 'NRPS')]"

    panel_sendMoney = "//span[contains(text(), 'Send Money')]"

    panel_wallet = "/html/body/div[5]/div/div/div/div/div/div/div[4]/div/span/div/div"
    tab_details = "//p[contains(text(), 'DETAILS AND PHOTO')]"

    panel_instapay = "//div[contains(text(), 'InstaPay')]"
    panel_pesonet = "//div[contains(text(), 'PesoNet')]"
