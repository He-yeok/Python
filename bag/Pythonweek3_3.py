class Bag: #Bag클래스 정의
    def __init__(self) : #생성자 함수
         self.bag= [] # 데이터멤버 bag정의 및 초기화

    def contains(self,e) :
        return e in self.bag

    def insert(self,e) :
         self.bag.append(e)

    def remove(self,e) :
        self.bag.remove(e)

    def count(self,bag):
        return len(self.bag) 

myBag = Bag()
myBag.insert('휴대폰')
myBag.insert('지갑')
myBag.insert('손수건')
myBag.insert('빗')
myBag.insert('지갑')
myBag.insert('야구공')
print('가방속의 물건:', myBag.bag)

myBag.insert('빗')
myBag.remove('손수건')
print('내 가방속의 물건:', myBag.bag)






