from data.sockets.SocketClient import SocketClient
from domain.model.Action import Action


class ActionsRepository:

    def __init__(self, socket_client):
        self.__socket_client: SocketClient = socket_client

    def process_action(self, action: Action):
        self.__socket_client.send_message(action.step, action.type)
