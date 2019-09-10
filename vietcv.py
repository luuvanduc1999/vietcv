import datetime

def split_string(source):
	splitlist = " "
	output = []
	atsplit = True
	for char in source:
		if char in splitlist:
			atsplit = True
		else:
			if atsplit:
				output.append(char)
				atsplit = False
			else:
				output[-1] = output[-1] + char
	return output

def dtm(a,b):
    dc=a-b
    return dc.total_seconds()/60

def attackList(accessList, m, n):
    data=[]
    for x in accessList:
        # Tách xâu thành time và user cho vào data[[time,user]]
        data.append(split_string(x))
        
        # Đảo ngược lại thành [[user,time],[user,time],...]
        temp=data[-1][0]
        data[-1][0]=data[-1][1]
        data[-1][1]=temp

        # Chuyển time dạng xâu YYMMDDHHMMSS thành dạng thời gian trong python
        data[-1][1]=datetime.datetime.strptime("20"+data[-1][1],'%Y%m%d%H%M%S')

    # Mảng kết quả  
    result = []
    # Sắp xếp data theo user, rồi theo time
    data.sort()

    for i in range(0,len(data)):
        if data[i][0]!="":
            # Bắt đầu xet user
            user = data[i][0]
            
            # Đưa time truy cập đầu tiên vào time[]
            time=[]
            time.append(data[i][1])

            # k là vị trí đầu tiên đang xét trong time[]
            k=0

            # có tấn công hay không
            flag=0

            # Xét các time tiếp theo
            for j in range(i+1, len(data)):
                # mà cùng user
                if data[j][0]==user:
                    time.append(data[j][1])

                    # Nếu có hơn n phiên
                    if len(time)-k >= n : 
                        # mà phiên cuối vừa được thêm vào - phiên đầu tiên đang xét là k ít hơn m phút thì
                        if (dtm(data[j][1],time[k])<=m):
                            # cho user vào mảng kết quả
                            result.append(user)
                            
                            #đánh dấu tìm thấy
                            flag=1

                            #cho hết các phần tử user tiếp theo có cùng user về rỗng để không xét lại
                            for t in range(i,len(data)):
                                if (data[t][0]==user):
                                    data[t][0]=""
                                elif (data[t][0]!=user) and (t>j):
                                    break
                            break
                        #ngược lại thì tăng k để xét thời gian bắt đầu tiếp theo
                        else: 

                            k=k+1

    print (result)
