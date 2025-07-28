import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.rcParams.update({
    'font.family': ['Arial', 'SimHei'],           # 字体优先使用 Arial，找不到时用 SimHei（支持中文）
    'font.size': 20,                              # 基础字体大小
    'axes.labelsize': 20,                         # 坐标轴标签字体大小
    'axes.titlesize': 20,                         # 坐标轴标题字体大小
    'xtick.labelsize': 18,                        # x 轴刻度标签字体大小
    'ytick.labelsize': 18,                        # y 轴刻度标签字体大小
    'legend.fontsize': 18,                        # 图例字体大小
    'mathtext.fontset': 'custom',                 # 使用自定义数学字体配置
    'mathtext.rm': 'Arial',                       # 数学文本正常字体用 Arial
    'mathtext.it': 'Arial:italic',                # 数学文本斜体用 Arial Italic
    'mathtext.bf': 'Arial:bold',                   # 数学文本粗体用 Arial Bold
    'xtick.direction': 'in',                      # x 轴刻度朝内
    'ytick.direction': 'in',                      # y 轴刻度朝内
})

plt.figure()                                      # 新建图表窗口
plt.title("示例标题 - 中文 + English")              # 图表标题，含中文和英文
plt.xlabel("X 轴标签")                            # x 轴标签，中文
plt.ylabel("Y 轴标签")                            # y 轴标签，中文
plt.plot([1, 2, 3], [4, 5, 6], label="测试曲线")    # 画一条曲线，图例含中文
plt.legend()                                      # 显示图例
plt.show()                                        # 展示图形窗口
