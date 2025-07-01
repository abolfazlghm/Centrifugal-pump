import numpy as np
from math import *
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Point, Polygon
from matplotlib.path import Path

Q = float(input("Enter Q (m³/h): "))
H = float(input("Enter H (m): "))
user_point =Point(Q, H)

file = pd.read_excel('D:\\Python\\Ex\\Default Dataset.xlsx')

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
    print("✅1")
    i = 1;
elif  polygon2.contains(user_point):
    print("✅2")
    i = 2;
elif  polygon3.contains(user_point):
    print("✅3")
    i = 3;
elif  polygon4.contains(user_point):
    print("✅4")
    i = 4;
elif  polygon5.contains(user_point):
    print("✅5")
    i = 5;
elif  polygon6.contains(user_point):
    print("✅6")
    i = 6;
elif  polygon7.contains(user_point):
    print("✅7")
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
     print("D = 110")
    elif polygon115_32_125.contains(user_point):
     print("D = 115")
    elif polygon120_32_125.contains(user_point):
     print("D = 120")
    elif polygon125_32_125.contains(user_point):
     print("D = 125")
    elif polygon130_32_125.contains(user_point):
     print("D = 130")
    elif polygon139_32_125.contains(user_point):
     print("D = 139")
    else:
        print("out of area")

     
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
        print("D = 130")
    elif polygon140_32_160.contains(user_point):
        print("D = 140")
    elif polygon150_32_160.contains(user_point):
        print("D = 150")
    elif polygon160_32_160.contains(user_point):
        print("D = 160")
    elif polygon169_32_160.contains(user_point):
        print("D = 169")
    else:
        print("out of area")


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
        print("D = 110")
    elif polygon115_40_125.contains(user_point):
        print("D = 115")
    elif polygon120_40_125.contains(user_point):
        print("D = 120")
    elif polygon125_40_125.contains(user_point):
        print("D = 125")
    elif polygon130_40_125.contains(user_point):
        print("D = 130")
    elif polygon135_40_125.contains(user_point):
        print("D = 135")
    elif polygon139_40_125.contains(user_point):
        print("D = 139")
    else:
        print("out of area")


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
        print("D = 130")
    elif polygon140_40_160.contains(user_point):
        print("D = 140")
    elif polygon150_40_160.contains(user_point):
        print("D = 150")
    elif polygon160_40_160.contains(user_point):
        print("D = 160")
    elif polygon169_40_160.contains(user_point):
        print("D = 169")
    else:
        print("out of area")


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
      print("D = 110")
    elif polygon115_50_125.contains(user_point):
      print("D = 115")
    elif polygon120_50_125.contains(user_point):
       print("D = 120")
    elif polygon125_50_125.contains(user_point):
       print("D = 125")
    elif polygon130_50_125.contains(user_point):
       print("D = 130")
    elif polygon139_50_125.contains(user_point):
       print("D = 139")
    else:
        print("out of area")
 


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
      print("D = 130")
    elif polygon140_50_160.contains(user_point):
      print("D = 140")
    elif polygon150_50_160.contains(user_point):
      print("D = 150")
    elif polygon160_50_160.contains(user_point):
      print("D = 160")
    elif polygon169_50_160.contains(user_point):
      print("D = 169")
    else:
        print("out of area")



    
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
        print("D = 170")
    elif polygon180_40_200.contains(user_point):
        print("D = 180")
    elif polygon190_40_200.contains(user_point):
        print("D = 190")
    elif polygon200_40_200.contains(user_point):
        print("D = 200")
    elif polygon209_40_200.contains(user_point):
        print("D = 209")
    else:
        print("out of area")


    
     

