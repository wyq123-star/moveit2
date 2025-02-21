from setuptools import find_packages, setup

package_name = 'my_moveit2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/launch.py']),  # 注册 launch 文件夹
        ('share/' + package_name + '/urdf', ['urdf/panda.urdf']),  # 注册 urdf 文件夹
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wyq',
    maintainer_email='3186831775@qq.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'demo_moveit_node = my_moveit2.demo_moveit_node:main',  # 正确注册节点
        ],
    },
)
