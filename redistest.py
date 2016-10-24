import redis
from threading import Thread
import tornado.ioloop
from tornado.web import Application, RequestHandler
from tornado.websocket import WebSocketHandler
from tornado.queues import Queue
import tornado.gen

q = Queue()


class ChatHandler(WebSocketHandler):
    clients = set()

    def open(self, *args, **kwargs):
        ChatHandler.clients.add(self)
        print('Add client')

    def on_close(self):
        ChatHandler.clients.remove(self)

    @classmethod
    def send_message(cls, message):
        print(len(cls.clients))
        for client in cls.clients:
            client.write_message(message)


class MainHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

    def post(self):
        ChatHandler.send_message('POST')
        self.write('OK')
        self.finish()


class RedisListener(Thread):
    def __init__(self, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)

        # Setup the Redis connection
        self.connection_pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
        self.client = redis.Redis(connection_pool=self.connection_pool)
        self.pubsub = self.client.pubsub()

        # Who subscribes to what, and vice-versa
        # self.channel_subscribers = defaultdict(set)
        # self.client_channels = defaultdict(set)

    def run(self):
        self.pubsub.subscribe('commands')
        for event in self.pubsub.listen():
            data = event['data']
            print('Put Queue %s' % data)
            q.put(data)


@tornado.gen.coroutine
def listen_redis():
    while True:
        msg = yield q.get()
        try:
            print('Get Queue %s' % msg)
            ChatHandler.send_message(msg)
        finally:
            q.task_done()


r = RedisListener()
r.start()
app = Application([
    (r'/', MainHandler),
    (r'/ws', ChatHandler)
])
app.listen(8080)
tornado.ioloop.IOLoop.instance().spawn_callback(listen_redis)
tornado.ioloop.IOLoop.instance().start()
