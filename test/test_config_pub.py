import rospy
import rostest
import unittest
from ros_concepts.config_pub import ConfigurableFloatPub

class TestConfigPub(unittest.TestCase):
    def test_get_float(self):
        
        cfp =  ConfigurableFloatPub()
        f = cfp.get_float()
        self.assertTrue(isinstance(f, float))
        self.assertGreaterEqual(f, cfp.min_)
        self.assertLessEqual(f, cfp.max_)

    def test_success(self):
        self.assertEquals(1, 1)



if __name__ == '__main__':
    rospy.init_node("test_node")
    rostest.rosrun("ros_concepts", 'test_config_pub', TestConfigPub)