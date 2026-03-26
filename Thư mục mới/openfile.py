def cach_truyen_thong():
    #step 1 : mo file
    #print(open("shop/test.txt","r").read())
    f=open("shop/test.txt","r")
    #step 2 : thao tac voi file
    data=f.read()
    print(data)
    #step 3 : dong file
    f.close
with open("shop/test.txt","r") as f:
    f.write("Dòng này được ghi vào file")
#chế độ w là ghi đè và xóa hết nội dung cũ
#chế độ a là ghi bổ sung vào nôiij dung cũ ,
# \n là kết hợp xuống dòng\
with open("shop/test.txt","r") as f:
    data=f.readlines()
    print(data)