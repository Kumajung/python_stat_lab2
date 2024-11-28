# ข้อมูลที่ไม่ได้จัดกลุ่ม 
# ตัวอย่างที่ 1: ครูระดับ K1 ต้องการบันทึกสีโปรดของนักเรียน 20 คนในชั้นเรียนเพื่อเตรียมสื่อการสอน ผลลัพธ์มีดังนี้

"""
Red, Blue, Purple, Red, Pink, Pink, Yellow, Pink,
Blue, Green, Blue, Pink, Purple, Green, Blue,
Blue, Yellow, Green, Pink, Yellow 
หาผลลัพธ์สามารถแสดงความถี่สําหรับสีโปรดของนักเรียน 20 คนในชั้นเรียน K1
"""

from collections import Counter

# ข้อมูลสีของนักเรียน
colors = ["Red", "Blue", "Purple", "Red", "Pink", "Pink", "Yellow", "Pink",
          "Blue", "Green", "Blue", "Pink", "Purple", "Green", "Blue",
          "Blue", "Yellow", "Green", "Pink", "Yellow"]

# นับจำนวนครั้งที่แต่ละสีปรากฏ
color_counts = Counter(colors)

# คำนวณจำนวนสีทั้งหมด
total_color = sum(color_counts.values())

# แสดงผลในรูปแบบตาราง
print("สี\tจำนวน")
for color, count in color_counts.items():
    print(f"{color}\t{count}")

# แสดงผลรวมจำนวนสีทั้งหมด
print(f"\nจำนวนสีทั้งหมด: {total_color} สี")
