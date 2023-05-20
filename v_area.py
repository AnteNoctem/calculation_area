%matplotlib
import math
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import pandas as pd

tn = math.tan(22.5 * math.pi / 180)
cs = math.cos(22.5 * math.pi / 180)
sn = math.sin(22.5 * math.pi / 180)

try:
    aproxim = str(input('Выберите метод постороения. Введите цифру (1, 2 или 3)\n\
    1.Классический (востмиугольник вписан в фигуру)\n\
    2.Дополнительный (восьмиугольник описывает фигуру)\n\
    3.16-тиугольник\n'))
except:
    aproxim = '1'

#Vehicle size
Vlenght = 5
Vwidth = 5

#Emergency zone
Efront = 15
Eback = 15
Esides = 20

#Alert zone
Afront = 50
Aback = 40
Asides = 30

#Vehicle
Vpoint_1 = [Vwidth/2, Vlenght/2]
Vpoint_2 = [Vwidth/2, -Vlenght/2]
Vpoint_3 = [-Vwidth/2, -Vlenght/2]
Vpoint_4 = [-Vwidth/2, Vlenght/2]

#Zones coordinates
E_zone_x_fr = Efront + Vpoint_1[0]
E_zone_x_sd = Esides + Vpoint_1[0]
E_zone_y_fr = Efront + Vpoint_1[1]
E_zone_y_bk = Eback + Vpoint_1[1]

A_zone_x_fr = Afront + Vpoint_1[0]
A_zone_x_sd = Asides + Vpoint_1[0]
A_zone_y_fr = Afront + Vpoint_1[1]
A_zone_y_bk = Aback + Vpoint_1[1]

if aproxim == '1':
    #Emergency zone coordinates
    Emergency = [[round(tn*E_zone_x_fr, 2), round(cs*E_zone_y_fr, 2)],
                 [round(cs*E_zone_x_sd, 2), round(sn*E_zone_y_fr, 2)],
                 [round(cs*E_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(tn*E_zone_x_fr, 2), round(-cs*E_zone_y_bk, 2)],
                 [round(-tn*E_zone_x_fr, 2), round(-cs*E_zone_y_bk, 2)], 
                 [round(-cs*E_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(-cs*E_zone_x_sd, 2), round(sn*E_zone_y_fr, 2)], 
                 [round(-tn*E_zone_x_fr, 2), round(cs*E_zone_y_fr, 2)],
                 [round(tn*E_zone_x_fr, 2), round(cs*E_zone_y_fr, 2)]]

    #Alert zone coordinates
    Asector_1 = [[round(tn*A_zone_x_fr, 2), round(cs*A_zone_y_fr, 2)], 
                 [round(tn*E_zone_x_fr, 2), round(cs*E_zone_y_fr, 2)],
                 [round(-tn*E_zone_x_fr, 2), round(cs*E_zone_y_fr, 2)],
                 [round(-tn*A_zone_x_fr, 2), round(cs*A_zone_y_fr, 2)],
                 [round(tn*A_zone_x_fr, 2), round(cs*A_zone_y_fr, 2)]]
    Asector_2 = [[round(cs*A_zone_x_sd, 2), round(sn*A_zone_y_fr, 2)],
                 [round(cs*E_zone_x_sd, 2), round(sn*E_zone_y_fr, 2)],
                 [round(tn*E_zone_x_fr, 2), round(cs*E_zone_y_fr, 2)],
                 [round(tn*A_zone_x_fr, 2), round(cs*A_zone_y_fr, 2)],
                 [round(cs*A_zone_x_sd, 2), round(sn*A_zone_y_fr, 2)]]
    Asector_3 = [[round(cs*A_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(cs*E_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(cs*E_zone_x_sd, 2), round(sn*E_zone_y_fr, 2)],
                 [round(cs*A_zone_x_sd, 2), round(sn*A_zone_y_fr, 2)],
                 [round(cs*A_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)]]
    Asector_4 = [[round(tn*A_zone_x_fr, 2), round(-cs*A_zone_y_bk, 2)],
                 [round(tn*E_zone_x_fr, 2), round(-cs*E_zone_y_bk, 2)],
                 [round(cs*E_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(cs*A_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(tn*A_zone_x_fr, 2), round(-cs*A_zone_y_bk, 2)]]
    Asector_5 = [[round(-tn*A_zone_x_fr, 2), round(-cs*E_zone_y_bk, 2)],
                 [round(-tn*E_zone_x_fr, 2), round(-cs*A_zone_y_bk, 2)],
                 [round(tn*E_zone_x_fr, 2), round(-cs*A_zone_y_bk, 2)],
                 [round(tn*A_zone_x_fr, 2), round(-cs*E_zone_y_bk, 2)],
                 [round(-tn*A_zone_x_fr, 2), round(-cs*E_zone_y_bk, 2)]]
    Asector_6 = [[round(-cs*A_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(-cs*E_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(-tn*E_zone_x_fr, 2), round(-cs*E_zone_y_bk, 2)],
                 [round(-tn*A_zone_x_fr, 2), round(-cs*A_zone_y_bk, 2)],
                 [round(-cs*A_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)]]
    Asector_7 = [[round(-cs*A_zone_x_sd, 2), round(sn*A_zone_y_fr, 2)],
                 [round(-cs*E_zone_x_sd, 2), round(sn*E_zone_y_fr, 2)],
                 [round(-cs*E_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(-cs*A_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(-cs*A_zone_x_sd, 2), round(sn*A_zone_y_fr, 2)]]
    Asector_8 = [[round(-tn*A_zone_x_fr, 2), round(cs*A_zone_y_fr, 2)],
                 [round(-tn*E_zone_x_fr, 2), round(cs*E_zone_y_fr, 2)],
                 [round(-cs*E_zone_x_sd, 2), round(sn*E_zone_y_fr, 2)],
                 [round(-cs*A_zone_x_sd, 2), round(sn*A_zone_y_fr, 2)],
                 [round(-tn*A_zone_x_fr, 2), round(cs*A_zone_y_fr, 2)]]
    
if aproxim == '2':
    Emergency = [[round(E_zone_x_sd, 2), round(tn*E_zone_x_sd, 2)],
                 [round(E_zone_x_sd, 2), round(-tn*E_zone_x_sd, 2)],
                 [round(tn*E_zone_y_bk, 2), round(-E_zone_y_bk, 2)],
                 [round(-tn*E_zone_y_bk, 2), round(-E_zone_y_bk, 2)],
                 [round(-E_zone_x_sd, 2), round(-tn*E_zone_x_sd, 2)],
                 [round(-E_zone_x_sd, 2), round(tn*E_zone_x_sd, 2)],
                 [round(-tn*E_zone_y_fr, 2), round(E_zone_y_fr, 2)],
                 [round(tn*E_zone_y_fr, 2), round(E_zone_y_fr, 2)],
                 [round(E_zone_x_sd, 2), round(tn*E_zone_x_sd, 2)]]
    
    Asector_1 = [[round(E_zone_x_sd, 2), round(tn*E_zone_x_sd, 2)],
                 [round(E_zone_x_sd, 2), round(-tn*E_zone_x_sd, 2)],
                 [round(A_zone_x_sd, 2), round(-tn*A_zone_x_sd, 2)],
                 [round(A_zone_x_sd, 2), round(tn*A_zone_x_sd, 2)],
                 [round(E_zone_x_sd, 2), round(tn*E_zone_x_sd, 2)]]    
    Asector_2 = [[round(E_zone_x_sd, 2), round(-tn*E_zone_x_sd, 2)],
                 [round(A_zone_x_sd, 2), round(-tn*A_zone_x_sd, 2)],
                 [round(tn*A_zone_y_bk, 2), round(-A_zone_y_bk, 2)],
                 [round(tn*E_zone_y_bk, 2), round(-E_zone_y_bk, 2)],
                 [round(E_zone_x_sd, 2), round(-tn*E_zone_x_sd, 2)]]
    Asector_3 = [[round(tn*E_zone_y_bk, 2), round(-E_zone_y_bk, 2)],
                 [round(tn*A_zone_y_bk, 2), round(-A_zone_y_bk, 2)],
                 [round(-tn*A_zone_y_bk, 2), round(-A_zone_y_bk, 2)],
                 [round(-tn*E_zone_y_bk, 2), round(-E_zone_y_bk, 2)],
                 [round(tn*E_zone_y_bk, 2), round(-E_zone_y_bk, 2)]]
    Asector_4 = [[round(-tn*E_zone_y_bk, 2), round(-E_zone_y_bk, 2)],
                 [round(-tn*A_zone_y_bk, 2), round(-A_zone_y_bk, 2)],
                 [round(-A_zone_x_sd, 2), round(-tn*A_zone_x_sd, 2)],
                 [round(-E_zone_x_sd, 2), round(-tn*E_zone_x_sd, 2)],
                 [round(-tn*E_zone_y_bk, 2), round(-E_zone_y_bk, 2)]]
    Asector_5 = [[round(-E_zone_x_sd, 2), round(-tn*E_zone_x_sd, 2)],
                 [round(-A_zone_x_sd, 2), round(-tn*A_zone_x_sd, 2)],
                 [round(-A_zone_x_sd, 2), round(tn*A_zone_x_sd, 2)],
                 [round(-E_zone_x_sd, 2), round(tn*E_zone_x_sd, 2)],
                 [round(-E_zone_x_sd, 2), round(-tn*E_zone_x_sd, 2)]]
    Asector_6 = [[round(-E_zone_x_sd, 2), round(tn*E_zone_x_sd, 2)],
                 [round(-A_zone_x_sd, 2), round(tn*A_zone_x_sd, 2)],
                 [round(-tn*A_zone_y_fr, 2), round(A_zone_y_fr, 2)],
                 [round(-tn*E_zone_y_fr, 2), round(E_zone_y_fr, 2)],
                 [round(-E_zone_x_sd, 2), round(tn*E_zone_x_sd, 2)]]
    Asector_7 = [[round(-tn*E_zone_y_fr, 2), round(E_zone_y_fr, 2)],
                 [round(-tn*A_zone_y_fr, 2), round(A_zone_y_fr, 2)],
                 [round(tn*A_zone_y_fr, 2), round(A_zone_y_fr, 2)],
                 [round(tn*E_zone_y_fr, 2), round(E_zone_y_fr, 2)],
                 [round(-tn*E_zone_y_fr, 2), round(E_zone_y_fr, 2)]]
    Asector_8 = [[round(tn*E_zone_y_fr, 2), round(E_zone_y_fr, 2)],
                 [round(tn*A_zone_y_fr, 2), round(A_zone_y_fr, 2)],
                 [round(A_zone_x_sd, 2), round(tn*A_zone_x_sd, 2)],
                 [round(E_zone_x_sd, 2), round(tn*E_zone_x_sd, 2)],
                 [round(tn*E_zone_y_fr, 2), round(E_zone_y_fr, 2)]]
    
if aproxim == '3':
    Emergency = [[round(tn*E_zone_x_sd, 2), round(cs*E_zone_y_fr, 2)],
                 [round(math.sqrt(E_zone_x_sd**2/2), 2), round(math.sqrt(E_zone_y_fr**2/2), 2)],
                 [round(cs*E_zone_x_sd, 2), round(sn*E_zone_y_fr, 2)],
                 [round(E_zone_x_sd, 2), 0],
                 [round(cs*E_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(math.sqrt(E_zone_x_sd**2/2), 2), round(-math.sqrt(E_zone_y_bk**2/2), 2)],
                 [round(tn*E_zone_x_sd, 2), round(-cs*E_zone_y_bk, 2)],
                 [0, round(-E_zone_y_bk, 2)],
                 [round(-tn*E_zone_x_sd, 2), round(-cs*E_zone_y_bk, 2)],
                 [round(-math.sqrt(E_zone_x_sd**2/2), 2), round(-math.sqrt(E_zone_y_bk**2/2), 2)],
                 [round(-cs*E_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(-E_zone_x_sd, 2), 0],
                 [round(-cs*E_zone_x_sd, 2), round(sn*E_zone_y_fr, 2)],
                 [round(-math.sqrt(E_zone_x_sd**2/2), 2), round(math.sqrt(E_zone_y_fr**2/2), 2)],
                 [round(-tn*E_zone_x_sd, 2), round(cs*E_zone_y_fr, 2)],
                 [0, round(E_zone_y_fr, 2)],
                 [round(tn*E_zone_x_sd, 2), round(cs*E_zone_y_fr, 2)]]

    Asector_1 = [[round(tn*A_zone_x_sd, 2), round(cs*A_zone_y_fr, 2)],
                 [round(tn*E_zone_x_sd, 2), round(cs*E_zone_y_fr, 2)],
                 [0, round(E_zone_y_fr, 2)],
                 [round(-tn*E_zone_x_sd, 2), round(cs*E_zone_y_fr, 2)],
                 [round(-tn*A_zone_x_sd, 2), round(cs*A_zone_y_fr, 2)],
                 [0, round(A_zone_y_fr, 2)],
                 [round(tn*A_zone_x_sd, 2), round(cs*A_zone_y_fr, 2)]]
    Asector_2 = [[round(cs*A_zone_x_sd, 2), round(sn*A_zone_y_fr, 2)],
                 [round(cs*E_zone_x_sd, 2), round(sn*E_zone_y_fr, 2)],
                 [round(math.sqrt(E_zone_x_sd**2/2), 2), round(math.sqrt(E_zone_y_fr**2/2), 2)],
                 [round(tn*E_zone_x_sd, 2), round(cs*E_zone_y_fr, 2)],
                 [round(tn*A_zone_x_sd, 2), round(cs*A_zone_y_fr, 2)],
                 [round(math.sqrt(A_zone_x_sd**2/2), 2), round(math.sqrt(A_zone_y_fr**2/2), 2)],
                 [round(cs*A_zone_x_sd, 2), round(sn*A_zone_y_fr, 2)]]
    Asector_3 = [[round(cs*A_zone_x_sd, 2), round(-sn*A_zone_y_bk, 2)],
                 [round(cs*E_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(E_zone_x_sd, 2), 0],
                 [round(cs*E_zone_x_sd, 2), round(sn*E_zone_y_fr, 2)],
                 [round(cs*A_zone_x_sd, 2), round(sn*A_zone_y_fr, 2)],
                 [round(A_zone_x_sd, 2), 0],
                 [round(cs*A_zone_x_sd, 2), round(-sn*A_zone_y_bk, 2)]]
    Asector_4 = [[round(tn*A_zone_x_sd, 2), round(-cs*A_zone_y_bk, 2)],
                 [round(tn*E_zone_x_sd, 2), round(-cs*E_zone_y_bk, 2)],
                 [round(math.sqrt(E_zone_x_sd**2/2), 2), round(-math.sqrt(E_zone_y_bk**2/2), 2)],
                 [round(cs*E_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(cs*A_zone_x_sd, 2), round(-sn*A_zone_y_bk, 2)],
                 [round(math.sqrt(A_zone_x_sd**2/2), 2), round(-math.sqrt(A_zone_y_bk**2/2), 2)],
                 [round(tn*A_zone_x_sd, 2), round(-cs*A_zone_y_bk, 2)]]
    Asector_5 = [[round(-tn*A_zone_x_sd, 2), round(-cs*A_zone_y_bk, 2)],
                 [round(-tn*E_zone_x_sd, 2), round(-cs*E_zone_y_bk, 2)],
                 [0, round(-E_zone_y_bk, 2)],
                 [round(tn*E_zone_x_sd, 2), round(-cs*E_zone_y_bk, 2)],
                 [round(tn*A_zone_x_sd, 2), round(-cs*A_zone_y_bk, 2)],
                 [0, round(-A_zone_y_bk, 2)],
                 [round(-tn*A_zone_x_sd, 2), round(-cs*A_zone_y_bk, 2)]]
    Asector_6 = [[round(-cs*A_zone_x_sd, 2), round(-sn*A_zone_y_bk, 2)],
                 [round(-cs*E_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(-math.sqrt(E_zone_x_sd**2/2), 2), round(-math.sqrt(E_zone_y_bk**2/2), 2)],
                 [round(-tn*E_zone_x_sd, 2), round(-cs*E_zone_y_bk, 2)],
                 [round(-tn*A_zone_x_sd, 2), round(-cs*A_zone_y_bk, 2)],
                 [round(-math.sqrt(A_zone_x_sd**2/2), 2), round(-math.sqrt(A_zone_y_bk**2/2), 2)],
                 [round(-cs*A_zone_x_sd, 2), round(-sn*A_zone_y_bk, 2)]]
    Asector_7 = [[round(-cs*A_zone_x_sd, 2), round(sn*A_zone_y_fr, 2)],
                 [round(-cs*E_zone_x_sd, 2), round(sn*E_zone_y_fr, 2)],
                 [round(-E_zone_x_sd, 2), 0],
                 [round(-cs*E_zone_x_sd, 2), round(-sn*E_zone_y_bk, 2)],
                 [round(-cs*A_zone_x_sd, 2), round(-sn*A_zone_y_bk, 2)],
                 [round(-A_zone_x_sd, 2), 0],
                 [round(-cs*A_zone_x_sd, 2), round(sn*A_zone_y_fr, 2)]]
    Asector_8 = [[round(-tn*A_zone_x_sd, 2), round(cs*A_zone_y_fr, 2)],
                 [round(-tn*E_zone_x_sd, 2), round(cs*E_zone_y_fr, 2)],
                 [round(-math.sqrt(E_zone_x_sd**2/2), 2), round(math.sqrt(E_zone_y_fr**2/2), 2)],
                 [round(-cs*E_zone_x_sd, 2), round(sn*E_zone_y_fr, 2)],
                 [round(-cs*A_zone_x_sd, 2), round(sn*A_zone_y_fr, 2)],
                 [round(-math.sqrt(A_zone_x_sd**2/2), 2), round(math.sqrt(A_zone_y_fr**2/2), 2)],
                 [round(-tn*A_zone_x_sd, 2), round(cs*A_zone_y_fr, 2)]]
    
Emer_plot = pd.DataFrame(Emergency, columns=['x', 'y'])
Alert_sector = [Asector_1, Asector_2, Asector_3, Asector_4, Asector_5,
                Asector_6, Asector_7, Asector_8]
for i in Alert_sector:
    Alert_plot = pd.DataFrame(i, columns=['x', 'y'])
    plt.plot(Alert_plot['x'], Alert_plot['y'], marker = 'o', color = 'yellow')
plt.grid()
plt.plot(Emer_plot['x'], Emer_plot['y'], marker = 'o', color = 'red')