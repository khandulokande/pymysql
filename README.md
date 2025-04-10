# MySQL Database connection by using the PyMySQL method.

This repository contains a simple Python script that demonstrates how to connect to a MySQL database using the [PyMySQL](https://pymysql.readthedocs.io/en/latest/) library.

## 📜 Script Overview

The script connects to a MySQL database using the provided credentials and safely handles connection closure. It's a basic example ideal for beginners looking to understand how to use `PyMySQL` in their projects.

### 🔧 Code Functionality

```python
import pymysql

def connect_to_database():
    try:
        connection = pymysql.connect(
            host='192.168.0.100',
            user='username',
            password='password',
            database='dbname'
        )
        print("Connected to MySQL database using PyMySQL")

    except pymysql.MySQLError as e:
        print("Error while connecting to MySQL:", e)

    finally:
        if 'connection' in locals():
            connection.close()
            print("MySQL connection is closed")

connect_to_database()
```

## ✅ Requirements

- Python 3.x
- PyMySQL

### Install PyMySQL

You can install PyMySQL via pip:

```bash
pip install pymysql
```

## ⚠️ Note

- Make sure your MySQL server is accessible from the IP address specified.
- Replace the placeholder credentials (`host`, `user`, `password`, `database`) with your actual database details.
- This example uses plaintext credentials for simplicity. In a real-world project, consider using environment variables or a configuration file to store sensitive information securely.

## 📁 Project Structure

```
.
├── connect_mysql.py   # The main script file
└── README.md          # Project documentation
```

## 🚀 Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/khandulokande/pymysql.git
   cd pymysql
   ```

2. Edit `connect_mysql.py` and replace the database details.

3. Run the script:
   ```bash
   python connect_mysql.py
   ```

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
