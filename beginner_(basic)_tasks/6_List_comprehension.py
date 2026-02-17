if __name__ == '__main__':
        x = int(input())
        y = int(input())
        z = int(input())
        n = int(input())

def method1():
        print("using list comprehension")
        output =[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i + j + k) != n]
        print(output)
  
  #BEGINER STYLE  CODE
def method2():  
    

        # ૧. પહેલા એક ખાલી લિસ્ટ બનાવો
        results = []

        # ૨. i માટે લૂપ (0 થી x સુધી)
        for i in range(x + 1):
            # ૩. j માટે લૂપ (0 થી y સુધી)
            for j in range(y + 1):
                # ૪. k માટે લૂપ (0 થી z સુધી)
                for k in range(z + 1):
                    # ૫. શરત તપાસો: જો સરવાળો n ના હોય
                    if (i + j + k) != n:
                        # ૬. જો શરત સાચી હોય, તો લિસ્ટમાં [i, j, k] ઉમેરો
                        results.append([i, j, k])

        print("without use of list comprehension")
        print(results)
method1()
method2()
    # ૭. છેલ્લે આખું લિસ્ટ પ્રિન્ટ કરો