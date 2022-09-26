def Intro_Peronality(nickname,age,event,celebrity):
    print(f"大家好，我是{nickname}因為我小時候，大約在{age}歲的時候經歷一場大轉變，而成為大家眼中的{nickname}。我平常喜歡{event}，而且就如同{celebrity}一樣，對這個世界充滿好奇。")
def Intro_Job(title,member,location,goal):
    print(f"我的工作是{title}和{member}共事，我們常常一起開會討論事情。我常常在{location}出現，處理各方的需求和理解疑難雜症。我目前的方向是希望未來能實現{goal}")
def Intro_Diet(fav_meal,food,drink,dessert):
    print(f"每天我最期待的一餐是{fav_meal}，尤其是{food}在哪一餐吃都會讓我很開心，下午茶可以搭配一杯{drink}或是再加上幸福甜點{dessert}。如果能跟大家一起分享食物，我會非常開心。")

#可以重複提問
selfintro = input("需要自我介紹嗎?別人想知道你的哪一面呢? (Job, Diet, or ME)").upper()

if selfintro == 'ME':
    nickname =  input("你的綽號是:")
    age = input("小時候最可愛的年紀(數字):")
    event = input("印象深刻的事:")
    celebrity = input("一位名人:")
    Intro_Peronality(nickname,age,event,celebrity)

if selfintro == 'JOB':    
    title =  input("你的職稱:")
    member = input("好同事:")
    location = input("經常出沒地點:")
    goal = input("共同工作目標:")
    Intro_Job(title,member,location,goal)

if selfintro == 'DIET':    
    fav_meal =  input("早餐午餐晚餐最喜歡哪一餐:")
    food = input("最喜歡的食物:")
    drink = input("最愛的手搖飲:")
    dessert = input("最喜歡的甜點:")
    Intro_Diet(fav_meal,food,drink,dessert)