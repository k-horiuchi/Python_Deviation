class Deviation :
	# 平均値を算出
	def getAverage(items): return float(sum(items) / len(items))
	# 偏差を算出
	def getDeviationList(items) : return tuple([float(item) - Deviation.getAverage(items) for item in items])
	# 分散を算出
	def getDeviationTotal(items) : return Deviation.getAverage(tuple([pow(float(item),2) for item in Deviation.getDeviationList(items)]))

items = (71,80,89)
print(Deviation.getDeviationTotal(items))