#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

laser_range = [None] * 721 # 라이다 센서 값을 받아올 리스트 선언
laser_range[360] = 1.0
left_before = 0.0
right_before = 0.0
count_left = 0
count_right = 0

def callback(data):         # Publish 되면 콜백 메서드 호출
    laser_input = data.ranges
    i = 0

    for laser_value in laser_input: # 라이다 센싱 값을 받아옵니다. 필터링을 통하여 제대로 받아온 값만 리스트에 넣습니다.
        if laser_value > 0:
            laser_range[i] = laser_value
            #if laser_range[i] > 0:
                #temp[i] = laser_range[i]
            i = i + 1
        else:
            i = i + 1
        #print(i, ' = ', laser_range[i])

    las_front = laser_range[329:389]    # 라이다는 총 720개의 센싱값을 받아옵니다. 각각 정면 측면의 범위를 지정해줬습니다.
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
