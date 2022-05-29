import pandas as pd 
import plotly.express as px 
import datetime
import cashflow
# A=Annualy M=Monthly Q=Quarterly W=Weekly D=Daily

cf = cashflow.CashFlow('Cash flow forecast')

# Balance
balance = 98000

# start_date
saar = 2022
smaaned = 5
sdag = 17

# End date
aar = 2027
maaned = 5
dag = 13 

# saar,smaaned,sdag
#Generate data
cf.add_event('Original balance', balance, datetime.date(saar,smaaned,sdag))

# weekly
cf.generate_series('Food', -100, frequency='W', start=datetime.date(2022, 5, 22), end=datetime.date(aar,maaned,dag))    

# Monthly  
cf.generate_series('Rent', -1500, frequency='M', start=datetime.date(2022, 6, 1), end=datetime.date(aar,maaned,dag))

# Quarterly
cf.generate_series('subscription', -1500, frequency='Q', start=datetime.date(2022, 6, 15), end=datetime.date(aar,maaned,dag))

# One-offs  
cf.add_event('One off payment - auto', -5000, datetime.date(2023, 5, 15)) 

# 
#Show the data
# print(cf.series)
cf.export_to_csv('', 'balance.csv')
