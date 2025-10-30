x1,y1,r1 = map(int,input().split())
x2,y2,r2 = map(int,input().split())
distance_centre = (((x2-x1)**2)+((y2-y1)**2))**0.5
d = abs(r2-r1)
if distance_centre > r1+r2:
    print("NO")
elif d > distance_centre :
    print("NO")

else :
    print("YES")
