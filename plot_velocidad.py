import rclpy 
from rclpy.node import Node
from std_msgs.msg import Int64, Float64
import matplotlib.pyplot as plt
import time 
class PlotVelocidad(Node):
      
   def __init__(self):
        super().__init__("plot_velocidad_node")
        #topico de rpm
        self.sub_rpm = self.create_subscription(Int64, "/velocidad_topic_pub", self.callback_rpm, 10)
        #topico de rad/s 
        self.sub_rad = self.create_subscription(Int64, "/velocidad_rad_topic", self.callback_rad, 10)
        self.get_logger().info("El nodo plot_velocidad_node esta activo")
        
        self.t_list = []
        self.rpm_list = []
        self.rad_list =[]
        self.t0 = time.time()
        self.last_rpm = 0.0
   def callback_rpm(self,msg):
        self.last_rpm = msg.data
   def callback_rad(self,msg):
        rad_s=msg.data
        t_now= time.time() - self.t0
        self.t_list.append= (t_now)
        self.rpm_list.append(self.last_rpm)
        self.rad_list.append(rad_s)
        self.get_logger().info(f"t={t_now:.2f} s, Velocidad recibida: {self.last_rpm} rpm, convertida:{rad_s:.2f} rad/s")
def main(args=None):
    rclpy.init(args=args)
    node = PlotVelocidad()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    #Grafica rad/s vs tiempo
    plt.figure()
    plt.plot(node.t_list, node.rad_list)
    plt.xlabel('Tiempo [s]')
    plt.ylabel('rad/s')
    plt.title('Velocidad en rad/s vs tiempo')
    plt.grid(True)
    plt.xlim(0,30)
    plt.ylim(0,1000)
    
    #Grafica rpm vs tiempo
    plt.figure()
    plt.plot(node.t_list, node.rpm_list)
    plt.xlabel('Tiempo [s]')
    plt.ylabel('rpm')
    plt.title('Velocidad en rpm vs tiempo')
    plt.grid(True)
    plt.xlim(0,30)
    plt.ylim(0,1000)
    plt.show()
    node.destroy_node()
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
        
