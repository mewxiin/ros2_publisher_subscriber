from setuptools import find_packages, setup

package_name = 'ros2_publisher_subscriber'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mewxiin',
    maintainer_email='mewxiin@gmail.com',
    description='A ROS 2 messaging system implementing a Publisher-Subscriber architecture.',
    license='',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = ros2_publisher_subscriber.publisher:main',
            'subscriber = ros2_publisher_subscriber.subscriber:main',
        ],
    },
)