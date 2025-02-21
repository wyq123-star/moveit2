import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/wyq/docker/moveit2/ros_ws/install/my_moveit2'
