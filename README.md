# Actions API
The purpose of this API is to provide a way to send remote actions to the aquarium by exposing a rest service that is able to receive an Action:

```python
def post(self):
  body = request.json
  action = Action(ActionType[body[ACTION]], ActionStep[body[STEP]])
  self.__use_case.publish(action)
  return request.json
```

## Action
The Action is composed by ActionType and Steps

```python
def __init__(self, type: ActionType, step: ActionStep):
  self.type = type
  self.step = step
```

in which the ActionType supported are CLEAN_AQUARIUM ad LIGHT_CONTROL

```python
class ActionType(Enum):
  CLEAN_AQUARIUM = 1
  LIGHT_CONTROL = 2
```

and a set of ActionSteps

```python
class ActionStep(Enum):
  COVER_UP = 1
  COVER_DOWN = 2
  LIGHTS_ON = 3
  LIGHTS_OFF = 4
  FILLING_BOMB_ON = 5
  FILLING_BOMB_OFF = 6
  EMPTY_BOMB_ON = 7
  EMPTY_BOMB_OFF = 8
```

This means that actually we allow two types of actions you can control remotely as follow: 

### Clean Aquarium
By sending a CLEAN_AQUARIUM ActionType, we allow the following ActionSteps: 
* **COVER_UP**: it allows to rise the aquarium cover for cleaning purposes.
* **COVER_DOWN**: it allows to lower the aquarium cover to the defualt position. 
* **EMPTY_BOMB_ON**: it allows to start the bomb that empty the aquarium.
* **EMPTY_BOMB_OFF**: it allows to stop the bomb that empty the aquarium. 
* **FILLING_BOMB_ON**: it allows to start the bomb that fill the aquarium with clean water. 
* **FILLING_BOMB_OFF**: it allows to stop the bomb that fill the aquarium. 

### Control Lights
By sending a CONTROL_LIGHTS ActionType, we allow the following ActionSteps: 
* **LIGHTS_ON**: turn on the lights and set the preferences to a manual mode with the lightts to ON. 
* **LIGHTS_OF**: turn off the lights and set the preferences to a manual mode with the lightts to OFF.

## Action 

When we receive the remote action, we send via socket the message to the [light-control](https://github.com/Self-fish/light-control) and [clean-control](https://github.com/Self-fish/clean-control) in order to handle it accordly

```python
def send_message(self, step: ActionStep, type: ActionType):
  socket = self.__socket_factory.get_socket(type)
    try:
      message = bytes(step.name, 'utf-8')
      socket.sendall(message)
    except Exception:
      socket.close()
```
   
