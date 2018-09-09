from django.db import connection
from school import read_models as models


# null if not have
def get_user_by_name(name):
    with connection.cursor() as cursor:
        cursor.execute("SELECT username, "
                       "userPasswordHash, privilegeName "
                       "from User "
                       "inner join Privilege using (privilegeId) "
                       "where username=%s", (name,))
        row = cursor.fetchone()
        if row is None:
            return None

        return models.new_user(
            username=row[0],
            user_password_hash=row[1],
            privilege_name=row[2],
        )
    return None
