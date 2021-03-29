class Container:
    def __init__(self,name:str,volume:int,current_volume:int,pout_out:int=100):
        self.__name=name
        self.__volume=volume
        self.current_volume=current_volume
        self.pour_out=pout_out

    def pour_out_liquid(self):
        if self.current_volume>0:
            self.current_volume-=self.pour_out
            return self.pour_out

        else:
            print(f'{self.__name} пуст')
            return 0

    def pour_liquid(self,volume:int):
        if self.current_volume+volume<=self.__volume:
            self.current_volume+=volume
        else:
            print(f'{self.__name} полон')

    def info(self):
        print(f'{self.__name} = {self.current_volume}')



def main():
    jug = Container('jug', 1000, 1000)
    glass = Container('glass', 200, 0, 50)
    i=0
    while i<15:
        jug.info()
        glass.info()
        glass.pour_liquid(jug.pour_out_liquid())
        i+=1

if __name__=='__main__':
    main()