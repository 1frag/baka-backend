## baka-backend
Локальный запуск:
```(shell script)
# запустите контейнер:
$ docker-compose run --rm main /bin/bash

# проверьте хост:
$ ip a | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b"

# запустите сервер:
$ python /src/backend/app.py 8888
```
