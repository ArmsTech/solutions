# Median Microservice

Design and implement a Median Microservice.

### Assumptions

This problem is open-ended so there are too many assumptions to list, however 
the primary assumption made is that historical (older than a minute) integer 
data is not relevant for this API and thus can be disregarded.

### Requirements

* Linux or other Unix-like OS
* Python development libraries
* Redis server
* RabbitMQ server
* Pip
* Virtualenv

### Configuration

All app configuration is accomplished by environmental variables. See .env.

### Install (e.g. Ubuntu)

```console
sudo apt-get install python-dev redis-server rabbitmq-server python-pip && sudo pip install virtualenv
virtualenv venv && . venv/bin/activate
make install
make microservice
```

### Testing

```console
make test
```

### Usage Example

```console
brenj$ http --form POST http://127.0.0.1:8000/put integer=2
HTTP/1.1 201 Created
Connection: close
Date: Sun, 13 Mar 2016 23:51:30 GMT
Server: gunicorn/19.4.5
content-length: 0

brenj$ http --form POST http://127.0.0.1:8000/put integer=3
HTTP/1.1 201 Created
Connection: close
Date: Sun, 13 Mar 2016 23:51:33 GMT
Server: gunicorn/19.4.5
content-length: 0

brenj$ http --form POST http://127.0.0.1:8000/put integer=1
HTTP/1.1 201 Created
Connection: close
Date: Sun, 13 Mar 2016 23:51:36 GMT
Server: gunicorn/19.4.5
content-length: 0

brenj$ http GET http://127.0.0.1:8000/median
HTTP/1.1 200 OK
Connection: close
Date: Sun, 13 Mar 2016 23:51:43 GMT
Server: gunicorn/19.4.5
content-length: 65
content-type: application/json; charset=utf-8

{
    "result_url": "http://127.0.0.1:8000/result/b303f13d-d716-4224-86c7-478b14d0ca77" 
}

brenj$ http GET http://127.0.0.1:8000/result/b303f13d-d716-4224-86c7-478b14d0ca77
HTTP/1.1 200 OK
Connection: close
Date: Sun, 13 Mar 2016 23:51:57 GMT
Server: gunicorn/19.4.5
content-length: 38
content-type: application/json; charset=utf-8

{
    "result": "2.0", 
    "status": "SUCCESS"
}
```

Please forgive me for using `gunicorn`.
