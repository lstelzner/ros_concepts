import rospy
from ros_concepts.config_pub import ConfigurableFloatPub

def main():
    rospy.init_node("simple_node")
    rospy.loginfo("Starting node")
    cfp = ConfigurableFloatPub()
    cfp.run()
    rospy.spin()

if __name__ == "__main__":
    main()    

    