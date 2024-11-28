import matplotlib.pyplot as plt

# ข้อมูลในตาราง
times = ['75-124', '125-174', '175-224', '225-274', '275-324']
frequencies = [11, 24, 10, 3, 2]

# สร้างกราฟแท่ง
plt.figure(figsize=(8, 6))
plt.bar(times, frequencies, color='red')

# ปรับแต่งกราฟ
plt.title('McDonald\'s Lunch Drive-Through Service Times')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

# แสดงกราฟ
plt.show()