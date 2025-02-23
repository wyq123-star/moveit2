# 寒假作业 moveit2 相关功能包的调用

## 项目描述
这是一个用于控制机器人手臂的 ROS 2 MoveIt 2 示例项目，使用 Docker 和 ROS 2 构建。

## 一.安装步骤

1. 克隆仓库：
    ```bash
    git clone https://github.com/wyq123-star/moveit2.git
    ```

2. 构建容器：
    ```bash
    cd .devcontainer
    docker compose build
    docker compose up
    ```
    

3. 打开另一个终端进入容器：
    ```bash
    docker exec -it moveit2-container bash
    ```

## 二.启动项目

```bash
colcon build
source /opt/ros/humble/setup.bash
source /ros_ws/install/setup.bash
ros2 launch my_moveit2 launch.py
```

### 目前只做到了配置urdf相关的文件以及编写发送运动指令的节点文件，后续还有控制器相关文件的完善

### PS:如果以后在容器里遇到rviz2或moveit2_setup_assistant等可视化软件打开报错，在本地目录运行以下代码：

```bash
xhost +local:docker
```

