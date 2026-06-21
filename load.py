import sqlite3
def load_data(data): 
    conn = sqlite3.connect("sales.db")
    
    data.to_sql("sales", conn, if_exists="replace", index=False)
    
    conn.close()