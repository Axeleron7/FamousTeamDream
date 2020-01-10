model_1 = "Квадрокоптер Ryze Tello Black-White,98 мм,41 мм,1100 мА*ч,13 минут,10мин,2 699"
model_2 = "Квадрокоптер DJI Mavic Mini Fly More Combo,290 мм,55 мм,2400 мА*ч,30 минут,15 470"
model_3 = "Квадрокоптер DJI Mavic Mini,290 мм,55 мм,2400 мА*ч,24 минуты,12 370"
model_4 = "Квадрокоптер DJI Mavic 2 Pro,320 мм,84 мм,3850 мА*ч,31 минута,42 750"
model_5 = "Квадрокоптер Hubsan X4 H107C,160 мм,35 мм,520 мА*ч,7 минут,42 750,1 999"


model_1 = list(model_1)
model_2 = list(model_2)
model_3 = list(model_3)
model_4 = list(model_4)
model_5 = list(model_5)

#d ={
#    key:value,
#}

d = {
    1: 'Квадрокоптер Ryze Tello Black-White',
    '98 мм' : '41 мм',
    '1100 мА*ч' : '13 минут',
    '2 699' : 1

}

listForDict = [['a', 1], ['b', 2], ['c', 3]]
print(type(listForDict))

dic = dict(listForDict)

print(dic, type(dic))

