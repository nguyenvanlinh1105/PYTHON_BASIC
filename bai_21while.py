i=0
while i<5:
    print(i)
    i +=1
else:
    print("Đã lặp xong ")

    # đặc biệt đối với while trong python thì có cả else nữa 

# nếu có break thì ngừng luôn vòng lặp while và else không dược hoạt động vì vậy muốn hoạt động được else thì while không được break
    i=0
while i<6:
    print(i)
    i +=1
    if i==3:
        break
else:
    print("Đã lặp xong ")