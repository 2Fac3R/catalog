"""Util functions: current_user"""

# Django
import inspect


def current_user():
    """ Returns Current User """
    for frame_record in inspect.stack():
        if frame_record[3] == 'get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None
    return request.user
