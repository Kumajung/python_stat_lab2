import numpy as np

# กำหนดชุดข้อมูล
data = np.array([0.2, 0.7, 0.1, 0.3, 0.5, 0.8, 0.9, 0.1, 0.9])

# เรียงลำดับข้อมูล
sorted_data = np.sort(data)
print("ข้อมูลที่เรียงลำดับแล้ว:", sorted_data)

# หาค่าโมดาล (ค่าที่เกิดขึ้นบ่อยที่สุด)
unique, counts = np.unique(data, return_counts=True)
max_count = np.max(counts)
modes = unique[counts == max_count]
print("ค่าฐานนิยม:", modes)