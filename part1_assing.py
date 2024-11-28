"""
**โจทย์ใหม่**:  
มีการสำรวจ 20 ครัวเรือนในหมู่บ้านแห่งหนึ่งเกี่ยวกับจำนวนจักรยานที่ครัวเรือนแต่ละหลังมีอยู่ ผลลัพธ์จากการสำรวจคือ:  
`0, 2, 1, 0, 3, 2, 1, 4, 2, 1, 1, 3, 0, 2, 1, 0, 1, 2, 3, 4`  

1. เขียนโปรแกรม Python เพื่อแสดงผลดังนี้:  
   - จำนวนจักรยานที่ครัวเรือนมี และจำนวนครัวเรือนที่มีจักรยานในแต่ละจำนวน  
   - จำนวนครัวเรือนทั้งหมดที่ไม่มีจักรยาน  

2. เพิ่มคำสั่งให้แสดงจำนวนจักรยานทั้งหมดในหมู่บ้าน
"""

from collections import Counter

# ข้อมูลจำนวนจักรยานของแต่ละครัวเรือน
bicycles = [0, 2, 1, 0, 3, 2, 1, 4, 2, 1, 1, 3, 0, 2, 1, 0, 1, 2, 3, 4]

# นับจำนวนครั้งที่แต่ละจำนวนจักรยานปรากฏ
bicycle_counts = Counter(bicycles)

# คำนวณจำนวนครัวเรือนทั้งหมดที่ไม่มีจักรยาน
households_without_bicycles = bicycle_counts[0]

# คำนวณจำนวนจักรยานทั้งหมดในหมู่บ้าน
total_bicycles = sum(num_bikes * count for num_bikes, count in bicycle_counts.items())

# แสดงผลลัพธ์ในรูปแบบตาราง
print("จำนวนจักรยาน\tจำนวนครัวเรือน")
for num_bikes, count in sorted(bicycle_counts.items()):
    print(f"{num_bikes}\t\t{count}")

# แสดงจำนวนครัวเรือนที่ไม่มีจักรยาน
print(f"\nจำนวนครัวเรือนที่ไม่มีจักรยาน: {households_without_bicycles} ครัวเรือน")

# แสดงจำนวนจักรยานทั้งหมดในหมู่บ้าน
print(f"จำนวนจักรยานทั้งหมดในหมู่บ้าน: {total_bicycles} คัน")
