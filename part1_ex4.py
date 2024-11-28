import matplotlib.pyplot as plt

# ข้อมูล
times = ['75-124', '125-174', '175-224', '225-274', '275-324']
frequencies = [11, 24, 10, 3, 2]

# คำนวณจุดกึ่งกลาง (Midpoints) ของช่วงเวลา
midpoints = [(75 + 124) / 2, (125 + 174) / 2, (175 + 224) / 2, (225 + 274) / 2, (275 + 324) / 2]

# เพิ่มจุดเริ่มต้นและจุดสิ้นสุดให้สมบูรณ์ (สำหรับเส้นปิด)
midpoints = [75] + midpoints + [325]
frequencies = [0] + frequencies + [0]

# วาด Frequency Polygon
plt.figure(figsize=(8, 6))
plt.plot(midpoints, frequencies, marker='o', color='blue', label='Frequency Polygon')
plt.fill_between(midpoints, frequencies, color='skyblue', alpha=0.2)  # เพิ่มพื้นที่ใต้กราฟเพื่อความสวยงาม

# ปรับแต่งกราฟ
plt.title('Frequency Polygon')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.xticks(midpoints, rotation=45)
plt.legend()
plt.grid()

# แสดงกราฟ
plt.show()
