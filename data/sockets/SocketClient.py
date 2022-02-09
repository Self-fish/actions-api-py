from data.sockets import SocketFactory
from domain.model.ActionStep import ActionStep
from domain.model.ActionType import ActionType


def send_message(step: ActionStep, type: ActionType):
    socket = SocketFactory.get_socket(type)
    try:
        message = bytes(step.name, 'utf-8')
        print(message)
        socket.sendall(message)
    except Exception:
        print("Something went wrong")
