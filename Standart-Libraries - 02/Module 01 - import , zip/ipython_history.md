# Importing Libraries
                                                    import math
math.pi
3.141592653589793
math.e
2.718281828459045
math.cos(math.pi)
-1.0
math.log(math.e)
1.0
math.floor(-15.5)
-16
math.ceil(-15.3)
-15

----------------------------------------------------------------


                                                    import random

random.random()
0.038473718960679304

random.random()
0.7484803052293665

random.random()*100
66.7605890376691

random.randint(1,10)
7
random.choice(["hi","yes","no"])
'hi'

suits = ("hearts","diamond","clubs","spades")

values = range(1,14)
list(values)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

cards = []


type(cards)
list

type(suits)
tuple


for s in suits:
    for v in values:
        cards.append("{0} of {1}".format(v,s) )

cards
['1 of hearts', '2 of hearts', '3 of hearts', '4 of hearts', '5 of hearts', '6 of hearts', '7 of hearts', '8 of hearts', '9 of hearts', '10 of hearts', '11 of hearts', '12 of hearts', '13 of hearts', '1 of diamond', '2 of diamond', '3 of diamond', '4 of diamond', '5 of diamond', '6 of diamond', '7 of diamond', '8 of diamond', '9 of diamond', '10 of diamond', '11 of diamond', '12 of diamond', '13 of diamond', '1 of clubs', '2 of clubs', '3 of clubs', '4 of clubs', '5 of clubs', '6 of clubs', '7 of clubs', '8 of clubs', '9 of clubs', '10 of clubs', '11 of clubs', '12 of clubs', '13 of clubs', '1 of spades', '2 of spades', '3 of spades', '4 of spades', '5 of spades', '6 of spades', '7 of spades', '8 of spades', '9 of spades', '10 of spades', '11 of spades', '12 of spades', '13 of spades']

random.choice(cards)
'8 of hearts'

----------------------------------------------------------------


random.shuffle(cards)

cards
['4 of clubs',  '4 of spades',  '5 of spades',  '10 of spades',  '6 of clubs',  '4 of diamond',  '3 of spades',  '2 of diamond',  '10 of diamond',  '8 of clubs',  '6 of hearts',  '3 of clubs',  '9 of diamond',  '8 of hearts',  '12 of hearts',  '5 of clubs',  '9 of hearts',  '13 of spades',  '5 of diamond',  '8 of spades',  '10 of hearts',  '1 of hearts',  '1 of clubs',  '3 of hearts',  '6 of spades',  '12 of clubs',  '12 of diamond',  '11 of clubs',  '11 of hearts',  '7 of hearts',  '13 of clubs',  '7 of spades',  '7 of diamond',  '8 of diamond',  '2 of hearts',  '13 of hearts',  '1 of spades',  '13 of diamond',  '11 of spades',  '6 of diamond',  '2 of spades',  '4 of hearts',  '5 of hearts',  '12 of spades',  '9 of spades',  '7 of clubs',  '11 of diamond',  '9 of clubs',  '2 of clubs',  '10 of clubs',  '1 of diamond',  '3 of diamond']

random.choice(cards)
'10 of clubs'

cards.sort()

cards
['1 of clubs',  '1 of diamond',  '1 of hearts',  '1 of spades',  '10 of clubs',  '10 of diamond',  '10 of hearts',  '10 of spades',  '11 of clubs',  '11 of diamond',  '11 of hearts',  '11 of spades',  '12 of clubs',  '12 of diamond',  '12 of hearts',  '12 of spades',  '13 of clubs',  '13 of diamond',  '13 of hearts',  '13 of spades',  '2 of clubs',  '2 of diamond',  '2 of hearts',  '2 of spades',  '3 of clubs',  '3 of diamond',  '3 of hearts',  '3 of spades',  '4 of clubs',  '4 of diamond',  '4 of hearts',  '4 of spades',  '5 of clubs',  '5 of diamond',  '5 of hearts',  '5 of spades',  '6 of clubs',  '6 of diamond',  '6 of hearts',  '6 of spades',  '7 of clubs',  '7 of diamond',  '7 of hearts',  '7 of spades',  '8 of clubs',  '8 of diamond',  '8 of hearts',  '8 of spades',  '9 of clubs',  '9 of diamond',  '9 of hearts',  '9 of spades']


----------------------------------------------------------------


                                                    import itertools as iter
                                                    import math as mat
mat.random()
mat.pi
3.141592653589793
for num in ter.chain([1,2,3],[4,6,5]):
    print(num)
for num in iter.chain([1,2,3],[4,6,5]):
    print(num)
for (a,b,c) in iter.combinations( ("peanut", "jelly", "mayo", "beetroot"), 3):
    print("How about a nice {0},{1}, and {2} sandwich".format(a,b,c) )
                                                    import time
time.localtime
<function time.localtime>
time.localtime()
time.struct_time(tm_year=2020, tm_mon=2, tm_mday=25, tm_hour=12, tm_min=38, tm_sec=1, tm_wday=1, tm_yday=56, tm_isdst=0)
time.gmtime()
time.struct_time(tm_year=2020, tm_mon=2, tm_mday=25, tm_hour=12, tm_min=38, tm_sec=12, tm_wday=1, tm_yday=56, tm_isdst=0)
now = time.strftime("%H:%M:%S %p - %A, %B %d %Y")
now
'12:38:59 PM - Tuesday, February 25 2020'
now = time.strftime("%H:%M:%S %p - %A, %B %d %Y", time.gmtime() )
now
'12:39:43 PM - Tuesday, February 25 2020'
time.time()
1582634426.6850286
clear


----------------------------------------------------------------


                                                    import datetime

now
'12:39:43 PM - Tuesday, February 25 2020'
datetime.datetime.strptime(now, "%H:%M:%S %p - %A, %B %d %Y")
datetime.datetime(2020, 2, 25, 12, 39, 43)

from datetime import datetime
datetime.strptime(now, "%H:%M:%S %p - %A, %B %d %Y")
datetime.datetime(2020, 2, 25, 12, 39, 43)
                                                    import time
time
<module 'time' (built-in)>
from datetime import time
time
datetime.time
my_list = [1,2,3,4]
my_list = "String"
                                                    import time
from datetime import time as dt_time
time:dt_time
now = datetime.now()
now
datetime.datetime(2020, 2, 25, 12, 45, 59, 667284)
clear


----------------------------------------------------------------


                                                    import gzip
                                                    import bz2
                                                    import zipfile

from zipfile import ZipFile
with ZipFile('info.zip') as files:
    print(files.namelist())
with ZipFile('info.zip') as files:
    print(files.namelist())
    files.extractall()
clear

help
Type help() for interactive help, or help(object) for help about object.
help()

magic_hist()
history

%hist -o -f ipython_history.md


# Download history from IPython