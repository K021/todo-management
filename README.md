> `config_secret` 파일이 깃에서 제외되어 있지 않아 새로 만들었다.

## 프로그램 설치 환경
python==3.6.3
RabbitMQ==3.5.7

# 기능 설명

> 접속 주소: http://ec2-13-125-254-180.ap-northeast-2.compute.amazonaws.com

## 할일 리스트
- `/`
- 할일들을 우선순위별로, 그리고 마감기한이 가까운 순서대로 분류된 것을 볼 수 있다. 
- 마감 완료 버튼으로 완료할 수 있으며, 완료된 경우 목록에서 사라진다. 
- 할일 작성 버튼이 있다.
- 할일을 클릭하면 할일 상세정보로 들어간다.

## 할일 상세정보
- `/todo/<pk>/`
- 할일 제목, 내용, 마감기한, 우선순위 정보가 표시된다. 
- 수정, 삭제 버튼이 있다.
- 삭제 버튼을 누를 경우, 확인 모달이 뜬다. 

## 할일 작성
- `/todo/add/`
- 할일 제목, 내용, 마감기한, 우선순위를 설정할 수 있다.

## 할일 변경
- `/todo/<pk>/change/`
- 할일 제목, 내용, 마감기한, 우선순위를 변경할 수 있다

## 할일 삭제
- `/todo/<pk>/delete`
- 할일을 삭제할 수 있다. 

## 할일 메일 알림
- celery beat 를 사용하여 periodic task 를 설정하였다.
- 10분 주기로 마감이 1시간 미만으로 남은 할일이 있는지 검색하고, 있는 경우 해당 정보를 메일로 보내준다.
- 메일은 gmail 을 사용하고 있으며, 보내는 메일은 joo2theeon.1@gmail.com, 받는 메일은 joo2theeon@gmail.com 으로 개발자 본인의 메일을 설정해두었다. 

# 기타 특징

## 서버
- 서버는 aws ec2 를 사용했고, nginx 와 uwsgi 를 사용했다. 시간이 나는 대로 elastic beanstalk 과 docker 를 사용할 예정이다. 

## 데이터베이스
- 데이터베이스 기능이 별로 필요하지 않으므로, 장고 기본인 db.sqlite 를 사용했다.


