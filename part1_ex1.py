# ตัวอย่างที่ : มีการสํารวจครัวเรือน 15 ครัวเรือนว่ามีรถยนต์กี่คันในบ้าน ผลลัพธ์มีดังนี้
# 0,1,2,3,4,0,1,1,2,2,4,3,1,1,1 ผลลัพธ์สามารถแสดงได้ด้วยภาษา python

from collections import Counter

# ข้อมูลจำนวนรถของแต่ละครัวเรือน
cars = [0, 1, 2, 3, 4, 0, 1, 1, 2, 2, 4, 3, 1, 1, 1]

# นับจำนวนครั้งที่แต่ละจำนวนรถปรากฏ
car_counts = Counter(cars)

# คำนวณจำนวนรถทั้งหมด
total_cars = sum(car_counts.values())

# แสดงผลลัพธ์ในรูปแบบตาราง
print("จำนวนรถ\tจำนวนครัวเรือน")
for num_cars, count in car_counts.items():
    print(f"{num_cars}\t\t{count}")

# แสดงผลรวมจำนวนรถทั้งหมด
print(f"\nจำนวนรถทั้งหมด: {total_cars} คัน")