import cx_Oracle as oci
import csv


def createTable():
    # [DB 연동 절차]
    # 1. Connection 얻어오기
    conn = oci.Connection('scott/tiger@127.0.0.1:1521/xe')
    # 2. sql 문장만들기
    sql = """
    CREATE TABLE supply
        (
            id integer primary key,
            supplier_name varchar(30),
            invoice_number varchar(20),
            part_number varchar(30),
            cost integer,
            purchase_date date
        )
    """
    # 3. cursor 얻어오기
    cursor = conn.cursor()
    # 4. sql 실행(전송)
    cursor.execute(sql)
    # ------------------------------
    sql2 = "CREATE sequence SEQ_SUPPLY_ID"
    cursor.execute(sql2)
    # 5. cursor 닫기
    cursor.close()
    # 6. 연결 닫기
    conn.close()


def saveTable(data):
    # 1. Connection 얻어오기
    conn = oci.Connection('scott/tiger@127.0.0.1:1521/xe')
    # 2. sql 문장만들기
    sql = """
    INSERT INTO supply (id, supplier_name, invoice_number, part_number, cost, purchase_date)
    VALUES (SEQ_SUPPLY_ID.nextval, :0, :1, :2, :3, :4)
    """
    # 3. cursor 얻어오기
    cursor = conn.cursor()
    # 4. sql 실행(전송)
    cursor.execute(sql, data)
    # 5. cursor 닫기
    cursor.close()
    # 6. 연결 닫기
    conn.commit()
    conn.close()


def viewTable(tname):
    print("입력하는 테이블 명 : {0}".format(tname))
    # 1. Connection 얻어오기
    conn = oci.Connection('scott/tiger@127.0.0.1:1521/xe')
    # 2. sql 문장만들기
    sql = 'SELECT * FROM {}'.format(tname)
    # 3. cursor 얻어오기
    cursor = conn.cursor()
    # 4. sql 실행(전송)
    cursor.execute(sql)
    for row in cursor:
        print(row)
    # 5. cursor 닫기
    cursor.close()
    # 6. 연결 닫기
    conn.close()


if __name__ == '__main__':
    # createTable()
    # imsi = ['kosmo','9999','8888',1000,'2022-04-20']
    # saveTable(imsi)
    # file = open('./files/supply.csv','r')
    # datas = csv.reader(file, delimiter=',')
    # header = next(datas, None) #첫번째 줄을 뺀다 None 할일이 없다!
    # print("{}".format(header))
    # for row in datas:
    #     saveTable(row)
    # file.close()
    # 지정된 테이블 명에 레코드들을 출력하는 함수
    viewTable('supply')
