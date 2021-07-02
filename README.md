# mini_pot  
U4-ER_project (smart green house)  
  
## 팀원  
phj, kjs  
  
## 구성  
* temp 폴더 : 테스트 or 추후 사용가능 코드  
    + .idea : 파이참 설정 폴더 (사용 X)  
    + log_* : 예전 기록 + 추후 참고가능  
    + python_test.py : 파이썬 구동 테스트 (단순 print)  
* blueprint 폴더 : 설계도면 모음  
* log 폴더 : 기록 모음  
* module_code 폴더 : 일부분 완성되어 추후 통합할 코드 모음  

- 모듈 완성후 server_main.py에 들어감 
- server_main.py : 현제 진행중 이름 그대로 서버실행의 메인  
  
  
## 약어 (나중에 볼때 편하시라구 ㅇㅅㅇ ctr+f)  
!! : 주의사항  
++ : 추후 수정사항, 개선사항  
  
#, ''', : 큰 목차  
*, +, - : 작은 목차  
#, ##, ### : 설명시 목차  
// : ''''''내부 설명 구분하기 위해서  
  
## todo (now)  
1. 실행 프로세스간 정보전달 (Question)  
2. 디비 테이블 분리 or 통합 (개인마다 데이터 분리할껀지 Q)  
### todo (thinking + algorithme)  
++ 정시 작동과 반복 작동의 분할 실행법  
++ 보고서 작성 양식과 전달 데이터 확정  ==>  전달 데이터 확정시 파이썬에서 가공작업  
++ a  
### todo (code file)  
++ S-recv, save, S-send main에 맞게 설정 + 추가 계발 (사실 에내도 위에 todo 보면 거의 0.. 아니다 1부터 시작하는...)  
++ manufacture, report: 0부터 시작하는 이세계 여행  
## todo (keep)  
1. 여러 사용자가 사용 가능하게 (keep)  
2. 젝슨 나노 사용 (keep)  
3. 보안문제 생각해보기 (keep)  
4. 에러사항 대처 필요함 (정시에 작동하는 코드 송-수신 오류시 재전송, 식물 불일치...)  
  
## git  
* 업로드  
cd C:\Users\dhkzh\Desktop\EndingProject\Git\mini_pot  
git add .  
git commit -m "주석"  
git push -u origin main  
  
* 다운로드  
git pull  
  
* LF or CRLF 에러 발생시  
git config core.autocrlf true  
  
- - - - -  
  
## mackdown  
* Enter  
줄 나눌때 띄워쓰기 두번 or html 다음줄 명령어 <br>  
  





  
## end  