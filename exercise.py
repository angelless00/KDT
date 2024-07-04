
msg="Hello Good Luck"
alpha=set(msg)
save={}
print(alpha)
for m in alpha:
    print(m,msg.count(m))
    save[m]=msg.count(m)
print(save)