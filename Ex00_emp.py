import pymysql as psql
import db
import pandas as pd

def print_menu():
    print('1. 사원정보 입력')
    print('2. 사원정보 출력')
    print('3. 사원정보 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)

def set_contact():
    data = (input("사번 입력 -> "), input("이름 입력 -> "), input("업무 입력 -> "), input("부서번호 입력 -> "))
    print('test', data)
    # Connection 얻어오기
    conn = psql.connect(host=db.host, port=3306, user='admin', password=db.password, db='projcetDB', charset='utf8',
                        autocommit=True)
    # cursor 얻어오기
    cursor = conn.cursor()
    #  sql 문장만들기
    sql = """
            INSERT INTO projcetDB.emp (empno, name, job, dept_no)
            VALUE (%s, %s, %s, %s)
        """
    # sql 실행(전송)
    cursor.execute(sql, data)
    # cursor 닫기
    cursor.close()
    # 연결 닫기
    conn.close()  # DB 연결 종료

def print_contact():
    # Connection 얻어오기
    conn = psql.connect(host=db.host, port=3306, user='admin', password=db.password, db='projcetDB', charset='utf8',
                        autocommit=True)
    # cursor 얻어오기
    cursor = conn.cursor()
    #  sql 문장만들기
    sql = """
            SELECT * FROM projcetDB.emp
            """
    # sql 실행(전송)
    cursor.execute(sql)
    for row in cursor:
        print('-' * 50)
        print('사번:{0} 이름:{1} 업무{2} 담당부서{3}'.format(row[0],row[1],row[2],row[3]))
    print('-' * 50)
    # cursor 닫기
    cursor.close()
    # 연결 닫기
    conn.close()  # DB 연결 종료


def delete_contact(empno):
    print(empno)
    # Connection 얻어오기
    conn = psql.connect(host=db.host, port=3306, user='admin', password=db.password, db='projcetDB', charset='utf8',
                        autocommit=True)
    # cursor 얻어오기
    cursor = conn.cursor()
    #  sql 문장만들기
    sql = """
                DELETE FROM projcetDB.emp where empno = {0}
                """.format(int(empno))
    # sql 실행(전송)
    cursor.execute(sql)
    for row in cursor:
        print(row)
    # cursor 닫기
    cursor.close()
    # 연결 닫기
    conn.close()  # DB 연결 종료

def run():
    # Contact 인스턴스를 저장할 리스트 자료구조 생성
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            set_contact()
        elif menu==2: # 출력을 선택하면
            print_contact()
        elif menu==3: # 삭제를 선택하면
            empno = input('삭제할 사원의 사번을 입력하세요 -> ')
            delete_contact(empno)


if __name__ == "__main__":
    run()