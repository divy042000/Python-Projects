from numpy import*

mat=array([['0','0','0'],['0','0','0'],['0','0','0']])

def number_to_string(argument,choice):
    match argument:
        case 0:
           if(choice==1):
             mat[0][0]='X'
           else:
             mat[0][0]='O'
             return mat[0][0]
        case 1:
           if(choice==1):
             mat[0][1]='X'
           else:
             mat[0][1]='O'
             return mat[0][1]
        case 2:
            if(choice==1):
             mat[0][0]='X'
            else:
             mat[0][0]='O'
             return mat[0][2]
            
        case default:
            return "something"
 
 
if __name__ == "__main__":
    argument = 1
    choice=0
    print(number_to_string(argument,choice))
    print (mat)