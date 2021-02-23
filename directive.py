class directive:
  def __init__(self, key, **attributes):
    self.key = key
    self.attributes = attributes

  def __enter__(self):
    sep = " " if len(self.attributes) > 0 else ""
    print(f"{{% {self.key}{sep}{self.__attribute_list()} %}}")

  def __attribute_list(self):
    return " ".join(map(self.__attribute, self.attributes))

  def __attribute(self, key):
    value = _format_value(self.attributes[key])
    return f"{key}={value}"

  def __exit__(self, type, value, traceback):
    print(f"{{% end{self.key} %}}")


def _format_value(value):
  if isinstance(value, str):
    return f'"{value}"'
  elif isinstance(value, bool):
    return f"{value}".lower()
  elif value is None:
    return '""'
  else:
    return f"{value}"
