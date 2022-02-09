from domain.model import ActionStep
from domain.model.ActionType import ActionType


class Action:

    def __init__(self, type: ActionType, step: ActionStep):
        self.type = type
        self.step = step

