import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

class VideoProcessor:
  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/image_raw", Image, self.callback)

  # Transformando ROS img para formato 
  def callback(self, data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
      
    # Descolorindo
    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    cv2.imshow("Edges", edges)
    cv2.waitKey(1)

if __name__ == '__main__':
  rospy.init_node('video_processor')
  vp = VideoProcessor()
  rospy.spin()
