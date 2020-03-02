def user_data_show( n, sn, bd, c, em, ph):
    """Выводит в одну строку данные от пользователя

    Именованные параметры:
    n -- имя
    sn -- фамилия
    bd -- год рождения
    c -- город проживания
    em -- email
    ph -- номер телефона

    """
    s = f"{n} {sn}, {bd}, {c}, {em}, {ph}"
    print( s)
    return s


user_data_show( n = input( "name: "),
                sn = input( "surname: "),
                bd = input( "birth year: "),
                c = input( "current city: "),
                em = input("email: "),
                ph = input( "phone number: "))