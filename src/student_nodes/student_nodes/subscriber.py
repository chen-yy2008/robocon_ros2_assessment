import rclpy
from rclpy.node import Node
from student_info_pkg.msg import StudentInfo
class StudentSubscriber(Node):
    def __init__(self):
        super().__init__("student_subscriber")

        self.subscriber = self.create_subscription(StudentInfo,"student_info",self.listener_callback,10)

    def listener_callback(self,msg):
        self.get_logger().info(f"学号: {msg.student_id}, 姓名: {msg.student_name}")

def main():
    rclpy.init()

    node = StudentSubscriber()

    rclpy.spin(node)