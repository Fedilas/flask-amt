web: flask db stamp head; flask db migrate; flask db upgrade; flask translate compile; gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 microblog:app


