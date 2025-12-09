from setuptools import find_packages, setup

package_name = 'practica_0'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools','velocidad_msgs'],
    zip_safe=True,
    maintainer='rocioromero',
    maintainer_email='rocioromero@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'velocidad_pub_node = scripts.velocidad_pub_node:main',
            'velocidad_pub_sub_node = scripts.velocidad_pub_sub_node:main'
        ],
    },
)
