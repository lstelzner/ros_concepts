import rospy
import rostest
import unittest
from std_srvs.srv import SetBool, SetBoolRequest, SetBoolResponse
from ros_concepts.config_pub import ConfigurableFloatPub


""" TODO  break into multiple tests, need to solve ros getting angry about redefining services/topics with 
multiple test functions
"""

class TestConfigPub(unittest.TestCase):
    def test_get_float(self):
        
        cfp =  ConfigurableFloatPub()
        #test get float
        f = cfp.get_float()
        self.assertTrue(isinstance(f, float))
        self.assertGreaterEqual(f, cfp.min_)
        self.assertLessEqual(f, cfp.max_)
        
        #test disable
       
        enable= rospy.ServiceProxy('enable_publish', SetBool)
        resp = enable(False)
        self.assertTrue(resp.success)
        self.assertFalse(cfp.enabled_)
        #test enable
        resp = enable(True)
        self.assertTrue(resp.success)
        self.assertTrue(cfp.enabled_)
    
    


if __name__ == '__main__':
    rospy.init_node("test_node")
    rostest.rosrun("ros_concepts", 'test_config_pub', TestConfigPub)