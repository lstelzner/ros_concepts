# ros_concepts #

## Build
clone repo into catkin workspace
```
catkin build
```

## Launch
There are three args, frequency, min, max, see below for an example
```
source (devel/install)/setup.bash
roslaunch ros_concepts float_pub.launch frequency:=5 min:=-5 max:=3
```

## Nodes
  - simple_node 

## Publishers
 float [std_msgs/Float64]- random float based off arg ~/min ~/max params

## Services
- enable_publish [std_srv/SetBool] - pass a True to enable, False to disable

## Params
- ~/frequncy
- ~/min
- ~/max

## Dynamic Reconfigure
- frequncy - rate at which to publish floats
- min - minimum value to generate the random value with
- max - maximum value to generate the random value with