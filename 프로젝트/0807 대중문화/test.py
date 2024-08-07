import matplotlib.pyplot as plt
import koreanize_matplotlib 

plt.figure(figsize=(10,10))
fig,ax_1=plt.subplots()
ax_1.bar([1,2,3,4,5],[20,23,13,43,53])
ax_1.set_yticks([0,50,100])
ax_1.set_ylabel('왼쪽')
ax_2=ax_1.twinx()
ax_2.plot([1,2,3,4,5],[100,300,245,461,424])
ax_2.set_yticks([200,400,600,700])
ax_2.set_ylabel('오른쪽')
ax_2
plt.show()



