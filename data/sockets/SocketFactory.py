import socket

from domain.model.ActionType import ActionType

LIGHT_SOCKET = 2001
CLEAN_SOCKET = 2000


class SocketFactory:

    def __init__(self):
        self.__light_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__light_socket.connect(('localhost', LIGHT_SOCKET))
        self.__clean_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__clean_socket.connect(('localhost', CLEAN_SOCKET))

    def get_socket(self, type: ActionType):
        if type == ActionType.CLEAN_AQUARIUM:
            return self.__clean_socket
        elif type == ActionType.LIGHT_CONTROL:
            return self.__light_socket
