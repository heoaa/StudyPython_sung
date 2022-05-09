# 주소록 프로그램 v1.5
# 작성일 : 2022-05-09
# 작성자 : Heo Ahyun
# 설  명 : 파일DB에서 Oracle로 변경 / 연락처 추가, 출력, 삭제, 프로그램 종료

# 모듈
import os
import cx_Oracle as ora

# 연락처 클래스
class Contact : 
    name = ''; phone_num = ''; e_mail = ''; addr = ''

    def __init__(self, name, phone_num, e_mail, addr) -> None:
        self.name = name
        self.phone_num = phone_num
        self.e_mail = e_mail
        self.addr = addr

    # 사용자가 볼 수 있는 화면
    def __str__(self) -> str :
        str_val = (f'이  름 : {self.name}\n'
                   f'핸드폰 : {self.phone_num}\n'
                   f'이메일 : {self.e_mail}\n'
                   f'주  소 : {self.addr}\n'
                   f'==============================')
        return str_val

# DB 초기화
def initDB() :
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
    conn = ora.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'utf-8')
    return conn

def run() : 
    conn = initDB()      # 오라클 연결 후 연결객체 생성
    clearConsole()
    while True :
        sel_menu = get_menu()
        if sel_menu == 1 : 
            clearConsole()
            isval = set_contact(conn)
            if isval :
                input('연락처 추가 성공\n계속하려면 엔터를 누르세요.')            # 아무값도 아니며, 단지 엔터 대기
            else :
                input('오류발생! 관리자 문의 요망')
            clearConsole()
        elif sel_menu == 2 :   # 연락처 출력
            clearConsole()
            get_contact(conn)
            input('계속하려면 엔터를 누르세요.')            # 엔터 대기
            clearConsole()
        elif sel_menu == 3 :   # 연락처 삭제
            clearConsole()
            name = input('삭제할 이름 입력 > ')
            del_contact(conn, name)
            input('연락처 삭제 성공\n계속하려면 엔터를 누르세요.')
            clearConsole()
        elif sel_menu == 4 :   # 종료
            conn.close()
            break
        else :
            clearConsole()

# 주소록 입력함수
# def set_contact() -> None :
def set_contact(conn) :
    contact = None
    isSucced = False # 입력 성공여부
    try :   # 아무 입력 없거나 엔터, 갯수 틀리면 생기는 예외처리
        name, phone_num, e_mail, addr = \
            input('정보입력(이름, 핸드폰, 이메일, 주소(구분자 /)) > ').split('/')
        contact = Contact(name, phone_num, e_mail, addr)
        # DB처리
        cur = conn.cursor() 
        # 공백없으면 예외발생(문자열, 공백 중요) // 따옴표로 구분하여 내리면 이어붙이기 가능(, 입력시 튜플로 인식)
        query = ('INSERT INTO addressbook '
                 'VALUES (SEQ_ADDRBOOK.nextval, :1, :2, :3, :4)')
        tup = (contact.name, contact.phone_num, contact.e_mail, contact.addr)
        cur.execute(query, tup)
        conn.commit()
        cur.close()
        isSucced = True
    except Exception as e :
        print('입력갯수 확인(이름/핸드폰/이메일/주소)')
        isSucced = False
    finally :
        return isSucced   # True이면 DB입력 성공, False이면 DB입력 실패

# 주소록 전체 출력
def get_contact(conn) :
    cur = conn.cursor()
    query = 'SELECT name, phone_num, e_mail, addr FROM addressbook'
    
    for row in cur.execute(query) : 
        contact = Contact(row[0], row[1], row[2], row[3],)
        print(contact)

    cur.close()

#  주소록 삭제
def del_contact(conn, name) :
    cur = conn.cursor()
    query = f"DELETE FROM addressbook WHERE name = '{name}'"
    cur.execute(query)
    conn.commit()
    cur.close()

# 메뉴 출력 및 선택
def get_menu() :
    str_menu = ('-- 주소록 프로그램 v1.5 --\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료')
    print(str_menu)

    # 0~9 숫자 외 ValueError 발생
    menu = 0
    try :
        menu = int(input('메뉴입력 : '))
    except Exception as e :
        print(e)
    finally :
        return menu

# 화면클리어 콘솔
def clearConsole() :
    command = 'clear'                # mac, unix, linux 화면클리어 명령어
    if os.name in ('nt', 'dos') :
        command = 'cls'              # windows, dos 화면 클리어 명령어
    os.system(command)

if __name__ == '__main__' :
    try : 
        run()
    except KeyboardInterrupt as e :
        print('Ctrl + c  종료')
