
import pymysql

# Connect to the database
db = pymysql.connect(host='database-1.cdujw71krmsf.us-west-1.rds.amazonaws.com',
                             user='admin',
                             password='12345678',
                             database='users',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



cursor = db.cursor()
cursor.execute("select version()")
#now you will get the version of MYSQL you have selected on instance
data = cursor.fetchone()
print(data)





sql = 'create table persons(name text, email text,message text)'
cursor.execute(sql)


# In[31]:


cursor.execute('SELECT * FROM persons')

# Fetch the results
results = cursor.fetchall()

# Print the results
for result in results:
    print(result)


# In[25]:

cursor.execute(sql, val)

cursor.execute('SELECT * FROM persons')
results = cursor.fetchall()

# Print the results
for result in results:
    print(result)




