import matplotlib.pyplot as plt
from collections import Counter

# ข้อมูลสีของนักเรียน
colors = ["Red", "Blue", "Purple", "Red", "Pink", "Pink", "Yellow", "Pink",
          "Blue", "Green", "Blue", "Pink", "Purple", "Green", "Blue",
          "Blue", "Yellow", "Green", "Pink", "Yellow"]
color_counts = Counter(colors)

# ตั้งค่าสี (เลือกสีตามความเหมาะสม)
custom_colors = ["#FF9999", "#66B2FF", "#CC99FF", "#FFCC99", "#FFFF99", "#99FF99"]

# สร้างกราฟวงกลม
plt.pie(
    color_counts.values(),
    labels=color_counts.keys(),
    autopct='%1.1f%%',
    colors=custom_colors
)
plt.title("Students' favorite colors")
plt.show()
