from dependency_injector import containers, providers

from data.repository.ActionsRepository import ActionsRepository
from data.sockets.SocketClient import SocketClient
from data.sockets.SocketFactory import SocketFactory
from domain.usecase.PublishActionUseCase import PublishActionUseCase


class ActionsApiContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    socket_factory = providers.Factory(SocketFactory)
    socket_client = providers.Factory(SocketClient, socket_factory)
    repository = providers.Factory(ActionsRepository, socket_client)
    use_case = providers.Factory(PublishActionUseCase, repository)

