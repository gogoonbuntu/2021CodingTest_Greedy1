def bundan ():
	a = list(map(int, input().split()))
	N = a[0]
	K = a[1]
	count = 0
	while(N!=1):
		mox = N%K
		N -= mox
		count += mox
		div = N/K
		count +=1
		N = div
		print("N=",N)

	return count

print(bundan())

#N/K 가 나눗셈이 안될때 해결불가.