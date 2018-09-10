from django.db import connections
from django.db import transaction
from school import read_models, write_models


# null if not have
def get_user_by_name(name):
    with connections['main'].cursor() as cursor:
        cursor.execute("SELECT username, "
                       "userPasswordHash, privilegeName "
                       "from User "
                       "inner join Privilege using (privilegeName) "
                       "where username=%s", (name,))
        row = cursor.fetchone()
        if row is None:
            return None

        return read_models.new_user(
            username=row[0],
            user_password_hash=row[1],
            privilege_name=row[2],
        )
    return None


# return False if fail, True if success
@transaction.atomic
def update_password(username, old_password,
                    new_password, re_enter_new_password):
    old_user = get_user_by_name(username)
    new_user = write_models.get_new_user_after_change_password(
        old_user=old_user,
        old_password=old_password,
        new_password=new_password,
        re_enter_new_password=re_enter_new_password
    )
    if new_user is None:
        return False

    with connections['main'].cursor() as cursor:
        cursor.execute("update User set userPasswordHash = %s "
                       "where username = %s",
                       (new_user['userPasswordHash'], new_user['username']))
    return True


# return False if fail, True if success
def add_account(username, password,
                re_enter_password, privilege_name):
    new_user = write_models.new_user_for_adding(
        username=username,
        password=password,
        re_enter_password=re_enter_password,
        privilege_name=privilege_name
    )
    if new_user is None:
        return False

    with connections['main'].cursor() as cursor:
        cursor.execute("insert into User("
                       "username, userPasswordHash, privilegeName) "
                       "values (%s, %s, %s)",
                       (new_user['username'],
                        new_user['userPasswordHash'],
                        new_user['privilegeName']))

    return True
