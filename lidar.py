#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

laser_range = [None] * 721
laser_range[360] = 1.0
left_before = 0.0
right_before = 0.0
count_left = 0
count_right = 0

def callback(data):
    laser_input = data.ranges
    i = 0

    for laser_value in laser_input:
        if laser_value > 0:
            laser_range[i] = laser_value
            #if laser_range[i] > 0:
                #temp[i] = laser_range[i]
            i = i + 1
        else:
            i = i + 1
        #print(i, ' = ', laser_range[i])

    las_front = laser_range[329:389]
    las_left = laser_range[509:569]
    las_right = laser_range[149:209]

    left = min(las_left)
    right = min(las_right)

    if min(las_front) > 1.0 or min(las_front) == None:
        print('Front obstacle detection')

    elif las_front <= 1.0 and left > right:
        print('Right obstacle detection')    
        
    else:
        print('Left obstacle detection')
        
rospy.init_node('ydlidar_node', anonymous=True)

sub = rospy.Subscriber("/scan", LaserScan, callback)
 
rospy.spin()
