from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configuration for AWS RDS MySQL
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'database': 'your_database',
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Insert data into the database
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            query = "INSERT INTO your_table (name, email, message) VALUES (%s, %s, %s)"
            values = (name, email, message)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return 'Data inserted successfully!'
        except mysql.connector.Error as error:
            return f'Error: {error}'
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
