# 📋 simple board (w/ flask)
## 구현 목표
- crud
- connect dbms
- docker

## 사용 기술
- python
- flask : a lightweight WSGI(Web Server Gateway Interface) web application framework
- jinja : a templating engine for Python
- docker : a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings
- mongo db

## 계획
- [x] ~12/20 : crud 구현
- [x] ~12/22 : mongo db 연동
- [x] ~12/27 : docker 연동

## 사용 방법
1. 실행 pc에 docker 설치
- https://www.docker.com/get-started
2. 프로젝트 경로에서 터미널을 통해 docker image 생성 (초기 실행에만)
- -t : image tag 설정
~~~
docker build -t [image_name] .
~~~
3. docker compose 실행
- -d : 백그라운드 작업
~~~
docker-compose up -d
~~~
4. 설정한 포트에서 정상 실행 확인
- http://0.0.0.0:5000/
