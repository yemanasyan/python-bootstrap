import queue
import socket
import struct
import threading
from time import sleep


class ListNode:

    def __init__(self, value: int = None, next: 'ListNode' = None):
        self.value = value
        self.next = next


class NumbersAccumulation:

    def __init__(self):
        self.first_number_pointer = None
        self.stream_pointers = dict()
        # queue.Queue is thread safe
        self.input_data_queue = queue.Queue()
        self.finish_accumulation = False

    def accumulate(self, host_name: str, port_number: int, stream_count: int) -> list:
        accumulation_thread = self._start_accumulation_thread()
        self._start_server(host_name, port_number, stream_count)
        self.finish_accumulation = True
        accumulation_thread.join()
        sorted_numbers = self._get_numbers_list(self.first_number_pointer)
        return sorted_numbers

    def _start_server(self, host: str, port: int, max_stream_count: int):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        # specifies max client sockets count that can be queued to be accepted
        # this doesn't mean that maximum max_stream_count connections with clients will be made
        server_socket.listen(max_stream_count)
        print(f"Server listening on {host}:{port}")

        client_threads = list()
        # to accept max_stream_count connections and stop
        for stream_index in range(max_stream_count):
            client_socket, address = server_socket.accept()
            print(f"Accepted connection from {address[0]}:{address[1]}")

            client_thread = threading.Thread(target=self._handle_client, args=(client_socket,))
            client_thread.start()
            client_threads.append(client_thread)

        for client_thread in client_threads:
            client_thread.join()

        server_socket.close()

    def _start_accumulation_thread(self) -> threading.Thread:
        accumulation_thread = threading.Thread(target=self._accumulation_values)
        accumulation_thread.start()

        return accumulation_thread

    def _accumulation_values(self):
        while not self.finish_accumulation or not self.input_data_queue.empty():
            if self.input_data_queue.empty():
                continue

            stream, number = self.input_data_queue.get()
            if self.first_number_pointer is None:
                self.first_number_pointer = ListNode(number)
                self.stream_pointers[stream] = self.first_number_pointer
                continue

            if number < self.first_number_pointer.value:
                self.first_number_pointer = ListNode(number, self.first_number_pointer)
                self.stream_pointers[stream] = self.first_number_pointer
                continue

            last_pointer = self.stream_pointers[stream] if stream in self.stream_pointers else self.first_number_pointer

            while last_pointer.next is not None and last_pointer.next.value <= number:
                last_pointer = last_pointer.next

            next_element = last_pointer.next
            current_element = ListNode(number, next_element)
            last_pointer.next = current_element
            self.stream_pointers[stream] = current_element

    def _handle_client(self, client_socket: socket.socket):
        while True:
            try:
                data = client_socket.recv(8)
            except socket.error:
                return

            if not data:
                print("Socket is closed")
                return

            stream, number = struct.unpack('ii', data)
            self.input_data_queue.put((stream, number))

    @staticmethod
    def _get_numbers_list(list_node: ListNode) -> list:
        sorted_list = list()
        while list_node is not None:
            sorted_list.append(list_node.value)
            list_node = list_node.next

        return sorted_list


def main():
    numbers_accumulation = NumbersAccumulation()
    sorted_numbers = numbers_accumulation.accumulate('localhost', 12345, 5)
    print(f"Numbers: {sorted_numbers}")


if __name__ == "__main__":
    main()
