#include <rclcpp/rclcpp.hpp>
#include <moveit_commander/robot_trajectory.h>
#include <moveit_commander/planning_scene_interface.h>
#include <moveit_commander/move_group_interface.h>
#include <moveit_commander/robot_trajectory.h>
#include <moveit_commander/planning_scene_interface.h>
#include <moveit_commander/move_group_interface.h>
#include <geometry_msgs/msg/pose.hpp>

class MoveArmNode : public rclcpp::Node
{
public:
    MoveArmNode() : Node("move_arm_node")
    {
        // 初始化 MoveIt
        moveit_commander::MoveGroupInterface move_group("arm"); // "arm" 是你在配置时定义的组名
        move_group.setPlannerId("RRTConnectkConfigDefault");  // 选择规划算法

        // 设置目标位置
        geometry_msgs::msg::Pose target_pose;
        target_pose.orientation.w = 1.0;  // 目标姿态
        target_pose.position.x = 0.4;     // 目标位置
        target_pose.position.y = 0.0;
        target_pose.position.z = 0.4;

        move_group.setPoseTarget(target_pose);

        // 开始规划并执行
        moveit_commander::MoveGroupInterface::Plan my_plan;
        bool success = (move_group.plan(my_plan) == moveit_commander::MoveItErrorCode::SUCCESS);
        if (success)
        {
            RCLCPP_INFO(this->get_logger(), "Planning successful, executing...");
            move_group.execute(my_plan);
        }
        else
        {
            RCLCPP_ERROR(this->get_logger(), "Planning failed");
        }
    }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MoveArmNode>());
    rclcpp::shutdown();
    return 0;
}
