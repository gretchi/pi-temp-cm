# template

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
