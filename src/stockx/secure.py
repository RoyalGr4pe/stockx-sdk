import inspect
import traceback
import functools


def secure_call():
    def decorator(func):
        if inspect.iscoroutinefunction(func):

            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                try:
                    return await func(*args, **kwargs)
                except Exception as error:
                    return {"error": str(error), "traceback": traceback.format_exc()}

            return async_wrapper
        else:

            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    return {"error": str(error), "traceback": traceback.format_exc()}

            return sync_wrapper

    return decorator
