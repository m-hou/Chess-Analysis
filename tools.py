import time
from functools import update_wrapper

def decorator(d):
    """doc"""
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

decorator = decorator(decorator)

@decorator
def timedcall(f):
    def timedcall_f(*arg, **kw):
        """doc"""
        start = time.time()
        res = f(*arg, **kw)
        end = time.time()
        print("%s took %fs to execute." % (f.__name__, end - start))
        return res
    return timedcall_f
