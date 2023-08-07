import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


class Database:

    def __init__(self):
        self.connection = psycopg2.connect(**self.database_uri())
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    @staticmethod
    def database_uri():
        uri = {
            'user': os.getenv('DB_USER'),
            'password': os.getenv('PASSWORD'),
            'host': os.getenv('ADDRESS'),
            'port': os.getenv('PORT'),
            'database': os.getenv('DATABASE')
        }
        return uri

    def insert(self, table_name, table_attributes, params, values):
        try:
            self.connection.autocommit = False

            insert_query = f"""
                    INSERT INTO {table_name} ({table_attributes})
                        VALUES ({params})
                        RETURNING *;
                        """

            self.cursor.execute(insert_query, values)
            self.connection.commit()
            return self.cursor.fetchone()
        except Exception as e:
            self.connection.rollback()
            print(f"Falha ao cadastrar {table_name}.")
            print(f"Detalhe do erro: {e}")

    def select(self, table_name, condition):

        select_query = f"SELECT * FROM {table_name} WHERE {condition};"
        self.cursor.execute(select_query)

        results = self.cursor.fetchall()

        if results:
            return results
        else:
            print("Nenhum registro encontrado")

    def update(self, table_name, set_update, condition):
        try:
            update_query = f"""UPDATE {table_name}
            SET {set_update}
            WHERE {condition}
            RETURNING *;"""

            self.cursor.execute(update_query)
            self.connection.commit()
            results = self.cursor.fetchall()

            if results:
                return results
            else:
                print("Erro!")

        except Exception as e:
            self.connection.rollback()
            print("\nNão foi possivel atualizar os dados do cliente. Erro: ", e, "\n")

    def delete(self, table_name, condition):
        delete_query = f"""DELETE FROM {table_name}
                    WHERE {condition}"""
        result = self.cursor.execute(delete_query)
        self.connection.commit()
        return result

