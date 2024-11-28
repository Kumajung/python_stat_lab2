# ตัวอย่าง: ชุดข้อมูลที่กําหนด 13, 19, 17, 11, 15, 14, 20
import numpy as np

# ชุดข้อมูล
data = np.array([13, 19, 17, 11, 15, 14, 20])

# หาค่ามัธยฐาน
median_value = np.median(data)
position_value = (len(data)+1)/2

print("ตําแหน่งสําหรับค่ามัธยฐาน: ",position_value)
print("ค่ามัธยฐาน:", median_value)