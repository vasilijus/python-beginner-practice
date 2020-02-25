import csv
with open('users.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'email', 'name'])
    writer.writerow([1,'vasiliokas@gmail.com', 'Sergio'])
    writer.writerow([2,'mail@mail.com', 'Test'])
ls
cat users.csv
import os
os.getenv('USER')
'sergio'
os.path.abspath('.')
'/home/sergio/code/Coding Practices/Python/CloudGuru/Standart-Libraries - 02'
clear
import sys
sys.argv
['/home/sergio/.local/bin/ipython']
sys.platform
'linux'
sys.version
'3.7.3 (default, Oct  7 2019, 12:56:13) \n[GCC 8.3.0]'
clear
import re
regular expression
# test patterns
if re.search('lemon', 'lemonade')
if re.search('lemon', 'lemonade'): print("lemon is inside string")
# OR
if "lemon" in "lemonade": print("lemon string is insided")
# Or use . do say any character
if re.search('.ang' , 'danger'):print("Found")
# use \w to match any word
if re.search(".ang\w", "dangerous"): print("Match!")
# use parentises to define groups
angs = re.search( "(.ang)", "dangerous")
angs.groups()
('dang',)
#find vowels
vowels_re = "[aeiou]"
re.findall(vowels_re, "dangerous")
['a', 'e', 'o', 'u']
clear
# more of the standard library
import turtle
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(40).rt(90).fd(50).lt(90).fd(50)
turtle.clear()
def do_square(size):
    for i in range(4):
        turtle.fd(size)
        turtle.lt(90)
do_square(100)
do_square(200)
turlte.clear()
turtle.clear()
# make turtle do a triangle
def do_triangle(size):
    for i in range(3):
        turtle.fd(size)
        turtle.lt(120)
do_triagnle(100)
do_triangle(100)
turtle.color('red')
do_triangle(200)
# make polygon
def do_pol(size, sides):
    angle = 360 / sides
    for i in range(sides):
        turtle.fd(size)
        turtle.lt(angle)
turtle.clear()
do_pol(50, 10)
do_pol(50, 7)
do_pol(50, 4)
%hist -o -f iphyton_history_module_2.md
