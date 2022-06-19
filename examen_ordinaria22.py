import re
import datetime
class userAccount:
    def __init__(self,alias,email,tweets,timeline,seguidores):
        if isinstance(alias,str):
            self.alias=alias
        else:
            self.alias="alias"
        if re.search(".*@.*\..*", email)==None or email=="":
            raise Exception("correo electronico debe tener formato xxx@xxx.xx: ")
        else:
            self.email=email
        self.tweets=tweets

        if type(seguidores)!=list:
            raise Exception ("debe ser una lista")
        else:
            self.seguidores=seguidores

        self.timeline=timeline
    def get_seguidores(self):
        for i in range(len(self.seguidores)):
            return self.seguidores[i].alias

    def follow(self,user):
        user.seguidores.append(self)

    def tweet(self,post):
        f=open(self.tweets,"w")
        f.write(f"\n {post}")
        f.close()


manolo=userAccount("manolo","manolo@j.j","tweets4.txt","tweets5.txt",[])
pepe=userAccount("pepe","pepe@j.j","tweets.txt","tweets1.txt",[])
javi=userAccount("javi","javi@j.j","tweets2.txt","tweets3.txt",[])
pepe.follow(javi)
manolo.follow(pepe)
javi.follow(pepe)
manolo.follow(javi)


javi.tweet("hola que tal soy nuevo")
print(javi.seguidores)
print(pepe.seguidores)

class tweet:
    def __init__(self,fichero,time,tweet,user):
        if len(time)==8:
            fecha_apertura=datetime.datetime.strptime(fecha_apertura,"%d%m%Y")
            self.time=time
        else:
            raise Exception("fecha no existe")
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
            raise Exception("tweet demasiado largo")
        self.user1=user1
        self.user2=user2

    def comenzar_coversacion(self):
        f=open(self.fichero,"w")
        f.write(f'\n{self.time}')
        f.write(f'\n{self.tweet}')
        f.close()


