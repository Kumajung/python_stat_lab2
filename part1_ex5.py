# ตัวอย่างกราฟวงกลม ข้อมูลจากตัวอย่างที่ 1
import matplotlib.pyplot as plt
from collections import Counter
# ข้อมูลสีของนักเรียน
colors = colors = ["Red", "Blue", "Purple", "Red", "Pink", "Pink", "Yellow", "Pink",
          "Blue", "Green", "Blue", "Pink", "Purple", "Green", "Blue",
          "Blue", "Yellow", "Green", "Pink", "Yellow"]
color_counts = Counter(colors)

# สร้างกราฟวงกลม
plt.pie(color_counts.values(), labels=color_counts.keys(), autopct='%1.1f%%')
plt.title("Students' favorite colors")
plt.show()