import cx_Oracle as oci
#[DB 연동 절차]
#1. Connection 얻어오기
conn = oci.Connection('scott/tiger@127.0.0.1:1521/xe')
print(conn.version)     #오라클 연결했는지 확인 및 ver확인하기
#2. sql 문장만들기
sql = 'SELECT * FROM EMP'
#3. cursor 얻어오기
cursor = conn.cursor()
#4. sql 실행(전송)
cursor.execute(sql)
for row in cursor:
    print('사번:{0} 사원명:{1}'.format(row[0],row[1]))
# cursor.execute(sql)
# datas = cursor.fetchall()
# #print(datas)
# for row in datas:
#     print('사번:{0} 사원명:{1}'.format(row[0], row[1]))
#5. cursor 닫기
cursor.close()
#6. 연결 닫기
conn.close()