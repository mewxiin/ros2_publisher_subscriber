# ros2_publisher_subscriber
Basic ROS 2 publisher and subscriber communication using Python.

## Features
- Publisher node sending messages
- Subscriber node receiving messages

## Prerequisites
- Ubuntu 24.04 (or compatible Linux distro)
- ROS 2 Kilted Kaiju
- Python 3.12+

## Installation
1. Creating a workspace:
  ``` Bash
  mkdir -p ~/ros2_ws/src
  cd ~/ros2_ws/src
  ```
2. Cloning the Repository:
  ``` Bash
  git clone https://github.com/mewxiin/ros2_publisher_subscriber/
  ```
3. Building the package
  ``` Bash
  cd ~/ros2_ws
  colcon build
  ```
4. Running the system
   Terminal 1:
  ``` Bash
  source install/setup.bash
  ros2 run ros2_publisher_subscriber publisher
  ```
  Terminal 2:
  ``` Bash
  cd ~/ros2_ws
  source install/setup.bash
  ros2 run ros2_publisher_subscriber subscriber
  ```
