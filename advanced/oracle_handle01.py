# 오라클DB 연동
import cx_Oracle as ora

# 데이터소스 네임 객체 생성(접속주소, 포트번호, 서비스명)
dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
# DB연결객체
conn = ora.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'UTF-8')

# 커서 생성
cur = conn.cursor()
# 쿼리문 생성 및 작성
query = 'SELECT * FROM membertbl'

for row in cur.execute(query) :
    print(row)

# DB 클로징 필수 (네트워크, DB, 파일 연결 후 클로징 필수)
cur.close()
conn.close()