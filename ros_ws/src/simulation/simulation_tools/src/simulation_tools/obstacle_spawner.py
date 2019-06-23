import rospy
from simulation_tools.srv import SpawnSingleStaticObstacle


def spawn_single_static_obstacle(req):


rospy.init_node('obstacle_spawner')
single_obstacle_srv = rospy.Service(
    'spawn_single_static_obstacle', SpawnSingleStaticObstacle, spawn_single_static_obstacle)

rospy.spin()
