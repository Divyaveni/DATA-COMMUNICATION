import numpy as np
import matplotlib.pyplot as plt

while (True):
    print("\n 1.) PAM\n", "2.) PWM\n","3.) Message Signal\n")

    n = int(input())
    if(n==1):
        percent = float(input('Enter percentage : '))
        TimePeriod = float(input('Enter time period : '))
        Cycles = int(input('Enter number of cycles : '))
        dt = 0.01

        t = np.arange(0,Cycles*TimePeriod,dt)
        pam =  (t%TimePeriod) < (TimePeriod*percent/100)

        x = np.linspace(-10,10,len(pam))
        y = (np.sin(x))

        y[pam == 0] = 0

        plt.plot(t,y)

        plt.ylim([-3,3])
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.grid()
        plt.show()
    elif (n==2):
        percent = float(input('Enter percentage : '))
        TimePeriod = float(input('Enter time period : '))
        Cycles = int(input('Enter number of cycles : '))
        dt = 0.01

        x = np.arange(0, Cycles * TimePeriod, dt)

        y = np.zeros_like(x)  # makes array of zeros of the same length as x
        npts = TimePeriod / dt

        i = 0
        while i * dt < Cycles * TimePeriod:
            if (i % npts) / npts < percent / 100.0:
                y[i] = 1
            i = i + 1

        plt.plot(x, y, '.-')
        plt.ylim([-.1, 1.1])
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.grid()
        plt.show()
    elif (n==3):
        '''
        Sample Input
        25
        2
        1
        '''
        Ac = 1
        fc = int(input('Enter carrier frequency n : '))
        fm = int(input('Enter message frequency : '))  # fm<fc
        m = float(input('Enter modulation index : '))
        Am = m * Ac

        t1 = np.arange(0, 1, 0.001)
        y1 = np.sin(2 * np.pi * fm * t1)  # message signal
        y2 = np.sin(2 * np.pi * fc * t1)  # carrier signal
        eq = (1 + m * y1) * (Ac * y2)

        plt.plot(t1, y1)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()