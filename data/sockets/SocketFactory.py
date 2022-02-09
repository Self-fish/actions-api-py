import socket

from domain.model.ActionType import ActionType


class SocketFactory:

    def __init__(self):
        self.__light_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__light_socket.connect(('localhost', 2001))
        self.__clean_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__clean_socket.connect(('localhost', 2000))

    def get_socket(self, type: ActionType):
        if type == ActionType.CLEAN_AQUARIUM:
            print("Return clean socket")
            return self.__clean_socket
        elif type == ActionType.LIGHT_CONTROL:
            print("Return lights socket")
            return self.__light_socket
