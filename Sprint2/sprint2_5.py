import re


def max_population(data):
    highest_pop=['',0]
    for i in range(1,len(data)):
        s=re.search(r'^[0-9]*,(\S+),.$', data[i]).group(1)
        new_pop=int(s.split(sep=',')[1])
        if int(highest_pop[1])<new_pop:
            highest_pop[0]=s.split(sep=',')[0]
            highest_pop[1]=int(s.split(sep=',')[1])
    return tuple(highest_pop)


data = ["id,name,poppulation,is_capital",
        "3024,eu_kyiv,24834,y",
        "3025,eu_volynia,20231,n",
        "3026,eu_galych,23745,n",
        "4892,me_medina,18038,n",
        "4401,af_cairo,18946,y",
        "4700,me_tabriz,13421,n",
        "4899,me_bagdad,22723,y",
        "6600,af_zulu,09720,n"]
print(max_population(data))
