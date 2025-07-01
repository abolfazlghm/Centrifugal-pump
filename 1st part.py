import numpy as np
from math import *
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Point, Polygon
from matplotlib.path import Path

Q = float(input("Enter Q (m³/h): "))
H = float(input("Enter H (m): "))
user_point =Point(Q, H)

file = pd.read_excel('Dataset.xlsx')

clean_file = file[['xcurve1', 'ycurve1']].dropna()
x1 = clean_file['xcurve1'].to_numpy()
y1 = clean_file['ycurve1'].to_numpy()
polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip(x1, y1)]
polygon0 = Polygon(polygon_points1)

clean_file = file[['xcurve2', 'ycurve2']].dropna()
x2 = clean_file['xcurve2'].to_numpy()
y2 = clean_file['ycurve2'].to_numpy()
polygon_points2 = [(float(xi), float(yi)) for xi, yi in zip(x2, y2)]
polygon2 = Polygon(polygon_points2)

clean_file = file[['xcurve3', 'ycurve3']].dropna()
x3 = clean_file['xcurve3'].to_numpy()
y3 = clean_file['ycurve3'].to_numpy()
polygon_points3 = [(float(xi), float(yi)) for xi, yi in zip(x3, y3)]
polygon3 = Polygon(polygon_points3)

clean_file = file[['xcurve4', 'ycurve4']].dropna()
x4 = clean_file['xcurve4'].to_numpy()
y4 = clean_file['ycurve4'].to_numpy()
polygon_points4 = [(float(xi), float(yi)) for xi, yi in zip(x4, y4)]
polygon4 = Polygon(polygon_points4)

clean_file = file[['xcurve5', 'ycurve5']].dropna()
x5 = clean_file['xcurve5'].to_numpy()
y5 = clean_file['ycurve5'].to_numpy()
polygon_points5 = [(float(xi), float(yi)) for xi, yi in zip(x5, y5)]
polygon5 = Polygon(polygon_points5)

clean_file = file[['xcurve6', 'ycurve6']].dropna()
x6 = clean_file['xcurve6'].to_numpy()
y6 = clean_file['ycurve6'].to_numpy()
polygon_points6 = [(float(xi), float(yi)) for xi, yi in zip(x6, y6)]
polygon6 = Polygon(polygon_points6)

clean_file = file[['xcurve7', 'ycurve7']].dropna()
x7 = clean_file['xcurve7'].to_numpy()
y7 = clean_file['ycurve7'].to_numpy()
polygon_points7 = [(float(xi), float(yi)) for xi, yi in zip(x7, y7)]
polygon7 = Polygon(polygon_points7)

if polygon0.contains(user_point):
    print("Pump type: 32_125")
    i = 1;
elif  polygon2.contains(user_point):
    print("Pump type: 32_160")
    i = 2;
elif  polygon3.contains(user_point):
    print("Pump type: 40_125")
    i = 3;
elif  polygon4.contains(user_point):
    print("Pump type: 40_160")
    i = 4;
elif  polygon5.contains(user_point):
    print("Pump type: 50_125")
    i = 5;
elif  polygon6.contains(user_point):
    print("Pump type: 50_160")
    i = 6;
elif  polygon7.contains(user_point):
    print("Pump type: 40_200")
    i = 7;
else:
    print("❌ Out of curves")
    i = 0;


if i == 1:
    clean_file = file[['x110_32_125','y110_32_125']].dropna()
    x110_32_125 = clean_file['x110_32_125'].to_numpy()
    y110_32_125 = clean_file['y110_32_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x110_32_125, y110_32_125)]
    polygon110_32_125 = Polygon(polygon_points1)
    
    clean_file = file[['x115_32_125','y115_32_125']].dropna()
    x115_32_125 = clean_file['x115_32_125'].to_numpy()
    y115_32_125 = clean_file['y115_32_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x115_32_125, y115_32_125)]
    polygon115_32_125 = Polygon(polygon_points1)

    clean_file = file[['x120_32_125','y120_32_125']].dropna()
    x120_32_125 = clean_file['x120_32_125'].to_numpy()
    y120_32_125 = clean_file['y120_32_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x120_32_125, y120_32_125)]
    polygon120_32_125 = Polygon(polygon_points1)

    clean_file = file[['x125_32_125','y125_32_125']].dropna()
    x125_32_125 = clean_file['x125_32_125'].to_numpy()
    y125_32_125 = clean_file['y125_32_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x125_32_125, y125_32_125)]
    polygon125_32_125 = Polygon(polygon_points1)

    clean_file = file[['x130_32_125','y130_32_125']].dropna()
    x130_32_125 = clean_file['x130_32_125'].to_numpy()
    y130_32_125 = clean_file['y130_32_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x130_32_125, y130_32_125)]
    polygon130_32_125 = Polygon(polygon_points1)

    clean_file = file[['x139_32_125','y139_32_125']].dropna()
    x139_32_125 = clean_file['x139_32_125'].to_numpy()
    y139_32_125 = clean_file['y139_32_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x139_32_125, y139_32_125)]
    polygon139_32_125 = Polygon(polygon_points1)

    if polygon110_32_125.contains(user_point):
     print("Diameter = 110")
     print("P = 0.68 kW")
    elif polygon115_32_125.contains(user_point):
     print("Diameter = 115")
     print("P = 0.85 kW")

    elif polygon120_32_125.contains(user_point):
     print("Diameter = 120")
     print("P = 0.97kW")

    elif polygon125_32_125.contains(user_point):
     print("Diameter = 125")
     print("P = 1.15 kW")

    elif polygon130_32_125.contains(user_point):
     print("Diameter = 130")
     print("P = 1.35 kW")

    elif polygon139_32_125.contains(user_point):
     print("Diameter = 139")
     print("P = 2.16 kW")
    else:
        print("out of area")

    clean_file = file[['x63635_32_125','y63635_32_125']].dropna()
    x63635_32_125 = clean_file['x63635_32_125'].to_numpy()
    y63635_32_125 = clean_file['y63635_32_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x63635_32_125, y63635_32_125)]
    polygon63635_32_125 = Polygon(polygon_points1)

    clean_file = file[['x6263_32_125','y6263_32_125']].dropna()
    x6263_32_125 = clean_file['x6263_32_125'].to_numpy()
    y6263_32_125 = clean_file['y6263_32_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x6263_32_125, y6263_32_125)]
    polygon6263_32_125 = Polygon(polygon_points1)

    clean_file = file[['x6062_32_125','y6062_32_125']].dropna()
    x6062_32_125 = clean_file['x6062_32_125'].to_numpy()
    y6062_32_125 = clean_file['y6062_32_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x6062_32_125, y6062_32_125)]
    polygon6062_32_125 = Polygon(polygon_points1)

    clean_file = file[['x5960_32_125','y5960_32_125']].dropna()
    x5960_32_125 = clean_file['x5960_32_125'].to_numpy()
    y5960_32_125 = clean_file['y5960_32_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x5960_32_125,y5960_32_125)]
    polygon5960_32_125 = Polygon(polygon_points1)

    clean_file = file[['x5559_32_125','y5559_32_125']].dropna()
    x5559_32_125 = clean_file['x5559_32_125'].to_numpy()
    y5559_32_125 = clean_file['y5559_32_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x5559_32_125,y5559_32_125)]
    polygon5559_32_125 = Polygon(polygon_points1)

    clean_file = file[['x5055_32_125','y5055_32_125']].dropna()
    x5055_32_125 = clean_file['x5055_32_125'].to_numpy()
    y5055_32_125 = clean_file['y5055_32_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x5055_32_125,y5055_32_125)]
    polygon5055_32_125 = Polygon(polygon_points1)

    if polygon63635_32_125.contains(user_point):
      print("Efficiency : 63-63.5 %")
    elif polygon6263_32_125.contains(user_point):
      print("Efficiency : 62-63 %")
    elif polygon6062_32_125.contains(user_point):
      print("Efficiency : 60-62 %")
    elif polygon5960_32_125.contains(user_point):
      print("Efficiency : 59-60 %")
    elif polygon5559_32_125.contains(user_point):
      print("Efficiency : 55-59 %")
    elif polygon5055_32_125.contains(user_point):
      print("Efficiency : 50-55 %")
        
     
elif i == 2:
    clean_file = file[['x130_32_160','y130_32_160']].dropna()
    x130_32_160 = clean_file['x130_32_160'].to_numpy()
    y130_32_160 = clean_file['y130_32_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x130_32_160, y130_32_160)]
    polygon130_32_160 = Polygon(polygon_points1)

    clean_file = file[['x140_32_160','y140_32_160']].dropna()
    x140_32_160 = clean_file['x140_32_160'].to_numpy()
    y140_32_160 = clean_file['y140_32_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x140_32_160, y140_32_160)]
    polygon140_32_160 = Polygon(polygon_points1)

    clean_file = file[['x150_32_160','y150_32_160']].dropna()
    x150_32_160 = clean_file['x150_32_160'].to_numpy()
    y150_32_160 = clean_file['y150_32_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x150_32_160, y150_32_160)]
    polygon150_32_160 = Polygon(polygon_points1)

    clean_file = file[['x160_32_160','y160_32_160']].dropna()
    x160_32_160 = clean_file['x160_32_160'].to_numpy()
    y160_32_160 = clean_file['y160_32_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x160_32_160, y160_32_160)]
    polygon160_32_160 = Polygon(polygon_points1)

    clean_file = file[['x169_32_160','y169_32_160']].dropna()
    x169_32_160 = clean_file['x169_32_160'].to_numpy()
    y169_32_160 = clean_file['y169_32_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x169_32_160, y169_32_160)]
    polygon169_32_160 = Polygon(polygon_points1)

    if polygon130_32_160.contains(user_point):
        print("Diameter = 130")
        print("P = 1.4 kW")
    elif polygon140_32_160.contains(user_point):
        print("Diameter = 140")
        print("P = 1.8 kW")
    elif polygon150_32_160.contains(user_point):
        print("Diameter = 150")
        print("P = 2.4 kW")
    elif polygon160_32_160.contains(user_point):
        print("Diameter = 160")
        print("P = 3.2 kW")
    elif polygon169_32_160.contains(user_point):
        print("Diameter = 169")
        print("P = 3.8 kW")
    else:
        print("out of area")

    clean_file = file[['x62636_32_160','y62636_32_160']].dropna()
    x62636_32_160 = clean_file['x62636_32_160'].to_numpy()
    y62636_32_160 = clean_file['y62636_32_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x62636_32_160, y62636_32_160)]
    polygon62636_32_160 = Polygon(polygon_points1)

    clean_file = file[['x6062_32_160','y6062_32_160']].dropna()
    x6062_32_160 = clean_file['x6062_32_160'].to_numpy()
    y6062_32_160 = clean_file['y6062_32_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x6062_32_160, y6062_32_160)]
    polygon6062_32_160 = Polygon(polygon_points1)

    clean_file = file[['x5860_32_160','y5860_32_160']].dropna()
    x5860_32_160 = clean_file['x5860_32_160'].to_numpy()
    y5860_32_160 = clean_file['y5860_32_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x5860_32_160, y5860_32_160)]
    polygon5860_32_160 = Polygon(polygon_points1)

    clean_file = file[['x5558_32_160','y5558_32_160']].dropna()
    x5558_32_160 = clean_file['x5558_32_160'].to_numpy()
    y5558_32_160 = clean_file['y5558_32_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x5558_32_160, y5558_32_160)]
    polygon5558_32_160 = Polygon(polygon_points1)

    clean_file = file[['x5055_32_160','y5055_32_160']].dropna()
    x5055_32_160 = clean_file['x5055_32_160'].to_numpy()
    y5055_32_160 = clean_file['y5055_32_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x5055_32_160, y5055_32_160)]
    polygon5055_32_160 = Polygon(polygon_points1)

    clean_file = file[['x4550_32_160','y4550_32_160']].dropna()
    x4550_32_160 = clean_file['x4550_32_160'].to_numpy()
    y4550_32_160 = clean_file['y4550_32_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x4550_32_160, y4550_32_160)]
    polygon4550_32_160 = Polygon(polygon_points1)

    if polygon62636_32_160.contains(user_point):
      print("Efficiency : 62-63.5 %")
    elif polygon6062_32_160.contains(user_point):
      print("Efficiency : 60-62 %")
    elif polygon5860_32_160.contains(user_point):
      print("Efficiency : 58-60 %")
    elif polygon5558_32_160.contains(user_point):
      print("Efficiency : 55-58 %")
    elif polygon5055_32_160.contains(user_point):
      print("Efficiency : 50-55 %")
    elif polygon4550_32_160.contains(user_point):
      print("Efficiency : 45-50 %")


elif i == 3:
    clean_file = file[['x110_40_125','y110_40_125']].dropna()
    x110_40_125 = clean_file['x110_40_125'].to_numpy()
    y110_40_125 = clean_file['y110_40_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x110_40_125, y110_40_125)]
    polygon110_40_125 = Polygon(polygon_points1)

    clean_file = file[['x115_40_125','y115_40_125']].dropna()
    x115_40_125 = clean_file['x115_40_125'].to_numpy()
    y115_40_125 = clean_file['y115_40_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x115_40_125, y115_40_125)]
    polygon115_40_125 = Polygon(polygon_points1)

    clean_file = file[['x120_40_125','y120_40_125']].dropna()
    x120_40_125 = clean_file['x120_40_125'].to_numpy()
    y120_40_125 = clean_file['y120_40_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x120_40_125, y120_40_125)]
    polygon120_40_125 = Polygon(polygon_points1)

    clean_file = file[['x125_40_125','y125_40_125']].dropna()
    x125_40_125 = clean_file['x125_40_125'].to_numpy()
    y125_40_125 = clean_file['y125_40_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x125_40_125, y125_40_125)]
    polygon125_40_125 = Polygon(polygon_points1)

    clean_file = file[['x130_40_125','y130_40_125']].dropna()
    x130_40_125 = clean_file['x130_40_125'].to_numpy()
    y130_40_125 = clean_file['y130_40_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x130_40_125, y130_40_125)]
    polygon130_40_125 = Polygon(polygon_points1)

    clean_file = file[['x135_40_125','y135_40_125']].dropna()
    x135_40_125 = clean_file['x135_40_125'].to_numpy()
    y135_40_125 = clean_file['y135_40_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x135_40_125, y135_40_125)]
    polygon135_40_125 = Polygon(polygon_points1)

    clean_file = file[['x139_40_125','y139_40_125']].dropna()
    x139_40_125 = clean_file['x139_40_125'].to_numpy()
    y139_40_125 = clean_file['y139_40_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x139_40_125, y139_40_125)]
    polygon139_40_125 = Polygon(polygon_points1)

    if polygon110_40_125.contains(user_point):
        print("Diameter = 110")
        print("P = 1.15kW")
    elif polygon115_40_125.contains(user_point):
        print("Diameter = 115")
        print("P = 1.3kW")
    elif polygon120_40_125.contains(user_point):
        print("Diameter = 120")
        print("P = 1.5kW")
    elif polygon125_40_125.contains(user_point):
        print("Diameter = 125")
        print("P = 1.7kW")
    elif polygon130_40_125.contains(user_point):
        print("Diameter = 130")
        print("P = 1.95kW")
    elif polygon135_40_125.contains(user_point):
        print("Diameter = 135")
        print("P = 2.22kW")
    elif polygon139_40_125.contains(user_point):
        print("Diameter = 139")
        print("P = 2.5kW")
    else:
        print("out of area")

    clean_file = file[['x6870_40_125','y6870_40_125']].dropna()
    x6870_40_125 = clean_file['x6870_40_125'].to_numpy()
    y6870_40_125 = clean_file['y6870_40_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x6870_40_125,y6870_40_125)]
    polygon6870_40_125 = Polygon(polygon_points1)

    clean_file = file[['x6568_40_125','y6568_40_125']].dropna()
    x6568_40_125 = clean_file['x6568_40_125'].to_numpy()
    y6568_40_125 = clean_file['y6568_40_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x6568_40_125,y6568_40_125)]
    polygon6568_40_125 = Polygon(polygon_points1)

    clean_file = file[['x6065_40_125','y6065_40_125']].dropna()
    x6065_40_125 = clean_file['x6065_40_125'].to_numpy()
    y6065_40_125 = clean_file['y6065_40_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x6065_40_125,y6065_40_125)]
    polygon6065_40_125 = Polygon(polygon_points1)

    clean_file = file[['x5560_40_125','y5560_40_125']].dropna()
    x5560_40_125 = clean_file['x5560_40_125'].to_numpy()
    y5560_40_125 = clean_file['y5560_40_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x5560_40_125,y5560_40_125)]
    polygon5560_40_125 = Polygon(polygon_points1)

    clean_file = file[['x5055_40_125','y5055_40_125']].dropna()
    x5055_40_125 = clean_file['x5055_40_125'].to_numpy()
    y5055_40_125 = clean_file['y5055_40_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x5055_40_125,y5055_40_125)]
    polygon5055_40_125 = Polygon(polygon_points1)

    if polygon6870_40_125.contains(user_point):
      print("Efficiency : 68-70 %")
    elif polygon6568_40_125.contains(user_point):
      print("Efficiency : 65-68 %")
    elif polygon6065_40_125.contains(user_point):
      print("Efficiency : 60-65 %")
    elif polygon5560_40_125.contains(user_point):
      print("Efficiency : 55-60 %")
    elif polygon5055_40_125.contains(user_point):
      print("Efficiency : 50-55 %")
        




elif i == 4:
    clean_file = file[['x130_40_160','y130_40_160']].dropna()
    x130_40_160 = clean_file['x130_40_160'].to_numpy()
    y130_40_160 = clean_file['y130_40_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x130_40_160, y130_40_160)]
    polygon130_40_160 = Polygon(polygon_points1)

    clean_file = file[['x140_40_160','y140_40_160']].dropna()
    x140_40_160 = clean_file['x140_40_160'].to_numpy()
    y140_40_160 = clean_file['y140_40_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x140_40_160, y140_40_160)]
    polygon140_40_160 = Polygon(polygon_points1)

    clean_file = file[['x150_40_160','y150_40_160']].dropna()
    x150_40_160 = clean_file['x150_40_160'].to_numpy()
    y150_40_160 = clean_file['y150_40_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x150_40_160, y150_40_160)]
    polygon150_40_160 = Polygon(polygon_points1)

    clean_file = file[['x160_40_160','y160_40_160']].dropna()
    x160_40_160 = clean_file['x160_40_160'].to_numpy()
    y160_40_160 = clean_file['y160_40_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x160_40_160, y160_40_160)]
    polygon160_40_160 = Polygon(polygon_points1)

    clean_file = file[['x169_40_160','y169_40_160']].dropna()
    x169_40_160 = clean_file['x169_40_160'].to_numpy()
    y169_40_160 = clean_file['y169_40_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x169_40_160, y169_40_160)]
    polygon169_40_160 = Polygon(polygon_points1)

    if polygon130_40_160.contains(user_point):
        print("Diameter = 130")
        print("P = 1.8kW")
    elif polygon140_40_160.contains(user_point):
        print("Diameter = 140")
        print("P = 2.3kW")
    elif polygon150_40_160.contains(user_point):
        print("Diameter = 150")
        print("P = 3kW")
    elif polygon160_40_160.contains(user_point):
        print("Diameter = 160")
        print("P = 3.8kW")
    elif polygon169_40_160.contains(user_point):
        print("Diameter = 169")
        print("P = 4.6kW")
    else:
        print("out of area")


    clean_file = file[['x66675_40_160','y66675_40_160']].dropna()
    x66675_40_160 = clean_file['x66675_40_160'].to_numpy()
    y66675_40_160 = clean_file['y66675_40_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x66675_40_160,y66675_40_160)]
    polygon66675_40_160 = Polygon(polygon_points1)

    clean_file = file[['x6466_40_160','y6466_40_160']].dropna()
    x6466_40_160 = clean_file['x6466_40_160'].to_numpy()
    y6466_40_160 = clean_file['y6466_40_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x6466_40_160,y6466_40_160)]
    polygon6466_40_160 = Polygon(polygon_points1)

    clean_file = file[['x6064_40_160','y6064_40_160']].dropna()
    x6064_40_160 = clean_file['x6064_40_160'].to_numpy()
    y6064_40_160 = clean_file['y6064_40_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x6064_40_160,y6064_40_160)]
    polygon6064_40_160 = Polygon(polygon_points1)

    clean_file = file[['x5560_40_160','y5560_40_160']].dropna()
    x5560_40_160 = clean_file['x5560_40_160'].to_numpy()
    y5560_40_160 = clean_file['y5560_40_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x5560_40_160,y5560_40_160)]
    polygon5560_40_160 = Polygon(polygon_points1)

    clean_file = file[['x5055_40_160','y5055_40_160']].dropna()
    x5055_40_160 = clean_file['x5055_40_160'].to_numpy()
    y5055_40_160 = clean_file['y5055_40_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x5055_40_160,y5055_40_160)]
    polygon5055_40_160 = Polygon(polygon_points1)

    clean_file = file[['x4550_40_160','y4550_40_160']].dropna()
    x4550_40_160 = clean_file['x4550_40_160'].to_numpy()
    y4550_40_160 = clean_file['y4550_40_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x4550_40_160,y4550_40_160)]
    polygon4550_40_160 = Polygon(polygon_points1)

    if polygon66675_40_160.contains(user_point):
      print("Efficiency : 66-67.5 %")
    if polygon6466_40_160.contains(user_point):
      print("Efficiency : 64-66 %")
    elif polygon6064_40_160.contains(user_point):
      print("Efficiency : 60-64 %")
    elif polygon5560_40_160.contains(user_point):
      print("Efficiency : 55-60 %")
    elif polygon5055_40_160.contains(user_point):
      print("Efficiency : 50-55 %")
    elif polygon4550_40_160.contains(user_point):
      print("Efficiency : 40-45 %")


elif i == 5:
    clean_file = file[['x110_50_125','y110_50_125']].dropna()
    x110_50_125 = clean_file['x110_50_125'].to_numpy()
    y110_50_125 = clean_file['y110_50_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x110_50_125, y110_50_125)]
    polygon110_50_125 = Polygon(polygon_points1)

    clean_file = file[['x115_50_125','y115_50_125']].dropna()
    x115_50_125 = clean_file['x115_50_125'].to_numpy()
    y115_50_125 = clean_file['y115_50_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x115_50_125, y115_50_125)]
    polygon115_50_125 = Polygon(polygon_points1)

    clean_file = file[['x120_50_125','y120_50_125']].dropna()
    x120_50_125 = clean_file['x120_50_125'].to_numpy()
    y120_50_125 = clean_file['y120_50_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x120_50_125, y120_50_125)]
    polygon120_50_125 = Polygon(polygon_points1)

    clean_file = file[['x125_50_125','y125_50_125']].dropna()
    x125_50_125 = clean_file['x125_50_125'].to_numpy()
    y125_50_125 = clean_file['y125_50_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x125_50_125, y125_50_125)]
    polygon125_50_125 = Polygon(polygon_points1)

    clean_file = file[['x130_50_125','y130_50_125']].dropna()
    x130_50_125 = clean_file['x130_50_125'].to_numpy()
    y130_50_125 = clean_file['y130_50_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x130_50_125, y130_50_125)]
    polygon130_50_125 = Polygon(polygon_points1)

    clean_file = file[['x139_50_125','y139_50_125']].dropna()
    x139_50_125 = clean_file['x139_50_125'].to_numpy()
    y139_50_125 = clean_file['y139_50_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x139_50_125, y139_50_125)]
    polygon139_50_125 = Polygon(polygon_points1)

    if polygon110_50_125.contains(user_point):
      print("Diameter = 110")
      print("P = 2.3kW")
    elif polygon115_50_125.contains(user_point):
      print("Diameter = 115")
      print("P = 2.6kW")
    elif polygon120_50_125.contains(user_point):
       print("Diameter = 120")
       print("P = 3kW")
    elif polygon125_50_125.contains(user_point):
       print("Diameter = 125")
       print("P = 3.4kW")
    elif polygon130_50_125.contains(user_point):
       print("Diameter = 130")
       print("P = 3.8kW")
    elif polygon139_50_125.contains(user_point):
       print("Diameter = 139")
       print("P = 5.1kW")
    else:
        print("out of area")


    clean_file = file[['x7778_50_125','y7778_50_125']].dropna()
    x7778_50_125 = clean_file['x7778_50_125'].to_numpy()
    y7778_50_125 = clean_file['y7778_50_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x7778_50_125, y7778_50_125)]
    polygon7778_50_125 = Polygon(polygon_points1)

    clean_file = file[['x7577_50_125','y7577_50_125']].dropna()
    x7577_50_125 = clean_file['x7577_50_125'].to_numpy()
    y7577_50_125 = clean_file['y7577_50_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x7577_50_125, y7577_50_125)]
    polygon7577_50_125 = Polygon(polygon_points1)

    clean_file = file[['x7075_50_125','y7075_50_125']].dropna()
    x7075_50_125 = clean_file['x7075_50_125'].to_numpy()
    y7075_50_125 = clean_file['y7075_50_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x7075_50_125, y7075_50_125)]
    polygon7075_50_125 = Polygon(polygon_points1)

    clean_file = file[['x6070_50_125','y6070_50_125']].dropna()
    x6070_50_125 = clean_file['x6070_50_125'].to_numpy()
    y6070_50_125 = clean_file['y6070_50_125'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x6070_50_125, y6070_50_125)]
    polygon6070_50_125 = Polygon(polygon_points1)

    if polygon7778_50_125.contains(user_point):
      print("Efficiency : 77-78 %")
    if polygon7577_50_125.contains(user_point):
      print("Efficiency : 75-77 %")
    elif polygon7075_50_125.contains(user_point):
      print("Efficiency : 70-75 %")
    elif polygon6070_50_125.contains(user_point):
      print("Efficiency : 60-70 %")





elif i == 6:
    clean_file = file[['x130_50_160','y130_50_160']].dropna()
    x130_50_160 = clean_file['x130_50_160'].to_numpy()
    y130_50_160 = clean_file['y130_50_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x130_50_160, y130_50_160)]
    polygon130_50_160 = Polygon(polygon_points1)

    clean_file = file[['x140_50_160','y140_50_160']].dropna()
    x140_50_160 = clean_file['x140_50_160'].to_numpy()
    y140_50_160 = clean_file['y140_50_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x140_50_160, y140_50_160)]
    polygon140_50_160 = Polygon(polygon_points1)

    clean_file = file[['x150_50_160','y150_50_160']].dropna()
    x150_50_160 = clean_file['x150_50_160'].to_numpy()
    y150_50_160 = clean_file['y150_50_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x150_50_160, y150_50_160)]
    polygon150_50_160 = Polygon(polygon_points1)

    clean_file = file[['x160_50_160','y160_50_160']].dropna()
    x160_50_160 = clean_file['x160_50_160'].to_numpy()
    y160_50_160 = clean_file['y160_50_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x160_50_160, y160_50_160)]
    polygon160_50_160 = Polygon(polygon_points1)

    clean_file = file[['x169_50_160','y169_50_160']].dropna()
    x169_50_160 = clean_file['x169_50_160'].to_numpy()
    y169_50_160 = clean_file['y169_50_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x169_50_160, y169_50_160)]
    polygon169_50_160 = Polygon(polygon_points1)

    if polygon130_50_160.contains(user_point):
      print("Diameter = 130")
      print("P = 2.7kW")
    elif polygon140_50_160.contains(user_point):
      print("Diameter = 140")
      print("P = 3.7kW")
    elif polygon150_50_160.contains(user_point):
      print("Diameter = 150")
      print("P = 4.8kW")
    elif polygon160_50_160.contains(user_point):
      print("Diameter = 160")
      print("P = 6.1kW")
    elif polygon169_50_160.contains(user_point):
      print("Diameter = 169")
      print("P = 7.7kW")
    else:
        print("out of area")


    clean_file = file[['x7375_50_160','y7375_50_160']].dropna()
    x7375_50_160 = clean_file['x7375_50_160'].to_numpy()
    y7375_50_160 = clean_file['y7375_50_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x7375_50_160, y7375_50_160)]
    polygon7375_50_160 = Polygon(polygon_points1)

    clean_file = file[['x7073_50_160','y7073_50_160']].dropna()
    x7073_50_160 = clean_file['x7073_50_160'].to_numpy()
    y7073_50_160 = clean_file['y7073_50_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x7073_50_160, y7073_50_160)]
    polygon7073_50_160 = Polygon(polygon_points1)

    clean_file = file[['x6570_50_160','y6570_50_160']].dropna()
    x6570_50_160 = clean_file['x6570_50_160'].to_numpy()
    y6570_50_160 = clean_file['y6570_50_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x6570_50_160, y6570_50_160)]
    polygon6570_50_160 = Polygon(polygon_points1)

    clean_file = file[['x6065_50_160','y6065_50_160']].dropna()
    x6065_50_160 = clean_file['x6065_50_160'].to_numpy()
    y6065_50_160 = clean_file['y6065_50_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x6065_50_160, y6065_50_160)]
    polygon6065_50_160 = Polygon(polygon_points1)

    clean_file = file[['x5560_50_160','y5560_50_160']].dropna()
    x5560_50_160 = clean_file['x5560_50_160'].to_numpy()
    y5560_50_160 = clean_file['y5560_50_160'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x5560_50_160, y5560_50_160)]
    polygon5560_50_160 = Polygon(polygon_points1)

    if polygon7375_50_160.contains(user_point):
      print("Efficiency : 73-75 %")
    elif polygon7073_50_160.contains(user_point):
      print("Efficiency : 70-73 %")
    if polygon6570_50_160.contains(user_point):
      print("Efficiency : 65-70 %")
    elif polygon6065_50_160.contains(user_point):
      print("Efficiency : 60-65 %")
    elif polygon5560_50_160.contains(user_point):
      print("Efficiency : 55-60 %")
    
elif i == 7:
    clean_file = file[['x170_40_200','y170_40_200']].dropna()
    x170_40_200 = clean_file['x170_40_200'].to_numpy()
    y170_40_200 = clean_file['y170_40_200'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x170_40_200, y170_40_200)]
    polygon170_40_200 = Polygon(polygon_points1)

    clean_file = file[['x180_40_200','y180_40_200']].dropna()
    x180_40_200 = clean_file['x180_40_200'].to_numpy()
    y180_40_200 = clean_file['y180_40_200'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x180_40_200, y180_40_200)]
    polygon180_40_200 = Polygon(polygon_points1)

    clean_file = file[['x190_40_200','y190_40_200']].dropna()
    x190_40_200 = clean_file['x190_40_200'].to_numpy()
    y190_40_200 = clean_file['y190_40_200'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x190_40_200, y190_40_200)]
    polygon190_40_200 = Polygon(polygon_points1)

    clean_file = file[['x200_40_200','y200_40_200']].dropna()
    x200_40_200 = clean_file['x200_40_200'].to_numpy()
    y200_40_200 = clean_file['y200_40_200'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x200_40_200, y200_40_200)]
    polygon200_40_200 = Polygon(polygon_points1)

    clean_file = file[['x209_40_200','y209_40_200']].dropna()
    x209_40_200 = clean_file['x209_40_200'].to_numpy()
    y209_40_200 = clean_file['y209_40_200'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x209_40_200, y209_40_200)]
    polygon209_40_200 = Polygon(polygon_points1)

    if polygon170_40_200.contains(user_point):
        print("Diameter = 170")
        print("P = 3.6kW")
    elif polygon180_40_200.contains(user_point):
        print("Diameter = 180")
        print("P = 4.5kW")
    elif polygon190_40_200.contains(user_point):
        print("Diameter = 190")
        print("P = 5.5kW")
    elif polygon200_40_200.contains(user_point):
        print("Diameter = 200")
        print("P = 6.6kW")
    elif polygon209_40_200.contains(user_point):
        print("Diameter = 209")
        print("P = 7.7kW")
    else:
        print("out of area")



    clean_file = file[['x5457_40_200','y5457_40_200']].dropna()
    x5457_40_200 = clean_file['x5457_40_200'].to_numpy()
    y5457_40_200 = clean_file['y5457_40_200'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x5457_40_200, y5457_40_200)]
    polygon5457_40_200 = Polygon(polygon_points1)

    clean_file = file[['x5054_40_200','y5054_40_200']].dropna()
    x5054_40_200 = clean_file['x5054_40_200'].to_numpy()
    y5054_40_200 = clean_file['y5054_40_200'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x5054_40_200, y5054_40_200)]
    polygon5054_40_200 = Polygon(polygon_points1)

    clean_file = file[['x4550_40_200','y4550_40_200']].dropna()
    x4550_40_200 = clean_file['x4550_40_200'].to_numpy()
    y4550_40_200 = clean_file['y4550_40_200'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x4550_40_200, y4550_40_200)]
    polygon4550_40_200 = Polygon(polygon_points1)

    clean_file = file[['x4045_40_200','y4045_40_200']].dropna()
    x4045_40_200 = clean_file['x4045_40_200'].to_numpy()
    y4045_40_200 = clean_file['y4045_40_200'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x4045_40_200, y4045_40_200)]
    polygon4045_40_200 = Polygon(polygon_points1)

    clean_file = file[['x5457_40_200','y5457_40_200']].dropna()
    x5457_40_200 = clean_file['x5457_40_200'].to_numpy()
    y5457_40_200 = clean_file['y5457_40_200'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x5457_40_200, y5457_40_200)]
    polygon5457_40_200 = Polygon(polygon_points1)

    clean_file = file[['x3540_40_200','y3540_40_200']].dropna()
    x3540_40_200 = clean_file['x3540_40_200'].to_numpy()
    y3540_40_200 = clean_file['y3540_40_200'].to_numpy()
    polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip( x3540_40_200, y3540_40_200)]
    polygon3540_40_200 = Polygon(polygon_points1)

    if polygon5054_40_200.contains(user_point):
      print("Efficiency : 50-54 %")
    elif polygon4550_40_200.contains(user_point):
      print("Efficiency : 45-50 %")
    if polygon4045_40_200.contains(user_point):
      print("Efficiency : 40-45 %")
    elif polygon5457_40_200.contains(user_point):
      print("Efficiency : 54-57 %")
    elif polygon3540_40_200.contains(user_point):
      print("Efficiency : 35-40 %")













    


    
     

