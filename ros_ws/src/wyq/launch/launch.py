from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # 包含MoveIt官方启动文件
    moveit_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            get_package_share_directory('moveit2_tutorials') + '/launch/demo.launch.py'
        ])
    )
    
    # 包含自定义节点启动文件
    demo_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            get_package_share_directory('my_moveit_demo') + '/launch/demo.launch.py'
        ])
    )

    return LaunchDescription([
        moveit_launch,
        demo_node
    ])