from data.sockets.SocketFactory import SocketFactory
from domain.model.ActionStep import ActionStep
from domain.model.ActionType import ActionType


class SocketClient:

    def __init__(self, socket_factory: SocketFactory):
        self.__socket_factory: SocketFactory = socket_factory

    def send_message(self, step: ActionStep, type: ActionType):
        socket = self.__socket_factory.get_socket(type)
        try:
            message = bytes(step.name, 'utf-8')
            print(message)
            socket.sendall(message)
        except Exception:
            print("Something went wrong")
            socket.close()

