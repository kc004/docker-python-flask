from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return '@@@@@_APP2_@@@@@\nHello This is APP2! I have been seen %s times.\n' % redis.get('hits').decode('utf-8')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
