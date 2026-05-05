def get_list(content: str):
  if not content:
    return ""
  distinct = set(content.split('\n\n'))
  return list(distinct)