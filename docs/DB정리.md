## 유저 DB : user

username 



## 전통주 DB : liquor

 liquorname

## 주문 DB : order

order_id :주문번호	/ int, pk 

tid : 주문 고유번호

username : 유저 이름 / 

kakaoemail : 카카오 이메일 / varchar(50)

liquornumber : 전통주 번호 / int

liquorname	: 전통주 이름	/ varchar(50)

liquorprice : 전통주가격

quantity : 수량	/int

waynumber : 운송장 번호 / varchar(50)

address :주소	/ varchar(200)

phonenumber	:핸드폰 번호	/ varchar(20)

uniqueness : 희망사항	/ varchar(300)

created_at : 주문시간	/ datetime

status : 주문상태(배송중, 등)	/ char(2)





## 구매내역 DB : purchase

kakaoemail	: 카카오 이메일	/ varchar(50)

liquornumber : 전통주 번호	/ int

liquorname : 전통주 이름	/ varchar(50)

quantity : 수량	/ int





## 리뷰 DB : review

review_id 	: 리뷰 번호

liquornumber	: 전통주 아이디

kakaoemail	: 카카오이메일

score	:평점

created_at : 생성일자

updated_at : 수정일자

content	: 리뷰내용



## 정기구독 DB : subscription

subscription_id 

kakaoemail : 이메일

address : 주소

continuemonth : 연속 정기구독 개월 수

created_at : 구독 시작일

next_payday : 다음결제일



## 장바구니 DB : cart

cart_id : 장바구니 번호

kakaoemail	: 카카오이메일

liquornumber	: 전통주 번호

liquorname : 전통주 이름

liquorprice : 전통주가격

quantity	:수량

