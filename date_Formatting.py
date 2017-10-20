from datetime import datetime

apple="faisal"
banana="afzal"
carrot="want"
fruitdict ={}
for i in ('apple', 'banana', 'carrot'):
    fruitdict[i] = locals()[i]
print(fruitdict)
