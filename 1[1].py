import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
plt.style.use('dark_background')
plt.rcParams['figure.figsize']=(20,3)
bit_seq=input("Enter the bit sequence: ")
    
def UnipolarNRZ(bit_seq):
    t=[]
    amp=[]
    dt = {'1':5, '0':0}

    for i in range(0, len(bit_seq)+1):
        t.append(i)

    for i in range(0, len(bit_seq)):
        amp.append(dt[bit_seq[i]])
    amp.append(0)

    plt.figure()
    plt.hlines(0, t[0], t[len(t)-1]+1, colors='#ffb300', linewidth=5.0)
    plt.plot(t, amp, drawstyle='steps-post', linewidth=5.0, color='#00ffa2')
    plt.xticks(t)
    plt.yticks([0, 5])
    plt.grid(b=True, color='#ffb300', linestyle='--', linewidth=2.0, axis='x')
    plt.show()

def UnipolarRZ(bit_seq):
    t=[]
    amp=[]

    for i in range(0, len(bit_seq)+1):
        t.append(i)
        if bit_seq[i]=='1':
            t.append(i+0.5)

    for i in range(0, len(bit_seq)):
        if bit_seq[i]=='0':
            amp.append(0)
        else:
            amp.append(5)
            amp.append(0)
    amp.append(0)

    plt.figure()
    plt.hlines(0, t[0], t[len(t)-1]+1, colors='#ffb300', linewidth=5.0)
    plt.plot(t, amp, drawstyle='steps-post', linewidth=5.0, color='#00ffa2')
    plt.xticks(t)
    plt.yticks([0, 5])
    plt.grid(b=True, color='#ffb300', linestyle='--', linewidth=2.0, axis='x')
    plt.show()
    
def PolarNRZL(bit_seq):
    t=[]
    amp=[]
    dt = {'1':5, '0':-5}

    for i in range(0, len(bit_seq)+1):
        t.append(i)

    for i in range(0, len(bit_seq)):
        amp.append(dt[bit_seq[i]])
    amp.append(0)

    plt.figure()
    plt.hlines(0, t[0], t[len(t)-1]+1, colors='#ffb300', linewidth=5.0)
    plt.plot(t, amp, drawstyle='steps-post', linewidth=5.0, color='#00ffa2')
    plt.xticks(t)
    plt.yticks([0, 5, -5])
    plt.grid(b=True, color='#ffb300', linestyle='--', linewidth=2.0, axis='x')
    plt.show()

def PolarNRZI(bit_seq):
    t=[]
    amp=[]

    for i in range(0, len(bit_seq)+1):
        t.append(i)
    
    prev = -5
    
    for i in range(0, len(bit_seq)):
        if  bit_seq[i]=='1':
            if prev==5:
                amp.append(-5)
                prev=-5
            else:
                amp.append(5)
                prev=5
        else:
            amp.append(prev)
    amp.append(0)

    plt.figure()
    plt.hlines(0, t[0], t[len(t)-1]+1, colors='#ffb300', linewidth=5.0)
    plt.plot(t, amp, drawstyle='steps-post', linewidth=5.0, color='#00ffa2')
    plt.xticks(t)
    plt.yticks([0, 5, -5])
    plt.grid(b=True, color='#ffb300', linestyle='--', linewidth=2.0, axis='x')
    plt.show()

def PolarRZ(bit_seq):
    t=[]
    amp=[]
    dt = {'1':5, '0':-5}

    for i in range(0, len(bit_seq)):
        t.append(i)
        t.append(i+0.5)
    t.append(i+1)

    for i in range(0, len(bit_seq)):
        amp.append(dt[bit_seq[i]])
        amp.append(0)
    amp.append(0)

    plt.figure()
    plt.hlines(0, t[0], t[len(t)-1]+1, colors='#ffb300', linewidth=5.0)
    plt.plot(t, amp, drawstyle='steps-post', linewidth=5.0, color='#00ffa2')
    plt.xticks(t)
    plt.yticks([0, 5, -5])
    plt.grid(b=True, color='#ffb300', linestyle='--', linewidth=2.0, axis='x')
    plt.show()

def Manchester(bit_seq):
    t=[]
    amp=[]

    for i in range(0, len(bit_seq)):
        t.append(i)
        t.append(i+0.5)
    t.append(i+1)

    for i in range(0, len(bit_seq)):
        if bit_seq[i]=='0':
            amp.append(-5)
            amp.append(5)
        else:
            amp.append(5)
            amp.append(-5)
    amp.append(0)

    plt.figure()
    plt.hlines(0, t[0], t[len(t)-1]+1, colors='#ffb300', linewidth=5.0)
    plt.plot(t, amp, drawstyle='steps-post', linewidth=5.0, color='#00ffa2')
    plt.xticks(t)
    plt.yticks([0, 5, -5])
    plt.tight_layout(pad=3.0)
    plt.grid(b=True, color='#ffb300', linestyle='--', linewidth=2.0, axis='x')
    plt.show()

def DifferentialManchester(bit_seq):
    t=[]
    amp=[]

    for i in range(0, len(bit_seq)):
        t.append(i)
        t.append(i+0.5)
    t.append(i+1)
    
    prev=5
    for i in range(0, len(bit_seq)):
        if bit_seq[i]=='0':
            if prev==5:
                amp.append(-5)
                amp.append(5)
                prev=5
            else:
                amp.append(5)
                amp.append(-5)
                prev=-5
        else:
            if prev==5:
                amp.append(5)
                amp.append(-5)
                prev=-5
            else:
                amp.append(-5)
                amp.append(5)
                prev=5
                
    amp.append(0)

    plt.figure()
    plt.hlines(0, t[0], t[len(t)-1]+1, colors='#ffb300', linewidth=5.0)
    plt.plot(t, amp, drawstyle='steps-post', linewidth=5.0, color='#00ffa2')
    plt.xticks(t)
    plt.yticks([0, 5, -5])
    plt.tight_layout(pad=3.0)
    plt.grid(b=True, color='#ffb300', linestyle='--', linewidth=2.0, axis='x')
    plt.show()

def BipolarAMI(bit_seq):
    t=[]
    amp=[]

    for i in range(0, len(bit_seq)+1):
        t.append(i)
    
    prev=-5
    for i in range(0, len(bit_seq)):
        if bit_seq[i]=='1':
            if prev==5:
                amp.append(-5)
                prev=-5
            else:
                amp.append(5)
                prev=5
        else:
            amp.append(0)
    amp.append(0)

    plt.figure()
    plt.hlines(0, t[0], t[len(t)-1]+1, colors='#ffb300', linewidth=5.0)
    plt.plot(t, amp, drawstyle='steps-post', linewidth=5.0, color='#00ffa2')
    plt.xticks(t)
    plt.yticks([-5,0, 5])
    plt.grid(b=True, color='#ffb300', linestyle='--', linewidth=2.0, axis='x')
    plt.show()

def BipolarPseudoternary(bit_seq):
    t=[]
    amp=[]

    for i in range(0, len(bit_seq)+1):
        t.append(i)
    
    prev=-5
    for i in range(0, len(bit_seq)):
        if bit_seq[i]=='0':
            if prev==5:
                amp.append(-5)
                prev=-5
            else:
                amp.append(5)
                prev=5
        else:
            amp.append(0)
    amp.append(0)

    plt.figure()
    plt.hlines(0, t[0], t[len(t)-1]+1, colors='#ffb300', linewidth=5.0)
    plt.plot(t, amp, drawstyle='steps-post', linewidth=5.0, color='#00ffa2')
    plt.xticks(t)
    plt.yticks([-5,0, 5])
    plt.grid(b=True, color='#ffb300', linestyle='--', linewidth=2.0, axis='x')
    plt.show()

def main():
    loop=True

    while loop:
        print("Choose the type of encoding:- ")
        print("1. Unipolar NRZ")
        print("2. Unipolar RZ")
        print("3. Polar-NRZ-L")
        print("4. Polar-NRZ-I")
        print("5. Polar-RZ")
        print("6. Manchester")
        print("7. Differential Manchester")
        print("8. Bipolar AMI")
        print("9. Bipolar Pseudoternary")
        print("10. Exit")

        option=int(input("Enter your choice>>> "))

        if option==1:
            UnipolarNRZ(bit_seq)
        
        elif option==2:
            UnipolarRZ(bit_seq)

        elif option==3:
            PolarNRZL(bit_seq)

        elif option==4:
            PolarNRZI(bit_seq)

        elif option==5:
            PolarRZ(bit_seq)

        elif option==6:
            Manchester(bit_seq)

        elif option==7:
            DifferentialManchester(bit_seq)

        elif option==8:
            BipolarAMI(bit_seq)

        elif option==9:
            BipolarPseudoternary(bit_seq)  
        else:
            loop=False  
main()