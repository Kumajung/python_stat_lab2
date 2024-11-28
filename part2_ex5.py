# ตัวอย่าง: กําหนดตารางความถี่
"""
Ages   Number of Students (Frequency)
17            1
18            4
19            1
20            2
21            1
"""
import numpy as np
from scipy.stats import mode

# ข้อมูลอายุ
ages = np.array([17, 18, 18, 18, 18, 19, 20, 20, 21])

# หาฐานนิยม
mode_result = mode(ages)

# ตรวจสอบผลลัพธ์และแสดงค่า
print(mode_result)  # ลองพิมพ์ mode_result ออกมาดู

# ถ้า mode_result เป็นสเกลาร์
if np.isscalar(mode_result.mode):
    print(f"ฐานนิยมคือ: {mode_result.mode}")
else:
    # ถ้า mode_result เป็นอาร์เรย์
    print(f"ฐานนิยมคือ: {mode_result.mode[0]}")
    print(f"จำนวนครั้งที่เกิดขึ้น: {mode_result.count[0]}")