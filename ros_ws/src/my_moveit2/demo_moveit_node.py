import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

class PandaTrajectoryPublisher(Node):
    def __init__(self):
        super().__init__('panda_trajectory_publisher')
        # 发布到 /follow_joint_trajectory 这个 topic
        self.publisher = self.create_publisher(JointTrajectory, '/follow_joint_trajectory', 10)
        self.timer = self.create_timer(1.0, self.publish_trajectory)
    
    def publish_trajectory(self):
        traj_msg = JointTrajectory()
        traj_msg.header.stamp = self.get_clock().now().to_msg()
        # 这里使用了 URDF 中定义的机械臂关节名称（panda_joint1 ~ panda_joint7）
        traj_msg.joint_names = [
            'panda_joint1',
            'panda_joint2',
            'panda_joint3',
            'panda_joint4',
            'panda_joint5',
            'panda_joint6',
            'panda_joint7'
        ]
        point = JointTrajectoryPoint()
        # 示例：设定目标关节角度，需根据你的运动学模型调整
        point.positions = [0.0, 0.5, 0.0, -0.5, 0.0, 0.5, 0.0]
        point.time_from_start.sec = 5  # 期望 5 秒内完成运动
        traj_msg.points.append(point)
        
        self.publisher.publish(traj_msg)
        self.get_logger().info("已发布运动轨迹指令。")

def main(args=None):
    rclpy.init(args=args)
    node = PandaTrajectoryPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
