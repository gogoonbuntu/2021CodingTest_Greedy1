def bundan ():
	a = list(map(int, input().split()))
	N = a[0]
	K = a[1]
	count = 0
	while(N!=1):
		if(N<K):
			count+=N-1
			break;
		target = (N//K)*K
		count += N-target
		N = N//K
		count +=1
		print("N=",N)
		print("count=",count)

	return count

print(bundan())

#N/K 가 나눗셈이 안될때 해결불가.