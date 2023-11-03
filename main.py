
# * รูปแบบ ที่ 1 การเรียกชื่อไฟล์
import example_1

# * ตั้งชื่อใหม่ 
import example_1 as myfunc

# * เรียกใช้งาน แค่บ้างส่วน เช่น ฟังชัน
# * หรือ เรียกใช้ทุกฟังชัน ที่อยู่ใน module ให้แทน * ชื่อฟังชัน 
# * from example_1 import *
from example_1 import test2,test3

example_1.test1()
print("--------")
myfunc.test3()
print("--------")
test2()
print("--------")
test3()
print("--------")