# mini_pot  
U4-ER_project (smart green house)  
  
## 팀원  
phj, kjs  
  
## 구성  
* temp 폴더 : 테스트 or 개발중 or 추후 사용가능 코드  
    + .idea : 파이참 설정 폴더 (사용 X)  
    + log_* : 예전 기록 + 추후 참고가능  
    + python_test.py : 파이썬 구동 테스트 (단순 print)  
* blueprint 폴더 : 설계도면 모음  
* log 폴더 : 기록 모음  
* module_code 폴더 : 일부분 완성되어 추후 통합할 코드 모음  
* report_result 폴더 : 보고서가 작성되서 저장되는 장소
* report_template 폴더 : 보고서 작성시 사용되는 탬플릿, 사진 저장구간
  
## 약어 (ctr+f로 보기 편하게)  
!! : 주의사항  
++ : 추후 수정사항, 개선사항  
  
## todo (now)  
0. server_main 어느정도 돌아가는 느낌 만들기  ++ 빈 dict 자료형 발생  
1. table 구조 설계 (회원가입 추가해서...)  
    1. 식물변경 함수 추가 (server_sql)  
    2. 테이블 추가하고 기록  
2. 보고서 작성 양식과 전달 데이터 확정  
    1. 전달 데이터 확정시 파이썬으로 이미지 생성  
    2. docx에 이미지 배치하기  
3. 분기 명령어 (order) 정립 
4. RPi_main 완성해서 테스트 해봐야함  
#### todo (thinking + algorithme)  
++ 정시 작동과 반복 작동의 분할 실행법 추가 생각  
++ 실행 프로세스간 정보전달 (Question)  
++ 디비 테이블 분리 or 통합 (개인마다 데이터 분리할껀지 Q)  
#### todo (keep)  
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