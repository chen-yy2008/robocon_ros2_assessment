import rclpy
from rclpy.node import Node
from student_info_pkg.msg import StudentInfo
class StudentPublisher(Node):
    
    def __init__(self):
        super().__init__("student_publisher")

        self.publisher = self.create_publisher(StudentInfo,"student_info",10)

        self.timer = self.create_timer(1.0, self.time_callback)

    def time_callback(self):
                msg = StudentInfo()
                msg.student_id = "1433223"
                msg.student_name = "yuan ge"
                self.publisher.publish(msg)

def main():
       rclpy.init()

       node = StudentPublisher()
       
       rclpy.spin(node)