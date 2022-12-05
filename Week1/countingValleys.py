def countingValleys(steps, path):
    # Write your code here
    valley=0
    current=0
    
    for i in range(steps):
        previous=current
        if path[i]=='U':
            current+=1
        if path[i]=='D':
            current-=1
        if current==0 and i!=0:
            if previous==-1:
                valley+=1
    return valley
        