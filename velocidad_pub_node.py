import rclpy
from rclpy.node import Node

from std_msgs.msg import Int64

class VelocidadPub(Node):

    def __init__(self):
        super().__init__("velocidad_pub_node")
           
        self.number_ = 1
        self.number_publisher_ = self.create_publisher(Int64, "velocidad_topic_pub",10)
        self.timer_ = self.create_timer(1.0, self.publish_number)
        self.get_logger().info("El nodo velocidad_pub_node esta activo")
        
    def publish_number(self):
        msg = Int64()
        msg.data = self.number_
        self.number_publisher_.publish(msg)
        self.number_ +=4
        
def main(args=None):
    rclpy.init(args=args)
    node = VelocidadPub()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()
        
        
