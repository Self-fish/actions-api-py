import socket

from domain.model.ActionType import ActionType


def get_socket(type: ActionType):
    action_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_address = None
    if type == ActionType.CLEAN_AQUARIUM:
        socket_address = ('localhost', 2000)
    elif type == ActionType.LIGHT_CONTROL:
        socket_address = ('localhost', 2001)
    action_socket.connect(socket_address)
    return action_socket
