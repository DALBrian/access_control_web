import sqlite3
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("SELECT user_image2 FROM cms_user WHERE user_name = ?", ('br',))
data = cursor.fetchone()[0]
conn.close()
with open('output_image.jpg', 'wb') as file:
    file.write(data)