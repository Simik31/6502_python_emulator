# ######################################
#  Copyright (c) 2021                  #
#                                      #
#  Author: Martin Šimara               #
#  Last modified on 30/01/2021, 22:07  #
# ######################################

def test_instance(method, parameter: any, expected_types: tuple, parameter_offset: int = 1) -> None:
    if type(parameter) not in expected_types and not issubclass(type(parameter), expected_types):
        c_name = method.__module__
        m_name = method.__name__
        p_name = method.__code__.co_varnames[parameter_offset]
        p_type = str(type(parameter)).split("\'")[1]
        raise ValueError(f"{c_name}.{m_name}() parameter '{p_name}' does not support type '{p_type}'")
