word =input()
colrow = int(input())
result = []
constant = (colrow-2)*2
cn = 1
if colrow >= 3:
    n = (colrow-3)*2 + 4
    result+= [word[k] for k in range(len(word)) if k%n==0]
    while constant >= 0:
        r = [word[k] for k in range(cn,len(word)) if ((k-cn)%n == 0 or n==0) and k < len(word)]
        l = [word[k+constant] for k in range(cn,len(word)) if ((k-cn)%n == 0 or n==0) and k+constant < len(word)]
        for k in range(max(len(r),len(l))):
            try :
                result.append(r[k])
            except:
                pass
            try : 
                result.append(l[k])
            except:
                pass
        cn +=1
        constant-=2
        if word[cn] == word[cn+constant] :
            break
        
    result+= list(word[colrow-1::((colrow-1)*2)])
    print("".join(result))

elif colrow == 2 :
    result+=[word[k] for k in range(len(word)) if k%2 == 0]
    result+=[word[k] for k in range(len(word)) if k%2 != 0]
    print(" ".join(result))

else:
    print(word if colrow == 1 else "Wrong no. of rows given.")

