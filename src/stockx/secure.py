import traceback


def secure_call():
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as error:
                return {"error": error, "trackback": traceback.format_exc()}

        return wrapper

    return decorator
