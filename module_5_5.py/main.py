
import time
from  re import match
from sys import hash_info


class User:

    def __init__(self,nickname,password,age,):
        self.nickname = nickname
        self.password = hash_info
        self.age =  age

    def __str__(self):
        #return self.nickname
        return f'User(Имя: {self.nickname},возраст: {self.age})'
    def __eq__(self, other):
        return other.nickname == self.nickname
    def __get__info(self):
        return self.nickname,self.password

class Video:

    def  __init__(self,title,duration,uploader,adult_mode = False):
        self.title = title
        self.duration = duration
        self.uploader = uploader
        self.time_now = 0

    def __str__(self):
        return self.title
        print( f'Video(Название: {self.title}, продолжительность:-{self.duration} канал: ("Мы теперь с тобой друзья")')
    def __repr__(self):
        return self.title

class UrTube:
    titles = ()
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self,login,password):
        for user in self.user:
            if (user.login,hash(password)) == user_get_info():
                self.current_user = user
                #print(f'Вход выполнен: {self.current_user.login}')
                return user
            print(f'Вход выполнен: {self.current_user.login}')
    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
                self.current_user = new_user
        return new_user

    def log_out(self):
         self.current_user = None
    def add(self,* videos:Video):
        for video in videos:
            if video not in self.videos:
                print('Неверный никнейм или пароль')
                return self.videos.append(video)
        print('Пользователь уже существует ')

    def get_videos(self,search_word):
        search_word = search_word.lower()
        matched_videos = [video for video in self.videos if search_word in video.title.lower()]
        return matched_videos


    def match_video(self,search_word):
        matched_videos = self.get.videos(search_word)
        if not matched_videos:
            print('Ничего не найдено')
            return

        for video in matched_videos:
            if video.adult_mode and self.current_user.age<18:
                print('Вам нет 18 лет.Вы не можете просматривать видео')
                continue
            print(f"Воспроизведение видео '{video.title} на {video.duration} секунд(ы)...")
        for second in range(video,duration):
            print(f"Секунда {sekond+1}...")
            time.sleep(1)
            print('Конец видео.')
            video.time_now = 0

ur=UrTube()
user1 = User('Lisa','3233','19')
print(user1)
user2 = User('Volk','8978','12')
print(user2)
new_user = User('Bolik','5466','25')
print(new_user)
video1 = 'Приколы нашего UU',23,'user1'
video2 = 'Позитив и юмор-наше кредо',30,'adult_mode = True'
print('Lisa',hash_info)
match_video2 = video2
print(video2)
watch_video1 = video1
print(video1)
watch_video2 = video2
print(video2)
v1 = video1
v2 = video2









