# def myfind(li, nu, start, end):
#     mid = (start + end) // 2
#     if end >= start:
#         if li[mid] > nu:
#             return myfind(li, nu, start, mid - 1)
#         elif li[mid] < nu:
#             return myfind(li, nu, mid + 1, end)
#         elif li[mid] == nu:
#             return mid
#     else:
#         return False
#
#
# li = [1, 3, 4, 6, 7, 8, 11, 13]
# nu = 13
#
# print(myfind(li, nu, 0, len(li)))

# 冒泡

li = [13, 5, 1, 3, 8, 6, 0, 4, 1, 2, 4, 4, 5]


# def mysort(li):
#     for i in range(len(li)):
#         for j in range(len(li)-i-1):
#             if li[j]>li[j+1]:
#                 li[j] , li[j + 1]=li[j+1],li[j]
#     return li

# 插入排序

# def mysort(li):
#     for i in range(1,len(li)):
#         tmp=li[i]
#         j=i-1
#         while j>=0:
#             if li[j]>tmp:
#                 li[j+1]=li[j]
#                 li[j]=tmp
#             j-=1
#     return li


# 选择排序

# def mysort(li):
#     for i in range(len(li)-1):
#         min_index=i
#         for j in range(i+1,len(li)):
#
#             if li[j]<li[min_index]:
#                 min_index=j
#
#         li[min_index],li[i]=li[i],li[min_index]
#     return li
#

#
#
# li2=mysort(li)
# print(li2)


# 两个栈实现一个队列

# class MyQueue(object):
#     def __init__(self):
#         self.stacka=[]
#         self.stackb=[]
#     def mypush(self,val):
#         self.stacka.append(val)
#     def mypop(self):
#         try:
#             if self.stackb == []:
#                 while self.stacka:
#                     self.stackb.append(self.stacka.pop())
#             # print(33333333333,self.stackb)
#             a=self.stackb.pop()
#             return a
#         except:
#             return "已经空空如也了"
#
#
# q=MyQueue()
# q.mypush(1)
# q.mypush(2)
# q.mypush(3)
# # print(q)
# print(q.mypop())
# print(q.mypop())
#
# q.mypush(4)
# q.mypush(5)
# q.mypush(6)
#
#
# print(q.mypop())
# print(q.mypop())
# print(q.mypop())
# print(q.mypop())
# print(q.mypop())


# 两个队列实现一个栈

# class MyStack(object):
#     def __init__(self):
#         self.queuea = []
#         self.queueb = []
#
#     def mypush(self, val):
#         if self.queueb == []:
#             self.queuea.append(val)
#         elif self.queuea == [] :
#             self.queueb.append(val)
#
#     def mypop(self):
#         try:
#             if self.queuea==[]:
#                 while len(self.queueb)>1:
#                     self.queuea.append(self.queueb.pop(0))
#                 return self.queueb.pop(0)
#             elif self.queueb==[]:
#                 while len(self.queuea)>1:
#                     self.queueb.append(self.queuea.pop(0))
#                 return self.queuea.pop(0)
#         except:
#             return "空空如也"
#
# q=MyStack()
# q.mypush(1)
# q.mypush(2)
# q.mypush(3)
# # print(q)
# print(q.mypop())
# print(q.mypop())
#
# q.mypush(4)
# q.mypush(5)
# q.mypush(6)
#
#
# print(q.mypop())
# print(q.mypop())
# print(q.mypop())
# print(q.mypop())
# print(q.mypop())


# def mytest(pusha,popa):
#     stack=[]
#     for i in range(len(pusha)):
#         stack.append(pusha[i])
#         try:
#             while  popa[0]==stack[-1]:
#                     # print(stack, popa, i)
#                     stack.pop()
#                     popa.pop(0)
#         except:
#             pass
#
#
#
#     if stack==[]:
#         return True
#     else:
#         return False
# pusha=[1, 2, 3, 4, 5]
# popa1=[1,5,4,3,2]
# popa2=[2,3,4,1,5]
# popa3=[1,5,4,2,3]
# popa4=[2,3,1,4,5]
#
# print(mytest(pusha,popa1))
# print(mytest(pusha,popa2))
# print(mytest(pusha,popa3))
# print(mytest(pusha,popa4))


# num=0
#
# def hanoi(n,a="A",b="B",c="C"):
#     global num
#     if n==1:
#         # num += 1
#         print(a,'--->',c)
#         return
#     else:
#         hanoi(n-1,a,c,b)
#         # num += 1
#         print(a, '--->', c,)
#         hanoi(n-1,b,a,c)
#     num+=1
#
#
# hanoi(3)
# print(num)

profit_rate= [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
profit_range = [100, 60, 40, 20, 10, 0]
x=float(input(">>>>"))
print(x,type(x))
y=0
for i in range(len(profit_range)):
    if x>profit_range[i]:
        y+=(x-profit_range[i])*profit_rate[i]
        x-=profit_range[i]

print(">>>>>  %.2f"%y)


















