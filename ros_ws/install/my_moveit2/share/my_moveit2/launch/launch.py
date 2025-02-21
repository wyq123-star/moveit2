from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from os.path import join

def generate_launch_description():
    try:
        urdf_config_launch_path = join(get_package_share_directory('urdf_config'), 'launch', 'demo.launch.py')

        urdf_config_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(urdf_config_launch_path)
        )

        return LaunchDescription([
            urdf_config_launch
        ])

    except Exception as e:
        print(f"错误: 无法找到 urdf_config 包的 demo_launch.py 文件, 请检查 urdf_config 是否正确安装. 详细错误: {e}")
        return LaunchDescription([])
