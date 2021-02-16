#!/usr/bin/env python3

import sys
import json

from directive import *
from helpers import *


DEFAULT_PARAMETER_TYPE = 'object'
DEFAULT_HTTP_CODE = 200


if len(sys.argv) != 2:
  print(f'usage: {sys.argv[0]} swagger.json')
  exit(1)

with open(sys.argv[1]) as file:
  data = json.load(file)

  for path, endpoints in data['paths'].items():
    for method, endpoint in endpoints.items():
      host = data["schemes"][0] + '://' + data["host"]
      full_path = data['basePath'] + path

      with directive('api-method', method = method, host = host, path = full_path):
        with directive('api-method-summary'):
          print(endpoint['summary'])

        with directive('api-method-description'):
          print(endpoint['description'])

        with directive('api-method-spec'):
          with directive('api-method-request'):
            for type in ['path', 'header', 'query', 'formData', 'body']:
              parameters = [p for p in endpoint['parameters'] if p['in'] == type]

              if len(parameters) == 0: continue

              with directive(parameters_directive_key(type)):
                for parameter in parameters:
                  schema_type = parameter.get('schema', {}).get('type')
                  default_type = DEFAULT_PARAMETER_TYPE

                  attributes = {
                    'name': parameter['name'],
                    'type': parameter.get('type', schema_type or default_type),
                    'required': parameter['required']
                  }

                  with directive('api-method-parameter', **attributes):
                    if 'description' in parameter:
                      print(parameter['description'])

          with directive('api-method-response'):
            for key, response in endpoint['responses'].items():
              try:
                code = int(key)
              except ValueError:
                code = DEFAULT_HTTP_CODE

              with directive('api-method-response-example', httpCode = code):
                with directive('api-method-response-example-description'):
                  print(response['description'])
