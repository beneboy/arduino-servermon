import requests
from time import sleep
from settings import MONITOR_URL

def test_services():
    r = requests.get(MONITOR_URL, timeout=3)
    return r

def down_test():
    while True:
        requests.post('http://127.0.0.1:5000/applycolour/', data=dict(red='255', green='0', blue='0'))
        sleep(1.2)

        try:
            rc = test_services()
            success = rc.status_code == 200
        except requests.exceptions.Timeout:
            success = False

        if success:
            requests.post('http://127.0.0.1:5000/applycolour/', data=dict(red='', green='255', blue='0'))
            break

        requests.post('http://127.0.0.1:5000/applycolour/', data=dict(red='0', green='0', blue='0'))

        sleep(0.8)


def indicate_update():
    for i in xrange(15):
        requests.post('http://127.0.0.1:5000/applycolour/', data=dict(red='0', green='0', blue='255'))
        sleep(1.2)
        requests.post('http://127.0.0.1:5000/applycolour/', data=dict(red='0', green='0', blue='0'))
        sleep(0.8)


def main():
    version = None

    while True:
        try:
            rc= test_services()
            success = rc.status_code == 200
        except requests.exceptions.Timeout:
            success = False

        if not success:
            down_test()
            continue
        else:
            requests.post('http://127.0.0.1:5000/applycolour/', data=dict(red='0', green='255', blue='0'))

            if version is None:
                version = rc.text
            elif rc.text != version:
                version = rc.text
                indicate_update()
                continue

        sleep(30)


if __name__ == '__main__':
    main()
