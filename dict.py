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
print(data[0]) 

#文字記數
#words是一個清單中裝很多個字
#用空白分隔每一個字
#wc['are']  
wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1 #已經出現過的字就在字典中記數
		else:
			wc[word] = 1 #遇到還沒有在字典中的自就新增新的key進wc字典
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc)) 

while True:
	word = input('請問你想找什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word,'出現過的次數為:', wc[word])
	else:
		print('這個字沒有出現過喔!')
print('感謝使用本功能')



# #算出留言平均長度
# #每一筆字串命名為d, 清單內的字串可以當成清單使用計算長度，用len(d)求長度,加總
# #起始為零開始加每一筆的長度 sum_len累積所有的長度
# sum_len = 0
# for d in data:
# 	sum_len = sum_len + len(d)
# print('留言的平均長度為', sum_len/len(data)) 

# #對清單做篩選
# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('一共有',len(new),'筆留言長度小於100' )
# print(new[0])

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good),'筆留言提到good')

# #快寫法 list comprehension
# good =[d for d in data if 'good' in d]