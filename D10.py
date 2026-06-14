import mysql.connector

try:
    con = mysql.connector.connect(
        user='root',
        password='root',
        database='pdbc',
        host='localhost'
    )
    crsr = con.cursor()

    Query1 = """
                UPDATE EMPLOYEE SET EMP_SAL = EMP_SAL - 5000 WHERE EMP_ID = 1
            """
    crsr.execute(Query1)

    Query2 = """
                UPDATE EMPLOYE SET EMP_SAL = EMP_SAL + 5000 WHERE EMP_ID = 2
            """
    
    crsr.execute(Query2)

    con.commit()

    no_of_emp = int(input('Enter Number of Employee: '))
    for i in range(1,no_of_emp+1):
        id = int(input('Enter Employee ID: '))
        name = input('Enter Employee Name: ')
        salary = int(input('Enter Employee Salary: '))
        role = input('Enter Employee Role: ')
        crsr.execute(Query,(id,name,salary,role))
    con.commit()
except Exception as e:
    con.rollback()
    print(e)


finally:
    crsr.close()
    con.close()