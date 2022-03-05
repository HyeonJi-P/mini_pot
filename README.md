# mini_pot  
U4-ER_project (smart green house)  
  
## 팀원  
HyeonJi-P(박현지), Jeongsu Kim(김정수)  
  
## 요약  
동아대학교 컴퓨터공학과 졸업 작품인 라즈베리파이를 이용한 스마트 미니온실 프로젝트의  
하드웨어 제어,관리부분과 서버통신처리 그리고 전체 설계에 해당하는 일부 소스코드 입니다.  
  
- - - - -  
  
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
  
## todo  
0. !! 빈 dict 자료형 발생  
0. ++ region, endregion VScode작동 안함..?  
0. ++ 코드 실행 과정에서 생성했던 파일 삭제하기  
0. ++ 디비에 이미지 저장 (오브젝트 스토리지 고려...?)  
0. ++ 이미지 상대경로 재설계  
0. ++ report에서 하루,일주일,월 구별실행  
0. ++ report 이미지 사진 비율 조정하기 (2개일떄 하나일때 ++PLT에서 나오는 이미지의 크기도 봐야함)  
1. table 구조 제작  
    1. 식물변경 함수 추가 (server_sql)  
    2. 회원가입 + serial number사용  
2. 보고서 작성  
    1. 파이썬으로 이미지 생성  
    2. 주별 보고서 작성시 주판단 월 넘어가는거, 프로그래밍 ...  
#### todo (thinking + algorithme)  
++ 정시 작동과 반복 작동의 분할 실행법 추가 생각  
++ 실행 프로세스간 정보전달 (Question)  
#### todo (keep)  
1. 다중 사용자 고려 (keep)  
2. 젝슨 나노 사용 (keep)  
3. 보안문제 생각해보기 (keep)  
4. 에러 대처 (정시에 작동하는 코드 송-수신 오류시 재전송, 식물 불일치...)  
  
- - - - -  
  
## git command help  
* 업로드  
cd 폴더위치
git add .  
git commit -m "주석"  
git push -u origin main  
* 다운로드  
git pull  
* LF or CRLF 에러 발생시  
git config core.autocrlf true  
  

## end  
  