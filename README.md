# template

## sensors

- 1-ぴー: EB:EA:8A:94:5C:D8
- 2-そら: C4:43:D5:0d:4D:F4
- 3-じん: FD:6B:1D:D9:15:56
- 4-きな: DC:08:9A:D2:9B:8A
- 5-ゆき: C2:B9:B2:F8:24:12

## plugs

- 1-ぴー: 10:27:F5:22:07:C9
- 2-そら: AC:84:C6:51:14:91
- 3-じん: 10:27:F5:22:08:E7
- 4-きな: 0C:80:63:04:FD:0B
- 5-ゆき: 10:27:F5:22:08:12

## ln

```sh
cd controller
ln -s ../lib-common/helper helper
ln -s ../lib-common/service_base service_base
ln -s ../lib-common/mq_client mq_client
ln -s ../lib-common/consumer_base consumer_base

cd driver
ln -s ../lib-common/helper helper
ln -s ../lib-common/service_base service_base
ln -s ../lib-common/mq_client mq_client
ln -s ../lib-common/consumer_base consumer_base
```

## Driver

### Endpoint

- [GET] /sensor/{mac}
- [POST] /sensors
- [GET] /plug/{mac}
- [GET] /plugs
- [POST] /plug/{mac}/{state}
- [POST] /device/restart

### object

```json
<Sensor>: {
    "ok": <bool>,
    "temp": <float>,
    "humidity": <int>,
    "battery": <int>,
    "ts": <string>,
    "mac": <string>
}

<Plug>: {
    "ok": <bool>,
    "state": <int>,
    "mac": <string>,
    "ip": <string>
}

```

## MACアドレス形式

DB格納時は `-` で区切る

```plaintext
XX-XX-XX-XX-XX-XX
```

## install ubuntu to docker and docker-compose

```bash
sudo apt-get update
sudo apt-get -y install curl

# docker
curl -fsSL https://get.docker.com/ | sh
curl -fsSL https://get.docker.com/gpg | sudo apt-key add

# docker-compose
sudo curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

usermod -a -G sudo gretel
usermod -a -G docker gretel
```

## install deploy key

```bash
ssh-keygen -f ~/.ssh/${REPO_NAME}
cat ~/.ssh/${REPO_NAME}.pub
```

```ssh-config:~/.ssh/config
Host ${REPO_NAME}
    HostName github.com
    IdentitiesOnly yes
    IdentityFile ~/.ssh/${REPO_NAME}
    User git
```
