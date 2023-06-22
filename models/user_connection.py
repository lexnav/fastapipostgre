# import psycopg

# class UserConnection:
#     conn = None

#     def __init__(self):
#         try:
#             self.conn = psycopg.connect("dbname=fastapi_test user=postgres password=sa host=localhost port=5432")
#         except psycopg.OperationalError as e:
#             print(e.__str__())
#             self.conn.close()

#     def write(self, data):
#         with self.conn.cursor() as cur:
#             cur.execute("""
#                 INSERT INTO "user"(name, phone) VALUES(%(name)s %(phone)s)
#             """, data)
#         self.conn.commit()

#     def __def__(self):
#         self.conn.close()
