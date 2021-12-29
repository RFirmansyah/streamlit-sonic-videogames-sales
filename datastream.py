import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gsheetsdb'])

from gsheetsdb import connect

source = "https://docs.google.com/spreadsheets/d/1tESr-18oIksdded9aniQMo2gGCEtOwJWhoQWNdW__Ws/"

template = """
        SELECT
            name,
            platform,
            manufacturer,        
            year,
            region,
            sales
        FROM
            "{0}"
    """

def data_stream():
    query = template.format(source)
    
    conn = connect()
    result = conn.execute(query, headers=1)
    
    return result 