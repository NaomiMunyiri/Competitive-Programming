def countingValleys(steps, path):
    # Write your code here
    #use dic-step in string so convert to int
    valley=0
    current=0
    
    for i in range(steps):
        previous=current
        if path[i]=='U':
            current+=1
        if path[i]=='D':
            current-=1
        if current==0 and i!=0: #curret 0 and not at first step
            if previous==-1: #coming from val
                valley+=1
    return valley
        