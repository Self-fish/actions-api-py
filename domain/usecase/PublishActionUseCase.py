from data.repository.ActionsRepository import ActionsRepository
from domain.model.Action import Action


class PublishActionUseCase:

    def __init__(self, repository: ActionsRepository):
        self.__repository: ActionsRepository = repository

    def publish(self, action: Action):
        self.__repository.process_action(action)

