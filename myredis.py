import redis


class RedisQueue:
    """Simple Queue with Redis Backend"""
    def __init__(self, name, namespace='queue', **redis_kwargs):
        """The default connection parameters are: host='localhost', port=6379, db=0"""
        self.__db = redis.Redis(**redis_kwargs)
        self.key = f"{namespace}: {name}"
        self.finished = False


    def put(self, item):
        """Put item into the queue."""
        self.__db.rpush(self.key, item)

    def get(self):
        """Remove and return an item from the queue.
        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        return self.__db.lpop(self.key)


