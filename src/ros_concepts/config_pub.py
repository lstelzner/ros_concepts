import rospy
import random
from std_msgs.msg import Float64
from std_srvs.srv import SetBool, SetBoolRequest, SetBoolResponse
from dynamic_reconfigure.server import Server
from ros_concepts.cfg import PublishSettingsConfig

class ConfigurableFloatPub:
    """
    class that will publish a random float on a topic
    Has a service to enable/disable publishing
    """
    def __init__(self, topic_name="float"):
        self.min_ = 0
        self.max_ = 10000.
        self.rate_ = rospy.Rate(rospy.get_param("pub_frequency"))
        self.pub_ = rospy.Publisher(topic_name, Float64, queue_size=10)
        self.enabled_ = True
        self.srv_server_ = rospy.Service('enable_publish', SetBool, self.enable_cb)
        self.dyn_server = Server(PublishSettingsConfig, self.dyn_reconfig_cb)

    def dyn_reconfig_cb(self, config, level):
        self.min_ = config.min
        self.max_ = config.max
        self.rate_ = rospy.Rate(config.frequency)
        self.enabled_ = config.enable
        return config

    def enable_cb(self, req):
        self.enabled_ = req.data
        resp = SetBoolResponse()
        resp.success = True
        if self.enabled_ :
            resp.message= "publishing enabled"
        else:
            resp.message = "publishing disabled"
        return resp

    def run(self):
        while not rospy.is_shutdown():
            if self.enabled_:
                f = Float64(self.get_float())
                self.pub_.publish(f)
            self.rate_.sleep()

    def get_float(self):
        #Could be improved upon with precise range
        return random.uniform(self.min_, self.max_)

        