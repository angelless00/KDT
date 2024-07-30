Table={'Seoul':['South Korea','Asia',9655000],
       'Tokyo':['Japan','Asia',14110000],
       'Beijing':['China','Asia',21540000],
       'London':['United Kingdom','Europe',14800000],
       'Berlin':['Germany','Europe',3426000],
       'Mexico City':['Mexico','America',21200000]}

Table=sorted(Table,key=lambda x: x[i][2] for i in Table)

print(Table)








