from django.db import connection
from django.shortcuts import render


def login_(request):
    email = request.POST.get('email')
    psw = request.POST.get('psw')
    cursor = connection.cursor()
    query = "select password,name from app1_users where email = '" + email + "'"
    cursor.execute(query)
    st_psw = str(cursor.fetchone()[0])
   # name = str(cursor.fetchone()[1])
    if cursor.rowcount == 0:
        msg = ("Your account doesn't exist. Please signup")
        return render(request,'login_signup,html')
    elif st_psw != psw:
        msg = ("Invalid password")
        return render(request, 'index.html')

    else:
        # Login succeeded
        # Return to Profile page
        data = { "email": email }
        return render(request, 'profile.html', data)
print( 'done')
