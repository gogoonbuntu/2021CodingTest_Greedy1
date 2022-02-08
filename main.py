# N 에 -1 혹은 나누기 K를 반복수행. N이 1이 될 때 까지. 가장 적은 횟수로.
# 나눗셈이 가능할 때 무조건 하는 것이 좋다 (2라 해도 -1보다 훨씬 빨리 줄기 때문)

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