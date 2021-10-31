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

