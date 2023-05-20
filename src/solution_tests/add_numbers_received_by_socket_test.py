import unittest
import socket
import struct
from time import sleep


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_add_numbers_received_by_socket():
        test_data = [
            (1, [200, 200, 201, 3000, 4000]),
            (2, [2001, 2002, 2003, 10000, 100001]),
            (3, [10]),
            (2, [400001]),
            (3, [4002])
        ]

        # Define the server address and port
        server_address = ('localhost', 12345)
        sockets = list()

        for stream, numbers in test_data:
            add_numbers_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connect to the server
            add_numbers_socket.connect(server_address)
            sockets.append(add_numbers_socket)

            for number in numbers:
                data = struct.pack('ii', stream, number)
                add_numbers_socket.sendall(data)

        sleep(10)
        for add_numbers_socket in sockets:
            add_numbers_socket.close()



if __name__ == '__main__':
    unittest.main()
