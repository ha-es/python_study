# 직접 에러 발생 가능
class BigNumberError(Exception):
    def __init__(self, msg) :
        self.msg = msg
        
    def __str__(self):
        return self.msg

# 의도적으로 에러 발생

try :
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1=int(input("첫 번째 숫자를 입력하세여 : "))
    num2=int(input("두 번째 숫자를 입력하세여 : "))
    
    if num1 >=10 or num2 >= 10 :
        #raise ValueError     #12번째 줄 실행
        #raise BigNumberError
        raise BigNumberError("입력값 : {0}, {1} ".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
    
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
    
# except BigNumberError:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")

except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
