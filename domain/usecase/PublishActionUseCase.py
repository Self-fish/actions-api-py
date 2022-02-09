from data.repository import ActionsRepository
from domain.model.Action import Action


def publish(action: Action):
    ActionsRepository.process_action(action)

