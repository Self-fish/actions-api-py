from flask import request
from flask_restful import Resource

from domain.model.Action import Action
from domain.model.ActionStep import ActionStep
from domain.model.ActionType import ActionType
from domain.usecase import PublishActionUseCase


class ActionsController(Resource):

    def post(self):
        body = request.json
        action = Action(ActionType[body['action']], ActionStep[body['step']])
        PublishActionUseCase.publish(action)

