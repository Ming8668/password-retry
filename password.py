# 密碼重設程式
# password = 'a1234'
# 請使用者重複輸入密碼
# 最多輸入3次
# 如果正確 就印出'訓練成功'
# 如不正確 就印出'密碼錯! 還有__次機會!!'

password ="a1234"
i = 3

while True:
  pwd = input('請輸入密碼:')
  if pwd == password:
    print('輸入成功!')
    break
  else:
    i = i - 1
    print('密碼錯誤! 還有', i,'次機會!!')
    if i == 0:
      break

