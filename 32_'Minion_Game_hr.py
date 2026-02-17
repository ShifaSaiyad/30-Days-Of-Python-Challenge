def minion_game(string):
    # your code goes here
    string = string.upper()
    vowels = "AEIOU"
    sturat_score = 0
    kevin_score = 0
    n = len(string)
    
    for i in range(n):
        if string[i] in vowels:
            kevin_score += (n-i)
        else:
            sturat_score += (n-i)
        
    if sturat_score > kevin_score:
        print("Stuart", sturat_score)
    elif sturat_score < kevin_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")
        
                 
            

if __name__ == '__main__':
    s = input()
    minion_game(s)