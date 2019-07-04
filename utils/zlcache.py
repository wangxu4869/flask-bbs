import memcache

cache=memcache.Client(['127.0.0.1:11211'],debug=True)

def set(key,vaule,timeout=60):
    #封装的好处：以后再添加代码可以直接在此处添加一次即可，不用再视图函数中写cache连接参数
    return cache.set(key,vaule,timeout)

def get(key):
    return cache.get(key)

def delete(key):
    return cache.delete(key)