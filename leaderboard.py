import pymysql

# Connect to the database
connection = pymysql.connect(
    host='93.29.76.28',
    user='sudoquest',
    password='ccc455a76c8435cb3085632a83cfeb83792536f894d53593294f4048f9cdf198',
    db='sudoquest',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Insert a new score
with connection.cursor() as cursor:
    sql = "INSERT INTO scores (player_name, score) VALUES (%s, %s)"
    cursor.execute(sql, ('Alice', 100))
connection.commit()

# Retrieve the top 10 scores
with connection.cursor() as cursor:
    sql = "SELECT player_name, score FROM scores ORDER BY score DESC LIMIT 10"
    cursor.execute(sql)
    rows = cursor.fetchall()

# Format the scores as HTML
table_html = "<table>"
for row in rows:
    table_html += "<tr><td>{}</td><td>{}</td></tr>".format(row['player_name'], row['score'])
table_html += "</table>"
