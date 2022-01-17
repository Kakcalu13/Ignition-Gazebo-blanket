

def generator(total):
    Total = total
    x = 0.0
    y = 00
    z = 0.0
    flag = 0
    increment = 0
    while (increment < Total):
        print("<include>    \n<name>piece_",y, "</name>    \n<pose>", z, x," 10 0 0 0</pose>    \n<uri>model://blanket.sdf</uri>    \n</include>    \n\n")
        flag = flag + 1
        if flag == 4:
            flag = 0
            z = z + 0.1
            x = 0
        x = x + 0.1
        y = y + 1
        increment = increment + 1

def generator_joint(total):
    Total = total
    x = 0.0
    y = 00
    z = 0.0
    flag = 0
    increment = 0
    while (increment < Total):
        print("<joint name='plate_", y, "' type='revolute'>    \n<pose relative_to='piece_", y , "'/>\n<parent>piece_",y,"</parent>\n<child>piece_",y+1,"</child>    \n<axis>    \n<limit>    \n<lower>-1.79769e+308</lower>    \n<upper>1.79769e+308</upper>    \n</limit>    \n</axis>    \n</joint>")
        flag = flag + 1
        if flag == 4:
            flag = 0
            z = z + 0.1
            x = 0
        x = x + 0.1
        y = y + 1
        increment = increment + 1


generator(50)
#generator_joint(50)