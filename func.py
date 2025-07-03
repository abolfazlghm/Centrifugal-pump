import numpy as np
from math import *
import pandas as pd
from shapely.geometry import Point, Polygon
  
Q = float(input("Enter Q (m³/h): "))
H = float(input("Enter H (m): "))
user_point =Point(Q, H)

file = pd.read_excel('Default Dataset.xlsx')

def f(x0,y0,polygon0):
  clean_file = file[[x0, y0]].dropna()
  x0 = clean_file[x0].to_numpy()
  y0 = clean_file[y0].to_numpy()
  polygon_points1 = [(float(xi), float(yi)) for xi, yi in zip(x0, y0)]
  polygon0 = Polygon(polygon_points1)
  return(polygon0)

polygon0 = f('xcurve1','ycurve1','polygon0')
polygon2 = f('xcurve2','ycurve2','polygon2')
polygon3 = f('xcurve3','ycurve3','polygon3')
polygon4 = f('xcurve4','ycurve4','polygon4')
polygon5 = f('xcurve5','ycurve5','polygon5')
polygon6 = f('xcurve6','ycurve6','polygon6')
polygon7 = f('xcurve7','ycurve7','polygon7')

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
    polygon110_32_125  = f('x110_32_125','y110_32_125','polygon110_32_125')
    polygon115_32_125  = f('x115_32_125','y115_32_125','polygon115_32_125')
    polygon120_32_125  = f('x120_32_125','y120_32_125','polygon120_32_125')
    polygon125_32_125  = f('x125_32_125','y125_32_125','polygon125_32_125')
    polygon130_32_125  = f('x130_32_125','y130_32_125','polygon130_32_125')
    polygon139_32_125  = f('x139_32_125','y139_32_125','polygon139_32_125')

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

    polygon63635_32_125 = f('x63635_32_125','y63635_32_125','polygon63635_32_125')
    polygon6263_32_125 = f('x6263_32_125','y6263_32_125','polygon6263_32_125')
    polygon6062_32_125 = f('x6062_32_125','y6062_32_125','polygon6062_32_125')
    polygon5960_32_125 = f('x5960_32_125','y5960_32_125','polygon5960_32_125')
    polygon5559_32_125 = f('x5559_32_125','y5559_32_125','polygon5559_32_125')
    polygon5055_32_125 = f('x5055_32_125','y5055_32_125','polygon5055_32_125')

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
    polygon130_32_160 = f('x130_32_160','y130_32_160','polygon130_32_160')
    polygon140_32_160 = f('x140_32_160','y140_32_160','polygon140_32_160')
    polygon150_32_160 = f('x150_32_160','y150_32_160','polygon150_32_160')
    polygon160_32_160 = f('x160_32_160','y160_32_160','polygon160_32_160')
    polygon169_32_160 = f('x169_32_160','y169_32_160','polygon169_32_160')

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

    polygon62636_32_160 = f('x62636_32_160','y62636_32_160','polygon62636_32_160')
    polygon6062_32_160  = f('x6062_32_160','y6062_32_160','polygon6062_32_160')
    polygon5860_32_160  = f('x5860_32_160','y5860_32_160','polygon5860_32_160')
    polygon5558_32_160  = f('x5558_32_160','y5558_32_160','polygon5558_32_160')
    polygon5055_32_160  = f('x5055_32_160','y5055_32_160','polygon5055_32_160') 
    polygon4550_32_160  = f('x4550_32_160','y4550_32_160','polygon4550_32_160')

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
   polygon110_40_125 = f('x110_40_125','y110_40_125','polygon110_40_125')
   polygon115_40_125 = f('x115_40_125','y115_40_125','polygon115_40_125')
   polygon120_40_125 = f('x120_40_125','y120_40_125','polygon120_40_125')
   polygon125_40_125 = f('x125_40_125','y125_40_125','polygon125_40_125')
   polygon130_40_125 = f('x130_40_125','y130_40_125','polygon130_40_125')
   polygon135_40_125 = f('x135_40_125','y135_40_125','polygon135_40_125')
   polygon139_40_125 = f('x139_40_125','y139_40_125','polygon139_40_125')

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
    
   polygon6870_40_125 = f('x6870_40_125','y6870_40_125','polygon6870_40_125')
   polygon6568_40_125 = f('x6568_40_125','y6568_40_125','polygon6568_40_125')
   polygon6065_40_125 = f('x6065_40_125','y6065_40_125','polygon6065_40_125')
   polygon5560_40_125 = f('x5560_40_125','y5560_40_125','polygon5560_40_125')
   polygon5055_40_125 = f('x5055_40_125','y5055_40_125','polygon5055_40_125')

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
    polygon130_40_160 = f('x130_40_160','y130_40_160','polygon130_40_160')
    polygon140_40_160 = f('x140_40_160','y140_40_160','polygon140_40_160')
    polygon150_40_160 = f('x150_40_160','y150_40_160','polygon150_40_160')
    polygon160_40_160 = f('x160_40_160','y160_40_160','polygon160_40_160')
    polygon169_40_160 = f('x169_40_160','y169_40_160','polygon169_40_160')
    
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

    polygon66675_40_160 = f('x66675_40_160','y66675_40_160','polygon66675_40_160')
    polygon6466_40_160  = f('x6466_40_160','y6466_40_160','polygon6466_40_160')
    polygon6064_40_160  = f('x6064_40_160','y6064_40_160','polygon6064_40_160')
    polygon5560_40_160  = f('x5560_40_160','y5560_40_160','polygon5560_40_160')
    polygon5055_40_160  = f('x5055_40_160','y5055_40_160','polygon5055_40_160')
    polygon4550_40_160  = f('x4550_40_160','y4550_40_160','polygon4550_40_160')

    if polygon66675_40_160.contains(user_point):
      print("Efficiency : 66-67.5 %")
    elif polygon6466_40_160.contains(user_point):
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
    polygon110_50_125 = f('x110_50_125','y110_50_125','polygon110_50_125')
    polygon115_50_125 = f('x115_50_125','y115_50_125','polygon115_50_125')
    polygon120_50_125 = f('x120_50_125','y120_50_125','polygon120_50_125')
    polygon125_50_125 = f('x125_50_125','y125_50_125','polygon125_50_125')
    polygon130_50_125 = f('x130_50_125','y130_50_125','polygon130_50_125')
    polygon139_50_125 = f('x139_50_125','y139_50_125','polygon139_50_125')

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

    polygon7778_50_125 = f('x7778_50_125','y7778_50_125','polygon7778_50_125')
    polygon7577_50_125 = f('x7577_50_125','y7577_50_125','polygon7577_50_125')
    polygon7075_50_125 = f('x7075_50_125','y7075_50_125','polygon7075_50_125')
    polygon6070_50_125 = f('x6070_50_125','y6070_50_125','polygon6070_50_125')

    if polygon7778_50_125.contains(user_point):
      print("Efficiency : 77-78 %")
    elif polygon7577_50_125.contains(user_point):
      print("Efficiency : 75-77 %")
    elif polygon7075_50_125.contains(user_point):
      print("Efficiency : 70-75 %")
    elif polygon6070_50_125.contains(user_point):
      print("Efficiency : 60-70 %")

elif i == 6:
    polygon130_50_160 = f('x130_50_160','y130_50_160','polygon130_50_160')
    polygon140_50_160 = f('x140_50_160','y140_50_160','polygon140_50_160')
    polygon150_50_160 = f('x150_50_160','y150_50_160','polygon150_50_160')
    polygon160_50_160 = f('x160_50_160','y160_50_160','polygon160_50_160')
    polygon169_50_160 = f('x169_50_160','y169_50_160','polygon169_50_160')
  
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

    polygon7375_50_160 = f('x375_50_160','y375_50_160','polygon375_50_160')
    polygon7073_50_160 = f('x7073_50_160','y7073_50_160','polygon7073_50_160')
    polygon6570_50_160 = f('x6570_50_160','y6570_50_160','polygon6570_50_160')
    polygon6065_50_160 = f('x6065_50_160','y6065_50_160','polygon6065_50_160')
    polygon5560_50_160 = f('x5560_50_160','y5560_50_160','polygon5560_50_160')

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
    polygon170_40_200 = f('x170_40_200','y170_40_200','polygon170_40_200')
    polygon180_40_200 = f('x180_40_200','y180_40_200','polygon180_40_200')
    polygon190_40_200 = f('x190_40_200','y190_40_200','polygon190_40_200')
    polygon200_40_200 = f('x200_40_200','y200_40_200','polygon200_40_200')
    polygon209_40_200 = f('x209_40_200','y209_40_200','polygon209_40_200')
    
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

    polygon5054_40_200 = f('x5054_40_200','y5054_40_200','polygon5054_40_200')
    polygon4550_40_200 = f('x4550_40_200','y4550_40_200','polygon4550_40_200')
    polygon4045_40_200 = f('x4045_40_200','y4045_40_200','polygon4045_40_200')
    polygon5457_40_200 = f('x5457_40_200','y5457_40_200','polygon5457_40_200')
    polygon3540_40_200 = f('x3540_40_200','y3540_40_200','polygon3540_40_200')

    if polygon5054_40_200.contains(user_point):
      print("Efficiency : 50-54 %")
    if polygon4550_40_200.contains(user_point):
      print("Efficiency : 45-50 %")
    elif polygon4045_40_200.contains(user_point):
      print("Efficiency : 40-45 %")
    elif polygon5457_40_200.contains(user_point):
      print("Efficiency : 54-57 %")
    elif polygon3540_40_200.contains(user_point):
      print("Efficiency : 35-40 %")