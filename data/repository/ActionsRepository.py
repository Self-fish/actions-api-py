from data.sockets import SocketClient
from domain.model.Action import Action


def process_action(action: Action):
    SocketClient.send_message(action.step, action.type)
