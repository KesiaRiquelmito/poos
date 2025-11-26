import mysql.connector


class Database:
    def __init__(self):
        self.connection, self.cursor = self.get_connection()
        self._create_schema()

    def get_connection(self):
        connection = mysql.connector.connect(
            user="root",
            password="qawsedr123",
            host="localhost",
            database="poos",
            auth_plugin="mysql_native_password",
        )
        cursor = connection.cursor()
        return connection, cursor

    def _create_schema(self):
        stmts = [
            """
            CREATE TABLE IF NOT EXISTS users
            (
                id
                INT
                AUTO_INCREMENT
                PRIMARY
                KEY,
                username
                VARCHAR
            (
                255
            ) UNIQUE NOT NULL,
                password_hash VARCHAR
            (
                255
            ) NOT NULL,
                role VARCHAR
            (
                50
            ) NOT NULL
                )
            """,
            """
            CREATE TABLE IF NOT EXISTS departments
            (
                id
                INT
                AUTO_INCREMENT
                PRIMARY
                KEY,
                name
                VARCHAR
            (
                255
            ) UNIQUE NOT NULL,
                manager_employee_id INT NULL
                )
            """,
            """
            CREATE TABLE IF NOT EXISTS employees
            (
                id
                INT
                AUTO_INCREMENT
                PRIMARY
                KEY,
                contract_start_date
                VARCHAR
            (
                50
            ),
                name varchar(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                phone_number VARCHAR(50),
                address VARCHAR(255),
                salary DECIMAL
            (
                12,
                2
            ),
                department_id INT NULL,
                CONSTRAINT fk_employees_department
                FOREIGN KEY
            (
                department_id
            )
                REFERENCES departments
            (
                id
            )
                ON DELETE SET NULL
                )
            """,
            """
            CREATE TABLE IF NOT EXISTS projects
            (
                id
                INT
                AUTO_INCREMENT
                PRIMARY
                KEY,
                name
                VARCHAR
            (
                255
            ) UNIQUE NOT NULL,
                description TEXT,
                start_date VARCHAR
            (
                50
            )
                )
            """,
            """
            CREATE TABLE IF NOT EXISTS employee_projects
            (
                id
                INT
                AUTO_INCREMENT
                PRIMARY
                KEY,
                employee_id
                INT
                NOT
                NULL,
                project_id
                INT
                NOT
                NULL,
                UNIQUE
            (
                employee_id,
                project_id
            ),
                CONSTRAINT fk_ep_employee
                FOREIGN KEY
            (
                employee_id
            )
                REFERENCES employees
            (
                id
            )
                ON DELETE CASCADE,
                CONSTRAINT fk_ep_project
                FOREIGN KEY
            (
                project_id
            )
                REFERENCES projects
            (
                id
            )
                ON DELETE CASCADE
                )
            """,
            """
            CREATE TABLE IF NOT EXISTS shifts
            (
                id
                INT
                AUTO_INCREMENT
                PRIMARY
                KEY,
                employee_id
                INT
                NOT
                NULL,
                project_id
                INT
                NOT
                NULL,
                shift_date
                VARCHAR
            (
                50
            ) NOT NULL,
                worked_hours INT NOT NULL,
                task_description TEXT,
                CONSTRAINT fk_shifts_employee
                FOREIGN KEY
            (
                employee_id
            )
                REFERENCES employees
            (
                id
            )
                ON DELETE CASCADE,
                CONSTRAINT fk_shifts_project
                FOREIGN KEY
            (
                project_id
            )
                REFERENCES projects
            (
                id
            )
                ON DELETE CASCADE
                )
            """
        ]
        for stmt in stmts:
            self.cursor.execute(stmt)
        self.connection.commit()
        print("Base de datos y tablas creadas correctamente.")

    def execute(self, query, params=()):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor

    def fetch_all(self, query, params=()):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def disconnect_database(self):
        self.cursor.close()
        return self.connection.close()
