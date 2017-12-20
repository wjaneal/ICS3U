###
This program is created for stock buyers to remind them about the price of the stock.
Within this program, I set up a data reader...later then, I created an e-mail server for sending emails
###
from pandas_datareader import data as pdr    	# import a module - "pandas_datareader"
import pandas as pd 			     	# import a module - "panda"
import smtplib				     	# import module "smtplib"
server = smtplib.SMTP('SMTP.gmail.com', 587) 	# set up a gmail server
server.starttls()				# give a command let the server stay activated
server.login("haha21596@gmail.com", "12345678ABC") #assign an account to the server and give the login information

import fix_yahoo_finance as yf 			# import data from the yahoo finance

yf.pdr_override()

data = pdr.get_data_yahoo("AAPL", start="2017-12-16", end="2017-12-17") #set a certain range of data to analyze

dataFrame = pd.DataFrame(data) #create a variable called dataFrame

print("\n")
dataNew = str(dataFrame).split("\n")

print(dataNew)

today=dataNew[3].split("  ") #convert the raw data to strings
yesterday=dataNew[2].split("  ") # convert the raw data to strings
print(today)			#display the data
print(yesterday)		#display the data

if float(today[4])-float(yesterday[4])>=1: #give a condition that if the subtraction is bigger than 1
    print("happy.") 				#tell the user that the market is nice that day
    msg = "You may sell it!"			# write down the message 
    server.sendmail("daibaiyu1122@gmail.com", "daibaoyu1122@gmail.com", msg) #give the receiver account
    server.quit() #down and quit
else:
    print("sad") #tell the user that the market is bad that day
    msg = "You may buy more!"# write down the message 
    server.sendmail("haha21596@gmail.com", "daibaoyu1122@icloud.com", msg)#give the receiver account
    server.quit()
