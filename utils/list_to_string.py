def format_list_to_string(data):
    if isinstance(data, list):
        return ", ".join(data)
    return data if data else ""

def format_list_for_forms(data):
    if isinstance(data, list):
        return "\n\n".join(data)
    return data if data else ""