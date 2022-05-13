import xlwt
from xlwt import Workbook
  
# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')


data = [
  "ABC BANK",
  "Preferred Rewards",
  "P.O. Box 12345",
  "Customer service information",
  "Wilmington, DE 144444",
  "0",
  "ph: (555) 555-1234",
  "TDD/TTY users only call: (800) 555-1234",
  "other: 1-800-555-1234",
  "John Doe",
  "bankingservices.com",
  "Your Adv Plus Banking",
  "Preferred Rewards Platinum",
  "for November 27, 2018 to December 24, 2018",
  "Account summary",
  "Beginning balance on November 27, 2018",
  "$83,576.78",
  "Deposits and other additions",
  "27,450.00",
  "ATM and debit card subtractions",
  "-0.00",
  "Other subtractions",
  "-50,923.23",
  "Checks",
  "-949.00",
  "Service fees",
  "-40.00",
  "Ending balance on December 24, 2018",
  "$59,114.55",
  "See all your benefits and rewards in one place",
  "My Rewards lets you see your Preferred Rewards benefits plus any",
  "Rewards",
  "other rewards and benefits available to you.",
  "Check out My Rewards at bankingservices.com/MyRewards",
  "Page 1 of 6",
  "November 27, 2018 to December 24, 2018",
  "IMPORTANT INFORMATION:",
  "BANK DEPOSIT ACCOUNTS",
  "How to Contact Us - You may call us at the telephone number listed on the front of this statement.",
  "Updating your contact information - We encourage you to keep your contact information up-to-date. This includes address, email",
  "and phone number. If your information has changed, the easiest way to update it is by visiting the Help & Support tab of Online",
  "Banking.",
  "Deposit agreement - When you opened your account, you received a deposit agreement and fee schedule and agreed that your",
  "account would be governed by the terms of these documents, as we may amend them from time to time. These documents are",
  "part of the contract for your deposit account and govern all transactions relating to your account, including all deposits and",
  "withdrawals. Copies of both the deposit agreement and fee schedule which contain the current version of the terms and",
  "conditions of your account relationship may be obtained at our financial centers.",
  "Electronic transfers: In case of errors or questions about your electronic transfers - If you think your statement or receipt is",
  "wrong or you need more information about an electronic transfer (e.g., ATM transactions, direct deposits or withdrawals,",
  "point-of-sale transactions) on the statement or receipt, telephone or write us at the address and number listed on the front of",
  "this statement as soon as you can. We must hear from you no later than 60 days after we sent you the FIRST statement on",
  "which the error or problem appeared.",
  "Tell us your name and account number.",
  "Describe the error or transfer you are unsure about, and explain as clearly as you can why you believe there is an error or",
  "why you need more information.",
  "Tell us the dollar amount of the suspected error.",
  "For consumer accounts used primarily for personal, family or household purposes, we will investigate your complaint and will",
  "correct any error promptly. If we take more than 10 business days (10 calendar days if you are a Massachusetts customer) (20",
  "business days if you are a new customer, for electronic transfers occurring during the first 30 days after the first deposit is",
  "made to your account) to do this, we will provisionally credit your account for the amount you think is in error, so that you will",
  "have use of the money during the time it will take to complete our investigation.",
  "For other accounts, we investigate, and if we find we have made an error, we credit your account at the conclusion of our",
  "investigation.",
  "Reporting other problems - You must examine your statement carefully and promptly. You are in the best position to discover",
  "errors and unauthorized transactions on your account. If you fail to notify us in writing of suspected problems or an unauthorized",
  "transaction within the time period specified in the deposit agreement (which periods are no more than 60 days after we make",
  "the statement available to you and in some cases are 30 days or less), we are not liable to you and you agree to not make a",
  "claim against us, for the problems or unauthorized transactions.",
  "Direct deposits - If you have arranged to have direct deposits made to your account at least once every 60 days from the same",
  "person or company, you may call us to find out if the deposit was made as scheduled. You may also review your activity online or",
  "visit a financial center for information.",
  "Equal Housing Lender",
  "Page 2 of 6",
  "November 27, 2018 to December 24, 2018",
  "Deposits and other additions",
  "Date",
  "Description",
  "Amount",
  "12/03/18",
  "Counter Credit",
  "8,075.00",
  "12/10/18",
  "Counter Credit",
  "9,970.00",
  "12/21/18",
  "PAYPAL",
  "DES:TRANSFER ID:1004561753452 INDN:",
  "CO",
  "1,000.00",
  "12/24/18",
  "Counter Credit",
  "8,405.00",
  "Total deposits and other additions",
  "$27,450.00",
  "Withdrawals and other subtractions",
  "Other subtractions",
  "Date",
  "Description",
  "Amount",
  "11/30/18",
  "Automatic Transfer to SAV 2084 Confirmation# 1313790286",
  "-25.00",
  "12/03/18",
  "Online Banking payment to CRD 8610 Confirmation# 0485104765",
  "-200.00",
  "12/04/18",
  "Customer Withdrawal Image",
  "-12,000.00",
  "12/07/18",
  "TRANSFER ",
  "-3,695.00",
  "12/11/18",
  "CARFAX",
  "DES:BT1210 ID:000000071591462 INDN:",
  "CO ID:1251465303",
  "-399.98",
  "12/13/18",
  "TRANSFER  :J Cars Confirmation# 0472167145",
  "-3,955.00",
  "12/19/18",
  "TRANSFER  :J Cars Confirmation# 0423610629",
  "-13,990.00",
  "12/20/18",
  "SOUTHWEST GAS DES:WEB",
  "ID:1410023972050 INDN:JOHNSON",
  "CO",
  "-28.25",
  "12/21/18",
  "TRANSFER  :J Cars Confirmation# 1642822709",
  "-16,630.00",
  "Total other subtractions",
  "-$50,923.23",
  "Page 3 of 6",
  " ",
  "November 27, 2018 to December 24, 2018",
  "Checks",
  "Date",
  "Check #",
  "Amount",
  "Date",
  "Check #",
  "Amount",
  "12/18/18",
  "1148",
  "-900.00",
  "11/28/18",
  "1521'",
  "-49.00",
  "Total checks",
  "-$949.00",
  "Total # of checks",
  "2",
  "There is a gap in sequential check numbers",
  "Service fees",
  "Date",
  "Transaction description",
  "Amount",
  "12/10/18",
  "External transfer fee - Next Day - 12/07/2018",
  "-10.00",
  "12/14/18",
  "External transfer fee - Next Day - 12/13/2018",
  "-10.00",
  "12/20/18",
  "External transfer fee - Next Day - 12/19/2018",
  "-10.00",
  "12/24/18",
  "External transfer fee - Next Day - 12/21/2018",
  "-10.00",
  "Total service fees",
  "-$40.00",
  "Note your Ending Balance already reflects the subtraction of Service Fees.",
  "Page 4 of 6",
  "November 27, 2018 to December 24, 2018",
  "Check images",
  "Check number: 1148",
  "Amount: $900.00",
  "Check number: 1521",
  "Amount: $49.00",
  "THE NATERE CONSFIVANCY",
  "RENEO",
  "TRA1-S-001439/001439 S1 ET M1 -000001",
  "000005",
  "Conservancy The Nature",
  "1148",
  "700 N UCCARRAN BLVD",
  "CARNEL Ph BAY CA% adrist",
  "89451",
  "1521",
  "e.e Wex ilst",
  "DATE 12/12/18",
  "24-72/1224 -",
  "Data 11/27/18",
  "Cornell Bay, CA96140",
  "817Z",
  "Safe Auto Transport",
  "900-",
  "Paylothe",
  "Orderof",
  "CITICARDS",
  "$49.00",
  "ORDER DE",
  "Nine Hundred & 00/100",
  "DELLARS @ and",
  "*****FORTYNINE AND 00/100*****",
  "206-C007495681 180",
  "122400724",
  "SCARS 07 GL450",
  "'06 EDIARE",
  "LAI",
  "Memo 4100390077958227 815830260521",
  "Authorizedby your Depositor 11/27/18",
  "Page 5 of 6",
  "This page intentionally left blank",
  "Page 6 of 6"
]


page = []
temp = []
email = []
phone = []
date = []

minimum = 0
maximum = 0

withdraw = []
deposit = []
for i in data:
    try:
        if("." in i):
            val = float(i.replace(",","").replace("$",""))
            if(val < 0):
                withdraw.append(val)
            else:
                deposit.append(val)
            if(minimum > val):
                minimum = val
            if(maximum < val):
                maximum = val
    except:
        pass
    if("-" in i):
        try:
            if(":" in i):
                t = True
                for j in i[i.index(":")+1:].strip():
                    if(j not in ['0','1','2','3','4','5','6','7','8','9','(',')','-',' ']):
                        t = False
                        break
                if(t):
                    phone.append(i[i.index(":")+1:].strip())
        except:
            pass
    if(i.count("/") == 2):
        date.append(i[i.index("/")-2:i.index("/")+8])
    if("Page" in i):
        page.append(temp)
        temp = []
    else:
        temp.append(i)

print(date)
print(phone)
print(minimum,maximum)
print(withdraw,deposit)

sheet1.write(0, 0, 'Key')
sheet1.write(0, 1, 'Value')

sheet1.write(1, 0, 'date')
sheet1.write(1, 1, str(date).replace("[","").replace("]",""))

sheet1.write(2, 0, 'phone')
sheet1.write(2, 1, str(phone).replace("[","").replace("]",""))

sheet1.write(3, 0, 'minimum')
sheet1.write(3, 1, minimum)

sheet1.write(4, 0, 'maximum')
sheet1.write(4, 1, maximum)

sheet1.write(5, 0, 'Withdraw')
sheet1.write(5, 1, str(withdraw).replace("[","").replace("]",""))

sheet1.write(6, 0, 'Deposit')
sheet1.write(6, 1, str(deposit).replace("[","").replace("]",""))

wb.save('output.xls')
