import pandas as pd
data = {
        'Supply of cakes':[100,200,500,700],
        'Expired packets':[40,60,100,150]
        }
var = pd.DataFrame(data,index=["day1","day2","day3","day4"])
print(var)
