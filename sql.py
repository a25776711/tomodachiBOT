import pymysql


conn=pymysql.connect(host="127.0.0.1", user="root", password="QinQin929Kaven0321", database="covid", charset='utf8' )
cursor=conn.cursor()
sql="""
    CREATE TABLE Member(
        ID int(6),
        Code int(6),
        coordinate float(20)
    );
    """
cursor.execute(sql)
conn.commit()
conn.close()