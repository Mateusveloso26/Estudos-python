from datetime import datetime

# data = datetime(2022,4,20,7,30)
# print (data)

# now = datetime.now()
# print(now)

data = datetime.strptime('2022-04-20', '%Y-%m-%d')
data_format = datetime.strftime(data, '%d/%m/%Y')
print (data_format)