import random

try_count = 1

#ランダムの違う4つの数字の配列を作る
def rand_ints_nodup(a, b, k):
  ns = []
  while len(ns) < k:
    n = random.randint(a, b)
    if not n in ns:
      ns.append(n)
  return ns

def play():
  global try_count
  hit_count = 0
  ball_count = 0
  my_answer = input('【' + str(try_count) + '回目】違う数字4つの組み合わせを答えてください')
  my_1000s_number = my_answer[-4]
  my_100s_number = my_answer[-3]
  my_10s_number = my_answer[-2]
  my_1s_number = my_answer[-1]
#ヒット探し  
  if my_1000s_number == con_1000s_number:
    hit_count += 1
  if my_100s_number == con_100s_number:
    hit_count += 1
  if my_10s_number == con_10s_number:
    hit_count += 1
  if my_1s_number == con_1s_number:
    hit_count += 1
#ボール探し    
  if my_1000s_number == con_1s_number or my_1000s_number == con_10s_number or my_1000s_number == con_100s_number:
    ball_count += 1
  if my_100s_number == con_1s_number or my_100s_number == con_10s_number or my_100s_number == con_1000s_number:
    ball_count += 1
  if my_10s_number == con_1s_number or my_10s_number == con_100s_number or my_10s_number == con_1000s_number:
    ball_count += 1 
  if my_1s_number == con_10s_number or my_1s_number == con_100s_number or my_1s_number == con_1000s_number:
    ball_count += 1 
#判定結果表示
  if hit_count == 4:
    print('おめでとう')
    print('正解は' + my_answer + 'です')
    print(str(try_count) + '回目での成功。お疲れ様でした')
  else:
    print(str(hit_count) + 'ヒット' + str(ball_count) + 'ボールです')
    try_count += 1
    play()

#正解設定
answer = rand_ints_nodup(0, 9, 4)
con_1s_number = str(answer[3])
con_10s_number = str(answer[2])
con_100s_number = str(answer[1])
con_1000s_number = str(answer[0])

play()