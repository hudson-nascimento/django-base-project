import os
import ast
import environ


def env(get, default=None, type=True):
    _env = environ.Env()
    try:
        if type:
            return ast.literal_eval(_env(get))
        return _env(get)
    except Exception as e:
        try:
            if type:
                return ast.literal_eval(os.environ.get(get, default))
            return os.environ.get(get, default)
        except Exception as e:
            return default


def get_hostname():
    env_name = env('DOMAIN', 'http://localhost:8000', False)
    return env_name
