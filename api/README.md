# Django-restful-framework Server
Django-restful-framework를 기반으로 구성되어있습니다.

## Applications

### Transi

현재 유일한 어플리케이션 입니다. Document, Paragraph, Translated 객체들([참조](/doc/models.md))과 관련된 모든 기능들을 담당합니다.

`/documents`, `/paragraphs`, `/translateds` 로 url이 이어집니다.

restful-framework특성상, `Content-type`이 `html`인, 브라우저로 접속할 경우 디버그 모드에서 테스트할 수 있는 사이트를 사용할 수 있습니다.

Authentication은 [BasicAuth](https://en.wikipedia.org/wiki/Basic_access_authentication)를 사용하고 있습니다.

## How to run
만약 실행에 성공하면 [http://localhost:8000](http://localhost:8000)에 연결해서 사용해볼 수 있을 것입니다.

### Prepare (In first)
```sh
virtualenv venv -p python3  # create virtual python environment
source venv/bin/activate  # activate virtual python environment(venv)
pip install -r requirements.txt  # setup all requirements to venv
python manage.py makemigrations  # make migration configurations for using sqlite3
python manage.py migrate  # make sqlite3 database file and schemes
```
### Run
```sh
source venv/bin/activate  # activate venv only if proper venv isn't activated
python manage.py runserver
```