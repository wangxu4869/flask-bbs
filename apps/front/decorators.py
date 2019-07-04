from flask import session,redirect,url_for
from functools import wraps
import config


def login_required(func):
    @wraps(func)
    def inner(*args,**kwsrgs):
        if config.FRONT_USER_ID in session:
            return func(*args,**kwsrgs)
        else:
            return redirect(url_for('front.signin'))
    return inner