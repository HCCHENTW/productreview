# 讀取檔案的過程中印出長度才知道讀取進度
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1快寫法
		if count % 1000 == 0: #如果是一千的倍數才印出來
				print(len(data)) # 計算資料筆數 
# print(data[0]) #印出清單中的第一筆資料
print('檔案讀取完了,一共有', len(data),'筆資料')

#算出留言平均長度
#每一筆字串命名為d, 清單內的字串可以當成清單使用計算長度，用len(d)求長度,加總
#起始為零開始加每一筆的長度 sum_len累積所有的長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data)) 