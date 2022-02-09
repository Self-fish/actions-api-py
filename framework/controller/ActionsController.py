from flask import request
from flask_restful import Resource

from domain.model.Action import Action
from domain.model.ActionStep import ActionStep
from domain.model.ActionType import ActionType
from domain.usecase.PublishActionUseCase import PublishActionUseCase


class ActionsController(Resource):

    def __init__(self, use_case: PublishActionUseCase):
        self.__use_case: PublishActionUseCase = use_case

    def post(self):
        body = request.json
        action = Action(ActionType[body['action']], ActionStep[body['step']])
        self.__use_case.publish(action)

