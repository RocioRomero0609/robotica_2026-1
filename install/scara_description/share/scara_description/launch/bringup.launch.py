from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    pkg_share = get_package_share_directory('scara_description')

    # Generar la descripción del robot a partir del xacro
    robot_description = Command([
        FindExecutable(name='xacro'), ' ',
        PathJoinSubstitution([
            FindPackageShare('scara_description'),
            'urdf',
            'scara_urdf.xacro'
        ])
    ])

    # Publicar URDF (para RViz y TF)
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description,
                     'use_sim_time': True}],
        output='screen'
    )

    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher'
    )

    # Lanzar Gazebo (ros_gz_sim) con tu mundo SDF
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            ])
        ]),
        launch_arguments={
            # aquí pasamos la ruta al mundo de tu paquete
            'gz_args': PathJoinSubstitution([
                FindPackageShare('scara_description'),
                'worlds',
                'scara_world.sdf'
            ])
        }.items()
    )

    # Spawnear el URDF en Gazebo
    spawn_scara = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'scara',
            '-param', 'robot_description',
            '-z', '0.1',
            '-world', 'default'   # nombre del <world> en scara_world.sdf
        ],
        output='screen'
    )

    # RViz
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=[
            '-d',
            PathJoinSubstitution([
                FindPackageShare('scara_description'),
                'rviz',
                'scara.rviz'
            ])
        ],
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher,
        joint_state_publisher,
        gz_sim,
        spawn_scara,
        rviz
    ])

