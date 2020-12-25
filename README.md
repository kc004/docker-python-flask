# docker-python-flask

This is project includes flask web app and redis. 

### Prerequisites


```
python, flask, redis and docker
```

### Deployment

Clone the source locally:

```
$ https://github.com/kc004/docker-python-flask.git
$ cd docker-python-flask
```

Now, execute following command to run full application.
```
$ docker-compose up
```
It will run 2 web app container and redis container.

### Testing
web apps are running on 5000 and 5001 port.
```
$ curl localhost:5000
$ curl localhost:5001
```
Each request will increase the redis request counter.
You will get output like this
```
#####_APP1_#####
Hello This is APP1! I have been seen 2 times.
```
