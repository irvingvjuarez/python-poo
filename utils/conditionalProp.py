def conditionalProp(dict, target, default):
  if target in dict:
    return dict[target]
  else:
    return default