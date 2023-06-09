
# from datetime import datetime
#the date time library
from datetime import datetime
now = datetime.now()
print(now) 

#Extracting information
from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

#Hot date
from datetime import datetime
now = datetime.now()
print('%02d/%02d/%04d'%(now.month,now.day,now.year))

#pretty time
from datetime import datetime
now = datetime.now()

print ('%02d:%02d:%04d' % (now.hour, now.minute, now.second))

#Grand Finale
from datetime import datetime
now = datetime.now()

print ('%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
