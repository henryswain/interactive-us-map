import pymysql
import json

def application(environ, start_response):
    try:
        dbcnx = pymysql.connect(
            host="webdev.divms.uiowa.edu",
            port=3306,
            user="henryswain",
            passwd="AgRZXxndJYXOIStHrDqk",
            db="cs3910_henryswain"
        )
        
        print("line before query")
        sqlquery = """SELECT * FROM us_states;"""
        print("line after query")
        
        cursor = dbcnx.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sqlquery)
        result = cursor.fetchall()
        
        cursor.close()
        dbcnx.close()
        
        # Convert result to JSON
        json_result = json.dumps(list(result))
        print("json_result: ", json_result)
        
        # Send response
        start_response('200 OK', [
            ('Content-Type', 'application/json'),
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Methods', 'GET'),
            ('Access-Control-Allow-Headers', 'Content-Type')
        ])
        return [json_result.encode('utf-8')]
    
    except pymysql.MySQLError as e:
        error_msg = f"MySQL Error: {str(e)}"
        print(error_msg)
        start_response('500 Internal Server Error', [
            ('Content-Type', 'text/plain')
        ])
        return [error_msg.encode('utf-8')]
    
    except Exception as e:
        error_msg = f"General Error: {str(e)}"
        print(error_msg)
        start_response('500 Internal Server Error', [
            ('Content-Type', 'text/plain')
        ])
        return [error_msg.encode('utf-8')]
