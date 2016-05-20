class Node():
    def __init__(self,name,children,alpha,beta,value,isMax=True):
        self.name=name
        self.children=children
        self.alpha=alpha
        self.beta=beta
        self.value=value
        self.isMax=isMax

    def mkBranch(self,num):
        for i in range(num):
            self.children.append(Node(i,[],None,None,None,not(self.isMax)))
            
    def lstChildren(self):
        print(self.name)
        for child in self.children:
            if type(child) is int:
                print(child)
            else:
                child.lstChildren()

    def prune(self,child):
        for kid in self.children:
            if (kid.name==child):
                self.children.remove(kid)
            else:
                kid.prune(child)
                
    global pName
    pName=''
    def getValue(self):
        global pName
        #print(self.name)
        for child in self.children:
            if (self.isMax==True):
                if self.value==None:
                    self.value=float("-inf")
                child.alpha=max(self.value,self.alpha)
                child.beta=self.beta
                
            elif (self.isMax==False):
                if self.value==None:
                    self.value=float("inf")
                child.beta=min(self.value,self.beta)
                child.alpha=self.alpha
                
            child.getValue()

            if self.isMax==True:
                self.value=max(list((child.value) for child in self.children))
                self.alpha=self.value
                if child.value>self.beta:
                    pName=self.name
                    #print('Pruning at '+pName)
                    return pName
                
            elif self.isMax==False:
                self.value=min(list((child.value) for child in self.children))
                self.beta=self.value
                if child.value < self.alpha:
                    pName=self.name
                    #print('Pruning at '+pName)
                    return pName
        if pName in list((child.name for child in self.children)):
            self.prune(pName)
            #print('yes')

        #print(self.name,self.value,self.alpha,self.beta)

    def nextMove(self):
        self.getValue()
        #print('Choose '+self.children[len(self.children)-1].name)
        return self.children[len(self.children)-1].name


#example tree for testing
tree=Node('A',
          [Node('B',
                [Node('C',
                      [Node('F',[],None,None,13,False),
                       Node('G',[],None,None,12,False)]
                      ,None,None,None,True),
                 Node('D',
                      [Node('H',[],None,None,15,False),
                       Node('I',[],None,None,7,False)]
                      ,None,None,None,True)],
                None,None,None,False),
           Node('E',
                [Node('J',[],None,None,0,True),
                 Node('K',[],None,None,120,True)]
                ,None,None,None,False)],
          float("-inf"),float("inf"),float("-inf"),True)
