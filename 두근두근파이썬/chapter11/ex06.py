import matplotlib.pyplot as plt

x = []
y = []
route = "C:/Users/kdy03/OneDrive/바탕 화면/파이썬/chapter11/ex06.txt"  # 파일 경로
infile = open(route,"r")
F = infile.readlines()
infile.close()

for i in F:
    i.replace("\n","")
    line = i.split(" ")
    x.append(line[0])
    y.append(int(line[1]))
plt.bar(x,y,label='score')
plt.legend(loc='best', fontsize=10, frameon=True, shadow=True)
plt.ylabel('scores')

font_title = {
    'fontsize': 16,
    'fontweight': 'bold'
}
plt.title('Student Score',fontdict=font_title)

plt.show()
