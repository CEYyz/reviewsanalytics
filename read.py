data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('總共有', len(data), '筆資料')

print(data[0])

wc ={}#word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('pls type word you want to check: ')
	if word == 'q':
		break	
	if word in wc:
		print(word, '出現過', wc[word])
	else:
		print('not in this dict')
print('thanks for using this')


# #留言平均長度
# sum_len = 0
# avg = 0
# for d in data:
# 	sum_len += len(d)
# print('留言平均長度是', sum_len/len(data))

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('長度小於100的留言', len(new))
# print(new[0])
# print(new[1])

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '筆留言提到good')
# print(good[0])

# #快寫法
# good = [1 for d in data if 'good' in d]
# print(good)
# bad =['bad' in d for d in data]
# print(bad)

#非快寫
#bad =[]
#for d in data:
#	bad.append('bad' in d)