import re


def parameters_directive_key(parameter_type):
  if parameter_type == 'header':
    suffix = 'headers'
  else:
    suffix = f'{_underscore(parameter_type)}-parameters'

  return f'api-method-{suffix}'


def _underscore(value):
  return re.sub(r'(?<!^)(?=[A-Z])', '_', value).lower()
