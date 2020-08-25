import  pygame
class Handler:
    def __init__(self):
        self.__succesor__ = None
    
    def set_succesor(self, succesor):
        self.__succesor__ = succesor

    def handler_request(self, score):
        pass


class HandlerOptionOne(Handler):

    def handler_request(self, score):
        if score >= 0 and score < 6:
            
            scenario = pygame.image.load("images\Interface\Scenes\scene_Workspace.png").convert()
            return scenario
        else:
            return self.__succesor__.handler_request(score)
           


class HandlerOptionTwo(Handler):

    def handler_request(self, score):
        if score >= 6 and score <13:
            scenario = pygame.image.load("images\Interface\Scenes\scene-02.png").convert()
            return scenario
        else:
           
            return self.__succesor__.handler_request(score)
            
    
class HandlerOptionThree(Handler):

    def handler_request(self, score):
        if score >= 13 and score < 20:
            scenario = pygame.image.load("images\Interface\Scenes\scene-03.png").convert()
            return scenario
        else:
            return self.__succesor__.handler_request(score)


class HandlerOptionFour(Handler):

    def handler_request(self, score):
        if score >= 20:
            scenario = pygame.image.load("images\Interface\Scenes\scene-04.png")
            return scenario
        else:
            return scenario

class HandlerOptionDefault(Handler):

    def handler_request(self, score):
        print("Opción no valida")


class ChainFloor():        
    
    def operacion(self,countFloor):

        scenarios = [HandlerOptionOne(), HandlerOptionTwo(), HandlerOptionThree(), 
                    HandlerOptionFour(),HandlerOptionDefault()]

        for i in range(len(scenarios)-1):
            
            scenarios[i].set_succesor(scenarios[i+1])
            
        return scenarios[0].handler_request(countFloor)
        
    


