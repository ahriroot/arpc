

def default(type_str):
    """
    This function is a template to generate default value.
    """
    if type_str == "int" or type_str == "integer":
        return "0"
    elif type_str == "float" or type_str == "double":
        return "0.0"
    elif type_str == "bool" or type_str == "boolean":
        return "False"
    elif type_str == "str" or type_str == "string":
        return "\"\""
    elif type_str == "list" or type_str == "array":
        return "[]"
    elif type_str == "dict" or type_str == "json" or type_str == "object":
        return "{}"
    else:
        return "None"


def generate_param_class(class_name, attr_list):
    """
    This function is a template to generate Param class.
    """

    init_attr_str = "pass"

    attr_name_list = []
    for param in attr_list:
        if init_attr_str == "pass":
            init_attr_str = ""
        init_attr_str += f"\n        self.{param['name']} = {param['name']}"
        attr_name_list.append(f"{param['name']}={default(param['type'])}")

    template = f"""
class {class_name}(arpc.Param):
    \"\"\"
    This class is a Param class for arpc.
    \"\"\"
    def __init__(self, {', '.join(attr_name_list)}):{''.join(init_attr_str)}
"""
    return template
