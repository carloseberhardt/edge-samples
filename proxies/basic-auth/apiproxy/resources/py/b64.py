import base64

base64string = flow.getVariable("basicAuth")

try:
  up = base64.b64decode(base64string).split(':')
  flow.setVariable("username", up[0])
  flow.setVariable("password", up[1])
except:
  flow.setVariable("username", 'terrible')
  flow.setVariable("password", 'error handling')