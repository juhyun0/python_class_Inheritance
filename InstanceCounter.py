class InstanceConter:
    count=0
    def __init__(self):
        InstanceConter.count+=1

    @classmethod
    def print_instance_count(cls):
        print(cls.count)

if __name__=='__main__':
    a=InstanceConter()
    InstanceConter.print_instance_count()

    b=InstanceConter()
    InstanceConter.print_instance_count()

    c=InstanceConter()
    c.print_instance_count()