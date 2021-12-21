# Bakri Altaif
# altaif.bakri@gmail.com
# 
# Requirements  ******************************
# tlv8==0.9.0
# django-qr-code==3.0.0


import tlv8, base64

def qr_code():

        data = [
            tlv8.Entry(1,'seller-name-arabic'),
            tlv8.Entry(2,'vat-number-registration'),
            tlv8.Entry(3,'date-time-stamp'), # your_date.strftime("%m/%d/%Y, %H:%M:%S")
            tlv8.Entry(4,str('total-cost-with-tax')),
            tlv8.Entry(5,str('vat total')),
        ]

        return base64.b64encode(tlv8.encode(data)).decode('utf-8')