
# Naming Game experiment

[![Build Status](https://travis-ci.org/wschuell/ng_userxp.svg?branch=master)](https://travis-ci.org/wschuell/ng_userxp)
[![codecov](https://codecov.io/gh/wschuell/ng_userxp/branch/master/graph/badge.svg)](https://codecov.io/gh/wschuell/ng_userxp)

### Requirements

Install docker and docker-compose
```
wget -qO- https://get.docker.com/ | sh
sudo pip install docker-compose
sudo usermod -aG docker $USER
```

### Install this repo:

```
git clone https://github.com/wschuell/ng_userxp.git
```

### Build and run docker containers
```
docker-compose up
```
and for development, using Django runserver with debug:
```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```

### Play the game:
go to http://127.0.0.1/ng

