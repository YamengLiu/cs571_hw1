def main():
    #load and process training set
    print "loading training data...\n"
    (trainingData, trainingLabel)=processFile("mnist_train.txt","mnist_train_labels.txt")
    print "training data loaded!\n"

    #learn perceptron from training set
    weight=train(trainingData, trainingLabel) 
    print "perceptron learned\n"
    
    #load and process testing set
    (testingData,testingLabel)=processFile("mnist_test.txt","mnist_test_labels.txt") 
    

    #calculate accuracy on testing set
    accuracy1=test(testingData, testingLabel, weight)     


    
    #get proportion of each dimension
    proportion=featureProportion(trainingData, trainingLabel, weight)
    print sorted(proportion)
    
    #threshold is the number of features we want to remain
    #change threshold and run experiment to find out the optimal value
    threshold=10
    #reduce features with proportion over threshold on testing sets
    print "select "+str(threshold)+" features"
    #(finishedData,finishedWeight)=featureReduction(proportion,testD,w,threshold)
    features=featureReduction(proportion,threshold)
    

    #calculate accuracy after feature reduction
    accuracy2=testwithfeatures(testingData, testingLabel, weight,features) 

    print "accuracy before feature reduction: "+ str(accuracy1)+"\n"
    print str(len(weight)-len(features))+" features are reduced:"
    print "accuracy after feature reduction "+ str(accuracy2)+"\n"

def processFile(data_Training, label_Training):
    #open training set
    fileData=open(data_Training) 
    fileLabel=open(label_Training) 

    #convert .txt file to lists of list
    data=[] 
    label=[] 

    for line in fileData:
        s=line.replace("\n","").split()
        data1=[] 
        for i in s:
            data1.append(int(i)) 
        data.append(data1) 

        
    for line in fileLabel :
        s=line.replace("\n","") 
        label.append(int(s)) 

    #filter out all data with label 0 or 1
    dataFinish=[]
    labelFinish=[]
    for i in range(0,len(label)):
        if( (label[i]==0) or (label[i]==1) ):
            dataFinish.append(data[i])
            labelFinish.append(label[i])
    
        
    return(dataFinish,labelFinish)

def train(data,label):
    #initialize
    w=[0]*len(data[0]) 

    mistakes=1
    #iteration
    while(mistakes != 0):
        mistakes=0 

        #calculate sum on each data
        for i in range(0,len(data)):
            sum=0 
            for j in range(0,len(w)):

                sum+=w[j]*data[i][j] 
            
            #revise the weight on wrong points
            if(sum>=0  and label[i]==0):
                for k in range(0,len(w)):
                
                    w[k]-=data[i][k] 
                    mistakes+=1 

            elif(sum<=0  and label[i]==1):
                for k in range(0,len(w)):
                
                    w[k]+=data[i][k] 
                    mistakes+=1 
    return w 

    
def test(data, label,w):  
    correctNumber=0 
    #calculate on each data point
    for i in range(0,len(data)):
        sum=0 
        for j in range(0,len(w)):
            sum+=w[j]*data[i][j] 

        if((sum>=0  and label[i]==1 )  or  (sum<0  and label[i]==0) ):
            correctNumber+=1 

    return float(correctNumber)/len(data)

def testwithfeatures(data, label,w,features):  
    correctNumber=0
    #calculate on each data point
    for i in range(0,len(data)):
        sum=0 
        for j in features:
            sum+=w[j]*data[i][j] 

        if((sum>=0  and label[i]==1 )  or  (sum<0  and label[i]==0) ):
            correctNumber+=1 

    return float(correctNumber)/len(data)


def featureProportion(data,label,weight):
    length=len(data)
    width=len(weight)
    feature=[]
    for i in range(0,width):
        sum=0
        for j in range(0,length):
            if(label[j]==0):
                sum-=data[j][i]*weight[i]
            else:
                sum+=data[j][i]*weight[i]
        feature.append(sum)
    return feature

def featureReduction(l,a):
    width=len(l)
    
    p=[]
    for i in range(0, width):
        q=[]
        q.append(l[i])
        q.append(i)
        p.append(q)

    pNew=sorted(p,key=lambda s:-s[0])

    index=[]
    for i in range(0,a):
        index.append(pNew[i][1])
    return index



main()


