import rclpy
from rclpy.node import Node
from moveit_commander import RobotCommander, PlanningSceneInterface, MoveGroupCommander
from geometry_msgs.msg import Pose

class MoveItDemo(Node):
    def __init__(self):
        super().__init__('moveit_demo')

        # 初始化 MoveGroupCommander（MoveIt 2接口）
        self.robot = RobotCommander()
        self.scene = PlanningSceneInterface()
        self.group_name = "arm"  # 你的运动组名称（根据你的MoveIt配置）
        self.move_group = MoveGroupCommander(self.group_name)

        # 设置目标位置（旋转）
        self.target_pose = Pose()
        self.target_pose.position.x = 0.3
        self.target_pose.position.y = 0.2
        self.target_pose.position.z = 0.5
        self.target_pose.orientation.w = 1.0

    def plan_and_execute(self):
        # 设置目标位姿
        self.move_group.set_pose_target(self.target_pose)

        # 规划并执行
        plan = self.move_group.plan()

        if plan and len(plan.joint_trajectory.points) > 0:
            # 执行规划
            self.move_group.go(wait=True)
            self.get_logger().info("Motion executed successfully!")
        else:
            self.get_logger().error("Planning failed!")
            return 1  # 这里确保 else 语句后面有正确的缩进

        return 0

def main(args=None):
    rclpy.init(args=args)
    node = MoveItDemo()

    try:
        # 规划并执行
        node.plan_and_execute()
        rclpy.spin(node)

    except Exception as e:
        node.get_logger().error(f"Error: {str(e)}")
        rclpy.shutdown()

if __name__ == '__main__':
    main()
