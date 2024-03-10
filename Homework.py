print("Chương trình Python tính toán")
str=input()
str=str.strip()
print("Loại bỏ các khoảng trắng thừa:"+str)
class Tinh:
    def __init__(self) -> None:
        pass

    def Add(a,b):
        return a+b
    
    def sub(a,b):
        return a-b
    
    def mul(a,b):
        return a*b
    
    def div(a,b):
        return a/b
    
def CountIn(s):
    a=s.index("(")
    b=s.index(")", len(s), 0)

a=str.index("(")
b=str.index(")")
print(a,b)