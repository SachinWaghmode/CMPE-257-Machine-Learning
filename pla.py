from random import randint
import matplotlib.pyplot as plt

class PerceptronLearner:
    dataset=[]
    vals=[]
    w=[]
    threshold=0
    step=0
    updates=0
    minx=0
    maxx=0
    def __init__(self, dataset,values,weights,threshold,step,minx,maxx):
        self.dataset=dataset
        self.vals=values
        self.w=weights
        self.threshold=threshold
        self.step=step
        self.minx=minx
        self.maxx=maxx

    def alterInput(self,step, i):
        self.threshold=round(self.threshold+step*self.vals[i],3)
        for j in range(0,len(self.w)):
            self.w[j]=round(self.w[j]+step*self.vals[i]*self.dataset[i][j],2)

    def classify(self,xvector,val):
        score=0;
        score+=self.threshold
        for i in range(0,len(xvector)):
            score+=xvector[i]*self.w[i]

        if ((score>0 and val>0) or (score<=0 and val<=0)):
            return True

        
        return False


    def train(self):
        while(True):
            error=0
            for i in range(0,len(self.dataset)):
                if(self.classify(self.dataset[i],self.vals[i])==False):
                    error=1
                    self.updates = self.updates + 1
                    self.alterInput(self.step,i)

            if(error == 0):
                break



    def plot(self):
        xs = []
        ys = []

        for i in range(0, len(self.dataset)):
            if (self.vals[i] > 0):
                xs.append(self.dataset[i][0])
                ys.append(self.dataset[i][1])

        plt.scatter(xs, ys, color='Green')

        xs = []
        ys = []

        for i in range(0, len(self.dataset)):
            if (self.vals[i] < 0):
                xs.append(self.dataset[i][0])
                ys.append(self.dataset[i][1])

        plt.scatter(xs, ys, color='Purple')
        length = self.maxx

        xcoord = [length]
        ycoord = [-(length * self.w[0] +self.threshold) / self.w[1]]

        length=-self.minx
        xcoord.append(-1 * length)
        ycoord.append(-(self.threshold - length * self.w[0]) / self.w[1])

        plt.plot(xcoord, ycoord, color='black')

        # plt.show()

        length = self.maxx

        xcoord = [length]
        ycoord = [10-(length * self.w[0]  + self.threshold) / self.w[1]]

        length = -self.minx
        xcoord.append(-1 * length)
        ycoord.append(-10-(self.threshold - length * self.w[0]) / self.w[1])

        plt.plot(xcoord, ycoord, color='gray')

        plt.show()

def main():

    dataset=[]
    minx=4000
    maxx=0
    for i in range(0,10) :
        pair=[]
        weight=randint(400, 500)
        height=randint(400, 500)
        pair.append(weight)
        pair.append(height)
        if(weight<minx):
            minx=weight
        if(weight>maxx):
            maxx=weight
        dataset.append(pair)


    for i in range(0,10) :
        pair = []
        weight=randint(540, 700)
        height=randint(300, 440)
        pair.append(weight)
        pair.append(height)
        if (weight < minx):
            minx = weight
        if (weight > maxx):
            maxx = weight
        dataset.append(pair)
    print "Training Dataset   :  ", dataset

    vals = [1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    print "Matching values    :   ", vals

    w = []
    x1=randint(-10,10)
    x2=randint(-10,10)
    print "value of x1 : ", x1
    print "value of x2 : ", x2

    w.append(x1)
    w.append(x2)

    print "value of w  : ", w

    threshold=randint(-5,5)
    print "value of threshold : ", threshold
    step = 6



    pla=PerceptronLearner(dataset,vals,w,threshold,step,minx,maxx) 

    pla.train()
    pla.plot()

    print "Total updates :",pla.updates


if __name__ == "__main__":
    main()
