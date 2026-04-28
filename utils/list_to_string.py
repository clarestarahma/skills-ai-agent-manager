def format_list_to_string(data):
    if isinstance(data, list):
        return ", ".join(data)
    return data if data else ""