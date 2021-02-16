import re


def parameters_directive_key(parameter_type):
  if parameter_type == 'header':
    suffix = 'headers'
  else:
    suffix = f'{_dashcase(parameter_type)}-parameters'

  return f'api-method-{suffix}'


def _dashcase(string):
  return re.sub(r'(?<!^)(?=[A-Z])', '-', string).lower()
