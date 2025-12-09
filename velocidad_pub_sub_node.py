import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64, Float64
import time

class VelocidadPubSub(Node):

    def __init__(self):
        super().__init__("velocidad_pub_sub_node")
           
        self.rad_pub_ = self.create_publisher(Float64, "velocidad_rad_topic",10)
        self.number_subscriber_ = self.create_subscription(Int64, "velocidad_topic_pub", self.callback_number, 10)
        self.t0 = time.time() 
        self.get_logger().info("El nodo velocidad_pub_sub_node esta activo")
        
        
        
    def callback_number(self,msg):
        rpm= msg.data
        rad_s=rpm*(2*3.141592)/60
        t_now = time.time() - self.t0
        out_msg = Float64()
        out_msg.data = rad_s
        self.rad_pub_.publish(out_msg)
        self.get_logger().info(f"t = {t_now:.2f} s, Velocidad recibida: {rpm} rpm, convertida:{rad_s:.2f} rad/s")
def main(args=None):
    rclpy.init(args=args)
    node = VelocidadPubSub()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
        
