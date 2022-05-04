# Driver

```sh
# authorized key
mkdir .ssh
curl https://github.com/gretchi.keys >> ~/.ssh/authorized_keys
```

```sh
# this repository
cd "${HOME}"
git clone git@github.com:gretchi/pi-temp-cm.git
```

```sh
# Docker
curl -fsSL https://get.docker.com/ | sh
curl -fsSL https://get.docker.com/gpg | sudo apt-key add
sudo curl -L https://github.com/docker/compose/releases/download/v2.5.0/docker-compose-linux-armv7 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G sudo gretel
sudo usermod -a -G docker gretel
```

```sh
# Python
sudo apt update
sudo apt install -y git make build-essential openssl wget curl llvm \
  libssl-dev libbz2-dev libreadline-dev libsqlite3-dev zlib1g-dev \
  libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

git clone https://github.com/yyuu/pyenv.git ~/.pyenv
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

cat < EOL >> ~/.bashrc
# pyenv and virtualenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
EOL

cd ~/pi-temp-cm/driver/admin-daemon
pyenv install --list
pyenv install 3.9.9
pyenv virtualenv 3.9.9 admin-daemon
pyenv local admin-daemon
```

```sh
# node npm
sudo apt update && sudo apt install nodejs npm
sudo npm install -g tplink-smarthome-api
/usr/local/bin/tplink-smarthome-api search
```
