from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from os.path import join

def generate_launch_description():
    # 包含 my_moveit2 包中的 launch 文件
    my_moveit2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            join(get_package_share_directory('my_moveit2'), 'launch', 'launch.py')  # 这里的 launch.py 需要是你的 my_moveit2 包中的启动文件
        )
    )
    
    # 包含 assistant 包中的 demo.launch.py 文件
    assistant_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            join(get_package_share_directory('assistant'), 'launch', 'demo.launch.py')  # 这里的 demo.launch.py 需要是你的 assistant 包中的启动文件
        )
    )

    return LaunchDescription([
        my_moveit2_launch,
        assistant_launch  # 这里我们使用 assistant_launch
    ])
