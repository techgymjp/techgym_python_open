import random

def play(try_count):
  hit_count = 0
  ball_count = 0
  my_answers = []
  
  input_string = ""
  while True:
    tmp_string = input('【' + str(try_count) + '回目】違う数字4つの組み合わせを答えてください')
    if len(tmp_string) == 4 and tmp_string.isdigit():
      input_string = tmp_string
      break
#回答のリスト生成
  for i in range(0, 4):
    my_answers.append(int(input_string[i]))
#ヒット探し
  for i in range(0, 4):
    if my_answers[i] == answers[i]:
      hit_count += 1    
#ボール探し    
  for i in range(0, 4):
     if my_answers[i] in answers:
       ball_count += 1 #hit数が重複している  
  ball_count -= hit_count
#判定結果表示
  if hit_count == 4:
    print('おめでとう')
    print('正解は')
    print(answers)
    print(str(try_count) + '回目での成功。お疲れ様でした')
    return False
  else:
    print(str(hit_count) + 'ヒット' + str(ball_count) + 'ボールです')
    return True
  
#正解リスト設定
numbers = list(range(0, 10))
answers = random.sample(numbers, 4)

try_count = 1
while True:
  if play(try_count):
    try_count += 1
  else:
    break
    
