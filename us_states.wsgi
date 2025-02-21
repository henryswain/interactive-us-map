import pymysql
import json
def application(environ, start_response):
    status = '200 OK'
    # connect
    dbcnx = pymysql.connect(host="webdev.divms.uiowa.edu",port=3306,user="henryswain",passwd="AgRZXxndJYXOIStHrDqk",db="cs3910_henryswain")
   
    print("line before query")
    sqlquery="""SELECT * FROM us_states;"""
    print("line after query")
    # create a database cursor
    cursor = dbcnx.cursor() 
   
    # execute SQL select 
    cursor.execute(sqlquery)
    result = cursor.fetchall()




    cursor.close ()
    dbcnx.close ()

        # Convert result to JSON
    json_result = json.dumps(result)
    print("json_result: ", json_result)

    # Send response
    start_response('200 OK',
                    [('Content-Type', 'application/json'),
                    ('Access-Control-Allow-Origin', '*'),
                    ('Access-Control-Allow-Methods', 'GET'),
                    ('Access-Control-Allow-Headers', 'Content-Type')]
    )
    return [json_result.encode('utf-8')]