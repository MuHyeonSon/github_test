class BankAccount :       #은행계좌클래스
  def __init__(self,name,number,money = 0) :    # 객체생성
     self.__name = name      #3가지 멤버변수 모두 private변수로 할거니까 변수명 앞에 __ 붙이기
     self.__number = number
     self.__money = money
  
  def deposit(self,money) :
    self.__money += money   # 여기 어떻게 쓰는지 모르겠음 양의 정수를 매개변수로 받을 거임 

  def withdraw(self,money) :
    if self.__money >= money:
      self.__money -= money
      return True
    else :
      return False 
    self.__money -= money

  def __str__(self) :
    return f"name: {self.__name}, number: {self.__number}, balance: {self.__balance}"