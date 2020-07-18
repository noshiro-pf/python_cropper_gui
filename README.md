# Cropper

## Usage

1. create venv

```sh
$ python3 -m venv env
$ source env/bin/activate
```

2. Install dependencies

```sh
(env) $ python3 -m pip install -r requirements.txt
```

3. Run `cropper.py` or `cropper_rx.py`

```sh
(env) $ python3 ./src/cropper.py
```

or

```sh
(env) $ python3 ./src/cropper_rx.py
```

## lint

```sh
(env) $ python3 -m flake8 ./src
```

## format

```sh
(env) $ python3 -m isort ./src
(env) $ python3 -m black -l 79 ./src
```
