## 엑셀 계산 사이트 구현

* main
  - 메인화면 : signin() => 로그인 페이지
  - 회원가입 : join()
    - 사용자 이메일, 이름 길이 제한
    - 이메일 중복체크
    - 회원가입 인증 이메일 발송 함수 호출
  - 로그인 : login()
    - 사용자가 입력한 PW 암호화
    - 사용자 이름과 이메일을 session에 저장
  - 로그아웃 : logout()
  - 이메일 인증 : verify()
  - 로그인 성공시 : index()
    - 엑셀 파일 업로드 가능
  - 업로드된 엑셀 파일 계산 결과 : result()  

* sendEmail
  - send() : 인증코드 적힌 메일을 발송  

* calculate
  - calculate() : pandas를 사용해 읽어들인 엑셀 파일을 계산
