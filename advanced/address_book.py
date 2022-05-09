# 주소록 프로그램 v1.1
# 작성일 : 2022-05-04 ~ 2022-05-06
# 작성자 : Heo Ahyun
# 설  명 : 연락처 추가, 출력, 삭제, 프로그램 종료

# 모듈
import os

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

def run() : 
    # contact = Contact('홍길동', '010-0000-1111', 'hgd@naver.com', '서울')
    # print(contact)
    # set_contact()
    list_contact = []    # 빈 리스트 생성
    load_contact(list_contact)   # 파일DB 읽어오기
    clearConsole()
    while True :
        sel_menu = get_menu()
        if sel_menu == 1 : 
            clearConsole()
            contact = set_contact()
            if contact is None : 
                input('계속하려면 엔터를 누르세요.')
                clearConsole()
                continue   # contact가 비면 리스트 추가 불가

            list_contact.append(contact)
            input('연락처 추가 성공\n계속하려면 엔터를 누르세요.')            # 아무값도 아니며, 단지 엔터 대기
            clearConsole()
        elif sel_menu == 2 :   # 연락처 출력
            clearConsole()
            get_contact(list_contact)
            input('계속하려면 엔터를 누르세요.')            # 엔터 대기
            clearConsole()
        elif sel_menu == 3 :   # 연락처 삭제
            clearConsole()
            name = input('삭제할 이름 입력 > ')
            del_contact(list_contact, name)
            input('연락처 삭제 성공\n계속하려면 엔터를 누르세요.')
            clearConsole()
        elif sel_menu == 4 :   # 종료
            save_contact(list_contact)   # 파일DB 저장
            break
        else :
            clearConsole()

# 주소록 입력함수
# def set_contact() -> None :
def set_contact() :
    contact = None
    try :   # 아무 입력 없거나 엔터, 갯수 틀리면 생기는 예외처리
        name, phone_num, e_mail, addr = \
            input('정보입력(이름, 핸드폰, 이메일, 주소(구분자 /)) > ').split('/')
        contact = Contact(name, phone_num, e_mail, addr)
    except Exception as e :
        print('입력갯수 확인(이름/핸드폰/이메일/주소)')
    finally :
        return contact  # 잘못되면 None 리턴, contact 객체 리턴

# 주소록 출력
def get_contact(list_contact) :
    for contact in list_contact :
        print(contact)

#  주소록 삭제
def del_contact(list_contact, name) :
    for i, contact in enumerate(list_contact) :
        if contact.name == name : 
            del list_contact[i]

# 주소록 파일DB 저장
def save_contact(list_contact) :
    f = open('./advanced/db_contact.txt', mode = 'w', encoding = 'utf-8')
    for contact in list_contact :
        f.write(contact.name + '/')
        f.write(contact.phone_num + '/')
        f.write(contact.e_mail + '/')
        f.write(contact.addr + '\n')            # 한사람 추가 끝난 후 엔터로 행 변경

    f.close()

# 주소록 파일DB 로드
def load_contact(list_contact) : 
    f = open('./advanced/db_contact.txt', mode = 'r', encoding = 'utf-8')
    while True :
        line = f.readline()
        if not line : break

        lines = line.rstrip('\n').split('/')  # \n 제거하고, /로 나눔( -> 리스트로)
        if len(lines) != 4 : continue   # 220506 11:11 엔터로 생기는 예외 처리
        contact = Contact(lines[0], lines[1], lines[2], lines[3])
        list_contact.append(contact)

    f.close()

# 메뉴 출력 및 선택
def get_menu() :
    str_menu = ('-- 주소록 프로그램 v1.1 --\n'
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
