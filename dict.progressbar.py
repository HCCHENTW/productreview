import time
import progressbar 
#每個物件都有自己的專屬功能和資料型別
#物件的第一個字大寫例如ProgressBar function第一個字小寫例如print
#練習用pip套件https://pypi.org/project/progressbar2/
data = []
count = 0
bar = progressbar.ProgressBar(max_value = 1000000)# max_value這個物件
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 
		bar.update(count) 
print('檔案讀取完了,一共有', len(data),'筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data)) 

