1. Необходимые либы

requests
requests_kerberos
requests_ntlm

2. Использование

В конфиге пишем способ соединения: для 1с rest api(ntlm) или для workflow(kerberos)
В поле User пишем пароль и имя пользователя(только для ntlm)

3. Запускается с 3 ключами:
   1. url
   2. тип запроса (get, post, delete, patch).
   3. данные в нужном формате.