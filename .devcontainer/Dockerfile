# 使用官方 ROS 2 Humble 桌面版镜像
FROM osrf/ros:humble-desktop-full

# 安装基础工具
RUN apt-get update && apt-get install -y \
    git \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 创建工作空间
RUN mkdir -p /ros_ws/src
WORKDIR /ros_ws

# 设置默认 shell 为 bash
SHELL ["/bin/bash", "-c"]

# source ROS 环境
RUN source /opt/ros/humble/setup.bash && \
    rosdep update && \
    rosdep install -y --rosdistro humble --from-paths . --ignore-src

# 安装 MoveIt 2 相关依赖
RUN apt-get update && apt-get install -y \
    ros-humble-moveit-resources-panda-description \
    ros-humble-moveit \
    ros-humble-moveit-core \
    ros-humble-moveit-planners \
    ros-humble-moveit-ros-planning \
    ros-humble-moveit-ros-perception \
    ros-humble-moveit-ros-visualization \
    ros-humble-moveit-ros-move-group \
    ros-humble-moveit-ros-control-interface \
    ros-humble-moveit-ros-robot-interaction \
    ros-humble-moveit-setup-assistant \
    ros-humble-controller-manager \
    && rm -rf /var/lib/apt/lists/*

# 安装缺少的 Python 依赖
RUN apt-get update && apt-get install -y python3-ament-package

# 构建 ROS 2 工作空间
RUN source /opt/ros/humble/setup.bash && colcon build --symlink-install

# 运行 bash 交互式 shell
CMD ["bash"]
