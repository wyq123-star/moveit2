import rclpy
from moveit_commander import RobotCommander, PlanningSceneInterface, MoveGroupCommander
from geometry_msgs.msg import Pose

def move_arm():
    # 初始化 ROS 2 节点
    rclpy.init()

    # 初始化 MoveIt Commander
    moveit_commander.roscpp_initialize([])

    # 创建接口对象
    robot_commander = RobotCommander()
    scene_interface = PlanningSceneInterface()
    move_group = MoveGroupCommander("arm")  # "arm" 是你在配置时定义的组名

    # 设置目标位置
    target_pose = Pose()
    target_pose.orientation.w = 1.0  # 目标姿态
    target_pose.position.x = 0.4     # 目标位置
    target_pose.position.y = 0.0
    target_pose.position.z = 0.4

    # 设置目标位置
    move_group.set_pose_target(target_pose)

    # 开始规划并执行
    success, plan = move_group.go(wait=True)

    if success:
        print("Planning successful, executing...")
    else:
        print("Planning failed")

    # 关闭 MoveIt 相关资源
    moveit_commander.roscpp_shutdown()

    rclpy.shutdown()

if __name__ == "__main__":
    move_arm()