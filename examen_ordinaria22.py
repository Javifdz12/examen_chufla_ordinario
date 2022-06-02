import re
import datetime
class userAccount:
    def __init__(self,alias,email,tweets,timeline,seguidores):
        if isinstance(alias,str):
            self.alias=alias
        else:
            self.alias="alias"
        if re.search(".*@.*\..*", email)==None or email=="":
            self.email=input("correo electronico debe tener formato xxx@xxx.xx: ")
        else:
            self.email=email
        self.tweets=tweets

        self.seguidores=seguidores

        self.timeline=timeline
    def get_seguidores(self):
        return self.seguidores
    def set_seguidores(self,user):
        self.seguidores=self.seguidores.append(user)
#user es un objeto useaccount
    def follow(self,user):
        user.seguidores=user.set_seguidores(self)

    def tweet(self,post):
        f=open(self.tweets,"w")
        f.write(f"\n {post}")
        f.close()


manolo=pepe=userAccount("manolo","manolo@j.j","tweets4.txt","tweets5.txt",[])
pepe=userAccount("pepe","pepe@j.j","tweets.txt","tweets1.txt",[manolo])
javi=userAccount("javi","javi@j.j","tweets2.txt","tweets3.txt",[manolo])
pepe.follow(javi)
javi.follow(pepe)
javi.tweet("hola que tal soy nuevo")
print(javi.seguidores)
print(pepe.seguidores)

class tweet:
    def __init__(self,fichero,time,tweet,user):
        if len(time)==8:
            fecha_apertura=datetime.datetime.strptime(fecha_apertura,"%d%m%Y")
            self.time=time
        else:
            print("fecha no existe")
        self.fichero=fichero
        if len(tweet)<=140:
            self.tweet=tweet
        else:
            raise Exception("demasiado largo")
        self.user=user

    def publicar(self):
        f=open(self.fichero,"w")
        f.write(f'\n {self.time}')
        f.write(f'\n {self.tweet}')
        f.close()

class directmessage:
    def __init__(self,fichero,time,tweet,user1,user2):
        if len(time)==8:
            fecha_apertura=datetime.datetime.strptime(fecha_apertura,"%d%m%Y")
            self.time=time
        else:
            print("fecha no existe")
        self.fichero=fichero
        if len(tweet)<=140:
            self.tweet=tweet
        else:
            raise Exception("demasiado largo")
        self.user1=user1
        self.user2=user2

    def comenzar_coversacion(self):
        f=open(self.fichero,"w")
        f.write(f'\n{self.time}')
        f.write(f'\n{self.tweet}')
        f.close()


