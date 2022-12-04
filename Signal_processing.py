
from tkinter import *
import numpy as np
from numpy.fft import fft, ifft
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import scipy
from scipy import signal
import webbrowser
import math
import cmath
root = Tk()

root.title("Graphical Representation")
root.geometry("1100x650")

root.configure(background = '#393939')

# Main Application "Exit" and "About Developer Menu" opens a new tab on your default browser 
def main_exit():
    root.destroy()    

    
# New Window for 4 Point - (DIT) - FFT    
def open1():
#     new_window = Toplevel()
  
#     
#    new_window.geometry('900x700')
#    new_window.configure(background ='#393939')
#     Poster_1 = Label(new_window,text="___ Sine Function Representation ___",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
#     Poster_1.place(x=250,y=20)
#     Poster_11 = Label(new_window,text="Please enter the amplitude and Frequece",font=('Calibri',18),bg='#393939',fg='white')
#     Poster_11.place(x=220,y=60)
    plt.title('Sine wave')
    x_samples = np.arange(-10, 350, 50)

    freq_samples = np.random.random(x_samples.shape) * 1.5 + 0.5
    x = np.arange(0, 300, 0.1)

    dx = np.full_like(x, 0.1 )       # Change in x

    interpolation = interp1d(x_samples, freq_samples, kind='quadratic')
    freq = interpolation(x)

    x_plot = (freq * dx ).cumsum()    # Cumsum freq * change in x

    y = np.sin(x_plot)

    plt.plot(x, y, label="sin(freq(x) * x)")
    plt.plot(x, freq, label="freq(x)")
    plt.legend()
    plt.show()



    
# New Window for 4 Point - (DIF) - FFT      
def open2():
    time= np.arange(0, 20, 0.2);

    amplitude   = np.cos(time)
    plt.plot(time, amplitude)
    plt.title('Cosine wave')
    plt.xlabel('Time')
    plt.ylabel('Amplitude = cosine(time)')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='b')
    plt.show()
    
# New Window for 8 Point - (DIT) - FFT     
def open3():
    # Time period
    t = np.arange(0, 10, 0.01);
# Create a sine wave with multiple frequencies(1 Hz, 2 Hz and 4 Hz)
    a = np.sin(2*np.pi*t) + np.sin(2*2*np.pi*t) + np.sin(4*2*np.pi*t);

# Do a Fourier transform on the signal
    tx  = np.fft.fft(a);
    
# Do an inverse Fourier transform on the signal
    itx = np.fft.ifft(tx);

 # Plot the original sine wave using inverse Fourier transform
    plt.plot(t, a);

    plt.title("Sine wave plotted using inverse Fourier transform");

    plt.xlabel('Time')

    plt.ylabel('Amplitude')

    plt.grid(True)

    plt.show();
   
    
# New Window for 2 sine fft

def open4():
    
  
       
    new_window = Toplevel()
    new_window.title("Two Sine FFT ")
  
    new_window.geometry('900x700')
    new_window.configure(background ='#393939')
    
    
    num_04 = Label(new_window, text='Enter Sampling Frequency = ', font=('Calibri',18),bg='#393939',fg='white')
    num_04.place(x=30,y=180)
    fs = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    fs.place(x=340,y=180)
    
    num_4 = Label(new_window, text='Enter End Time period of Signal =', font=('Calibri',18),bg='#393939',fg='white')
    num_4.place(x=30,y=240)
    et = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    et.place(x=380,y=240)
    
    num_5 = Label(new_window, text='Enter Signal 1 Frequency =', font=('Calibri',18),bg='#393939',fg='white')
    num_5.place(x=30,y=300)
    s1 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    s1.place(x=380,y=300)
    
    num_6 = Label(new_window, text='Enter Signal 2 Frequency =', font=('Calibri',18),bg='#393939',fg='white')
    num_6.place(x=30,y=360)
    s2 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    s2.place(x=380,y=360)
    
    def submit():
   
       
       # How many time points are needed i,e., Sampling Frequency

        samplingFrequency = int(fs.get())

    # At what intervals time points are sampled
        samplingInterval       = 1 / samplingFrequency;
       
     # Begin time period of the signals
        beginTime           = 0;

     

    # End time period of the signals

        endTime = int(et.get()) 

     

    # Frequency of the signals

        signal1Frequency = int(s1.get())

        signal2Frequency = int(s2.get())

     

    # Time points

        time = np.arange(beginTime, endTime, samplingInterval);

     

    # Create two sine waves

        amplitude1 = np.sin(2*np.pi*signal1Frequency*time)

        amplitude2 = np.sin(2*np.pi*signal2Frequency*time)

     

    # Create subplot

        figure, axis = plt.subplots(4, 1)

        plt.subplots_adjust(hspace=1)

     

    # Time domain representation for sine wave 1

        axis[0].set_title('Sine wave for Signal 1 ')
       

        axis[0].plot(time, amplitude1)

        axis[0].set_xlabel('Time')

        axis[0].set_ylabel('Amplitude')

     

     

    # Time domain representation for sine wave 2

        axis[1].set_title('Sine wave for Signal 2 ')

        axis[1].plot(time, amplitude2)

        axis[1].set_xlabel('Time')

        axis[1].set_ylabel('Amplitude')

     

    # Add the sine waves

        amplitude = amplitude1 + amplitude2

     

    # Time domain representation of the resultant sine wave

        axis[2].set_title('Sine wave with multiple frequencies')

        axis[2].plot(time, amplitude)

        axis[2].set_xlabel('Time')

        axis[2].set_ylabel('Amplitude')

     

    # Frequency domain representation

        fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude

        fourierTransform = fourierTransform[range(int(len(amplitude)/2))] # Exclude sampling frequency

     

        tpCount     = len(amplitude)

        values      = np.arange(int(tpCount/2))

        timePeriod  = tpCount/samplingFrequency

        frequencies = values/timePeriod

     

    # Frequency domain representation

        axis[3].set_title('Fourier transform depicting the frequency components')

     

        axis[3].plot(frequencies, abs(fourierTransform))

        axis[3].set_xlabel('Frequency')

        axis[3].set_ylabel('Amplitude')

     

        plt.show()
    
    Poster_4 = Label(new_window,text="___ Two Sine FFT___",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_4.place(x=250,y=20)
    Poster_14 =Label(new_window,text=" Enter your frequency 1 & 2 and sampling frequency in Hz and Time period",font=('Calibri',18),bg='#393939',fg='white')
    Poster_14.place(x=60,y=60)
    Poster_114 = Label(new_window,text="",font=('Calibri',18),bg='#393939',fg='white')
    Poster_114.place(x=130,y=100) 
     
   
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)

    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300)
      
    
    


def open5():
    
    new_window = Toplevel()
    new_window.title("Sine sampling")
  
    new_window.geometry('900x700')
    new_window.configure(background ='#393939')
    num_0 = Label(new_window, text='Enter Frequency (max) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_0.place(x=30,y=180)
    f = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    f.place(x=330,y=180)
    
    num_1 = Label(new_window, text='Enter Sampling Frequency (rate)=', font=('Calibri',18),bg='#393939',fg='white')
    num_1.place(x=30,y=240)
    r = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    r.place(x=380,y=240)
    
  
#     num_2 = Label(new_window, text='Enter end Time period =', font=('Calibri',18),bg='#393939',fg='white')
#     num_2.place(x=30,y=300)
#     edt = Entry(new_window,width=8,fg='black',font=('Calibri',16))
#     edt.place(x=380,y=300)

    def submit():
      
        
#        f=20 # Hz
        fre=int(f.get())
       # endtime=int(edt.get())
        
        t = np.linspace(0, 0.50, 200)
        x1 = np.sin(2 * np.pi * fre * t)

        s_rate= int(r.get())
#       s_rate = 35 # Hz. Here the sampling frequency is less than the requirement of sampling theorem

        T = 1 / s_rate
        n = np.arange(0, 0.50 / T)
        nT = n * T
        x2 = np.sin(2 * np.pi * fre * nT) # Since for sampling t = nT.
        plt.figure(figsize=(10, 8))
        plt.suptitle("Sampling a Sine Wave of given frequency and sampling rate", fontsize=20)
       

        plt.subplot(2, 2, 1)
        plt.plot(t, x1, linewidth=3, label='SineWave of given frequency')
        plt.xlabel('time.', fontsize=15) 
        plt.ylabel('Amplitude', fontsize=15)
        plt.legend(fontsize=10, loc='upper right')

        plt.subplot(2, 2, 2)
        plt.plot(nT, x2, 'ro', label='Sample marks after resampling at given rate')
        plt.xlabel('time.', fontsize=15)
        plt.ylabel('Amplitude', fontsize=15)
        plt.legend(fontsize=10, loc='upper right')

        plt.subplot(2, 2, 3)
        plt.stem(nT, x2, 'm', label='Sample after resampling at given rate ')
        plt.xlabel('time.', fontsize=15)
        plt.ylabel('Amplitude', fontsize=15)
        plt.legend(fontsize=10, loc='upper right')

        plt.subplot(2, 2, 4)
        plt.plot(nT, x2, 'g-', label='Reconstructed Sine Wave')
        plt.xlabel('time.', fontsize=15)
        plt.ylabel('Amplitude', fontsize=15)
        plt.legend(fontsize=10, loc='upper right')

        plt.tight_layout()
        
        plt.show()
    
    Poster_1 = Label(new_window,text="___ Sine Sampling Funtion___",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_1.place(x=250,y=20)
    Poster_11 = Label(new_window,text=" Enter your frequency and sampling frequency in Hz ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_11.place(x=220,y=60)
    Poster_111 = Label(new_window,text=" ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_111.place(x=130,y=100) 
       
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)

    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300) 

       
   
def open6():
    new_window = Toplevel()
    new_window.title("4 - POINT (DIF) FFT Calculator ")
   
    new_window.geometry('900x700')
    new_window.configure(background ='#393939')
    
# Calculation/Math     
    def submit():
        sub1=Label(new_window,text='(Stage - 1)',font=('Calibri',18),bg='#393939',fg='white')
        sub1.place(x=350,y=140)
        sub2=Label(new_window,text='(Stage - 2)',font=('Calibri',18),bg='#393939',fg='white')
        sub2.place(x=670,y=140)
        
        s_0 = int(x_2.get()) + int(x_0.get())
        s_1 = int(x_3.get()) + int(x_1.get())
        s_2 = int(x_0.get()) - int(x_2.get())
        s_3 = int(x_1.get()) - int(x_3.get())
        ss_0 = s_1 + s_0
        ss_1 = s_0 - s_1
        ss_2 = (complex(s_3)*(-1j)) + s_2
        ss_3 = s_2 - (complex(s_3)*(-1j)) 
        
        stage_1_0=Label(new_window,text=str(s_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_0.place(x=400,y=180)        
        stage_1_1=Label(new_window,text=str(s_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_1.place(x=400,y=260)    
        stage_1_2=Label(new_window,text=str(s_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_2.place(x=400,y=340)        
        stage_1_3=Label(new_window,text=str(s_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_3.place(x=400,y=420) 
               
        stage_2_0=Label(new_window,text=str(ss_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_0.place(x=700,y=180)        
        stage_2_1=Label(new_window,text=str(ss_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_1.place(x=700,y=260)    
        stage_2_2=Label(new_window,text=str(ss_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_2.place(x=700,y=340)        
        stage_2_3=Label(new_window,text=str(ss_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_3.place(x=700,y=420)     

    # Sub-Application-2 Layout                                                    
    Poster_1 = Label(new_window,text="___ 4 - POINT (DIF) FFT ___",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_1.place(x=250,y=20)
    Poster_11 = Label(new_window,text=" Enter your 'X(n)' Sequence here",font=('Calibri',18),bg='#393939',fg='white')
    Poster_11.place(x=220,y=60)
    Poster_111 = Label(new_window,text=" Enter the Sequence  ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_111.place(x=130,y=100) 
       
    num_0 = Label(new_window, text='X(0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_0.place(x=30,y=180)
    x_0 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_0.place(x=90,y=180)        
    num_1 = Label(new_window, text='X(1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_1.place(x=30,y=260)
    x_1 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_1.place(x=90,y=260)       
    num_2 = Label(new_window, text='X(2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_2.place(x=30,y=340)
    x_2 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_2.place(x=90,y=340)    
    num_3 = Label(new_window, text='X(3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_3.place(x=30,y=420)    
    x_3 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_3.place(x=90,y=420)
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)
    
    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300) 
   

def open7():
    new_window = Toplevel()
    new_window.title("4 - POINT (DIT) FFT Calculator ")
  
    new_window.geometry('900x700')
    new_window.configure(background ='#393939')

# Calculation/Math               
    def submit():
        sub1=Label(new_window,text='(Stage - 1)',font=('Calibri',18),bg='#393939',fg='white')
        sub1.place(x=350,y=140)
        sub2=Label(new_window,text='(Stage - 2)',font=('Calibri',18),bg='#393939',fg='white')
        sub2.place(x=670,y=140) 
               
        s_0 = int(x_2.get()) + int(x_0.get())
        s_1 = int(x_0.get()) - int(x_2.get())
        s_2 = int(x_3.get()) + int(x_1.get())
        s_3 = int(x_1.get()) - int(x_3.get())        
        s_1_0 = s_0
        s_2_1 = s_1
        s_3_2 = s_2
        s_4_3 = s_3
        s_1_com = complex(s_1_0)
        s_2_com = complex(s_2_1)
        s_3_com = complex(s_3_2)
        s_4_com = complex(s_4_3)
        sf_1 =  s_3_2 + s_1_0
        sf_2 =  ((-1j*s_4_com) + s_2_com )
        sf_3 =  s_1_0 - s_3_2
        sf_4 =  (s_2_com - (-1j*s_4_com))
              
        stage_1_0=Label(new_window,text=str(s_1_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_0.place(x=400,y=180)        
        stage_1_1=Label(new_window,text=str(s_2_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_1.place(x=400,y=260)    
        stage_1_2=Label(new_window,text=str(s_3_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_2.place(x=400,y=340)        
        stage_1_3=Label(new_window,text=str(s_4_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_3.place(x=400,y=420)
                
        stage_2_0=Label(new_window,text=str(sf_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_0.place(x=700,y=180)        
        stage_2_1=Label(new_window,text=str(sf_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_1.place(x=700,y=260)    
        stage_2_2=Label(new_window,text=str(sf_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_2.place(x=700,y=340)        
        stage_2_3=Label(new_window,text=str(sf_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_3.place(x=700,y=420)
            
    # Sub-Application-1 Layout                                                    
    Poster_1 = Label(new_window,text="___ 4 - POINT (DIT) FFT ___",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_1.place(x=250,y=20)
    Poster_11 = Label(new_window,text=" Enter your 'X(n)' Sequence here",font=('Calibri',18),bg='#393939',fg='white')
    Poster_11.place(x=220,y=60)
    Poster_111 = Label(new_window,text="Enter the Sequence as it is ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_111.place(x=130,y=100)
    
    num_0 = Label(new_window, text='X(0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_0.place(x=30,y=180)
    x_0 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_0.place(x=90,y=180)
        
    num_1 = Label(new_window, text='X(1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_1.place(x=30,y=260)
    x_1 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_1.place(x=90,y=260)
       
    num_2 = Label(new_window, text='X(2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_2.place(x=30,y=340)
    x_2 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_2.place(x=90,y=340)
    
    num_3 = Label(new_window, text='X(3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_3.place(x=30,y=420)    
    x_3 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_3.place(x=90,y=420)
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)
    
    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300) 



def open8():
    new_window = Toplevel()
    new_window.title("8 - POINT (DIT) FFT Calculator")
    
    new_window.geometry('900x700')
    new_window.configure(background ='#393939')
    
# Calculation/Math    
    def submit():
        sub1=Label(new_window,text='(Stage - 1)',font=('Calibri',18),bg='#393939',fg='white')
        sub1.place(x=280,y=140)
        sub2=Label(new_window,text='(Stage - 2)',font=('Calibri',18),bg='#393939',fg='white')
        sub2.place(x=450,y=140)
        sub3=Label(new_window,text='(Stage - 3)',font=('Calibri',18),bg='#393939',fg='white')
        sub3.place(x=640,y=140)
        
        s_0 = int(x_4.get()) + int(x_0.get())
        s_1 = int(x_0.get()) - int(x_4.get())
        s_2 = int(x_6.get()) + int(x_2.get())
        s_3 = int(x_2.get()) - int(x_6.get())
        s_4 = int(x_5.get()) + int(x_1.get())
        s_5 = int(x_1.get()) - int(x_5.get())
        s_6 = int(x_7.get()) + int(x_3.get())
        s_7 = int(x_3.get()) - int(x_7.get())
        
        ss_0 = s_2 + s_0
        ss_1 = ((complex(s_3))*(-1j)) + s_1
        ss_2 = s_0 - s_2
        ss_3 = s_1 - ((complex(s_3))*(-1j))
        ss_4 = s_6 + s_4
        ss_5 = ((complex(s_7))*(-1j)) + s_5
        ss_6 = s_4 - s_6
        ss_7 = s_5 - ((complex(s_7))*(-1j)) 
        
        sss_0 = ss_4 + ss_0
        sss_1 = ((0.7071067812-0.7071067812j)*(complex(ss_5))) + ss_1
        sss_2 = ((complex(ss_6))*(-1j)) + ss_2
        sss_3 = ((-0.7071067812-0.7071067812j)*(complex(ss_7))) + ss_3
        sss_4 = ss_0 - ss_4
        sss_5 = ss_1 - ((0.7071067812-0.7071067812j)*(complex(ss_5)))
        sss_6 = ss_2 - ((complex(ss_6))*(-1j))
        sss_7 = ss_3 - ((-0.7071067812-0.7071067812j)*(complex(ss_7)))
        
        round_sss1=(round(sss_1.real,3)+round(sss_1.imag,3) * 1j)
        round_sss3=(round(sss_3.real,3)+round(sss_3.imag,3) * 1j)
        round_sss5=(round(sss_5.real,3)+round(sss_5.imag,3) * 1j)
        round_sss7=(round(sss_7.real,3)+round(sss_7.imag,3) * 1j)
        
        stage_1_0=Label(new_window,text=str(s_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_0.place(x=310,y=180)        
        stage_1_1=Label(new_window,text=str(s_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_1.place(x=310,y=220)    
        stage_1_2=Label(new_window,text=str(s_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_2.place(x=310,y=260)        
        stage_1_3=Label(new_window,text=str(s_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_3.place(x=310,y=300)
        stage_1_4=Label(new_window,text=str(s_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_4.place(x=310,y=340)        
        stage_1_5=Label(new_window,text=str(s_5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_5.place(x=310,y=380)    
        stage_1_6=Label(new_window,text=str(s_6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_6.place(x=310,y=420)        
        stage_1_7=Label(new_window,text=str(s_7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_7.place(x=310,y=460) 
        
        stage_2_0=Label(new_window,text=str(ss_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_0.place(x=470,y=180)        
        stage_2_1=Label(new_window,text=str(ss_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_1.place(x=470,y=220)    
        stage_2_2=Label(new_window,text=str(ss_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_2.place(x=470,y=260)        
        stage_2_3=Label(new_window,text=str(ss_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_3.place(x=470,y=300)
        stage_2_4=Label(new_window,text=str(ss_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_4.place(x=470,y=340)        
        stage_2_5=Label(new_window,text=str(ss_5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_5.place(x=470,y=380)    
        stage_2_6=Label(new_window,text=str(ss_6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_6.place(x=470,y=420)        
        stage_2_7=Label(new_window,text=str(ss_7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_7.place(x=470,y=460)  
        
        stage_3_0=Label(new_window,text=str(sss_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_0.place(x=660,y=180)        
        stage_3_1=Label(new_window,text=str(round_sss1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_1.place(x=660,y=220)    
        stage_3_2=Label(new_window,text=str(sss_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_2.place(x=660,y=260)        
        stage_3_3=Label(new_window,text=str(round_sss3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_3.place(x=660,y=300)
        stage_3_4=Label(new_window,text=str(sss_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_4.place(x=660,y=340)        
        stage_3_5=Label(new_window,text=str(round_sss5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_5.place(x=660,y=380)    
        stage_3_6=Label(new_window,text=str(sss_6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_6.place(x=660,y=420)        
        stage_3_7=Label(new_window,text=str(round_sss7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_7.place(x=660,y=460)   
      
    Poster_1 = Label(new_window,text="___ 8 - POINT (DIT) FFT ___",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_1.place(x=250,y=20)
    Poster_11 = Label(new_window,text="Hello User, Enter your 'X(n)' Sequence here",font=('Calibri',18),bg='#393939',fg='white')
    Poster_11.place(x=220,y=60)
    Poster_111 = Label(new_window,text=" Enter the Sequence  ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_111.place(x=130,y=100)
    
    #Sub-Application-3 Layout  
    num_0 = Label(new_window, text='X(0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_0.place(x=30,y=180)
    x_0 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_0.place(x=90,y=180)    
    num_1 = Label(new_window, text='X(1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_1.place(x=30,y=220)
    x_1 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_1.place(x=90,y=220)       
    num_2 = Label(new_window, text='X(2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_2.place(x=30,y=260)
    x_2 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_2.place(x=90,y=260)    
    num_3 = Label(new_window, text='X(3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_3.place(x=30,y=300)    
    x_3 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_3.place(x=90,y=300)    
    num_4 = Label(new_window, text='X(4) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_4.place(x=30,y=340)
    x_4 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_4.place(x=90,y=340)        
    num_5 = Label(new_window, text='X(5) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_5.place(x=30,y=380)
    x_5 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_5.place(x=90,y=380)      
    num_6 = Label(new_window, text='X(6) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_6.place(x=30,y=420)
    x_6 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_6.place(x=90,y=420)    
    num_7 = Label(new_window, text='X(7) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_7.place(x=30,y=460)    
    x_7 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_7.place(x=90,y=460) 
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)
    
    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300)

    

# New Window for 8 Point (DIF) FFT     
def open9():
    new_window = Toplevel()
    new_window.title("8 - POINT (DIF) FFT Calculator ")

    new_window.geometry('900x700')
    new_window.configure(background ='#393939')
    
    def submit():
        sub1=Label(new_window,text='(Stage - 1)',font=('Calibri',18),bg='#393939',fg='white')
        sub1.place(x=280,y=140)
        sub2=Label(new_window,text='(Stage - 2)',font=('Calibri',18),bg='#393939',fg='white')
        sub2.place(x=450,y=140)
        sub3=Label(new_window,text='(Stage - 3)',font=('Calibri',18),bg='#393939',fg='white')
        sub3.place(x=640,y=140)
        
        s_0 = int(x_4.get()) + int(x_0.get())
        s_1 = int(x_5.get()) + int(x_1.get())
        s_2 = int(x_6.get()) + int(x_2.get())
        s_3 = int(x_7.get()) + int(x_3.get())
        s_4 = int(x_0.get()) - int(x_4.get())
        s_5 = int(x_1.get()) - int(x_5.get())
        s_6 = int(x_2.get()) - int(x_6.get())
        s_7 = int(x_3.get()) - int(x_7.get())
        
        ss_0 = s_2 + s_0
        ss_1 = s_3 + s_1
        ss_2 = s_0 - s_2
        ss_3 = s_1 - s_3
        ss_4 = (((complex(s_6))*(-1j)) + (s_4))
        ss_5 = (((-0.7071067812-0.7071067812j)*(complex(s_7))) + ((0.7071067812-0.7071067812j)*(complex(s_5))))
        ss_6 = ((s_4) -  ((complex(s_6))*(-1j)))
        ss_7 = (((0.7071067812-0.7071067812j)*(complex(s_5))) - ((-0.7071067812-0.7071067812j)*(complex(s_7))))
        round_ss5=(round(ss_5.real,3)+round(ss_5.imag,3) * 1j)
        round_ss7=(round(ss_7.real,3)+round(ss_7.imag,3) * 1j)

        sss_0 = ss_1 + ss_0
        sss_1 = ss_0 - ss_1
        sss_2 = (complex(ss_3)*(-1j)) + ss_2
        sss_3 = ss_2 - (complex(ss_3)*(-1j))
        sss_4 = ss_5 + ss_4 
        sss_5 = ss_4 - ss_5
        sss_6 = (complex(ss_7)*(-1j)) + ss_6
        sss_7 = ss_6 - (complex(ss_7)*(-1j))
        round_sss4=(round(sss_4.real,3)+round(sss_4.imag,3) * 1j)
        round_sss5=(round(sss_5.real,3)+round(sss_5.imag,3) * 1j)
        round_sss6=(round(sss_6.real,3)+round(sss_6.imag,3) * 1j)
        round_sss7=(round(sss_7.real,3)+round(sss_7.imag,3) * 1j)
        
        stage_1_0=Label(new_window,text=str(s_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_0.place(x=310,y=180)        
        stage_1_1=Label(new_window,text=str(s_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_1.place(x=310,y=220)    
        stage_1_2=Label(new_window,text=str(s_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_2.place(x=310,y=260)        
        stage_1_3=Label(new_window,text=str(s_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_3.place(x=310,y=300)
        stage_1_4=Label(new_window,text=str(s_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_4.place(x=310,y=340)        
        stage_1_5=Label(new_window,text=str(s_5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_5.place(x=310,y=380)    
        stage_1_6=Label(new_window,text=str(s_6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_6.place(x=310,y=420)        
        stage_1_7=Label(new_window,text=str(s_7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_1_7.place(x=310,y=460) 
        
        stage_2_0=Label(new_window,text=str(ss_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_0.place(x=470,y=180)        
        stage_2_1=Label(new_window,text=str(ss_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_1.place(x=470,y=220)    
        stage_2_2=Label(new_window,text=str(ss_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_2.place(x=470,y=260)        
        stage_2_3=Label(new_window,text=str(ss_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_3.place(x=470,y=300)
        stage_2_4=Label(new_window,text=str(ss_4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_4.place(x=470,y=340)        
        stage_2_5=Label(new_window,text=str(round_ss5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_5.place(x=470,y=380)    
        stage_2_6=Label(new_window,text=str(ss_6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_6.place(x=470,y=420)        
        stage_2_7=Label(new_window,text=str(round_ss7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_2_7.place(x=470,y=460)  
        
        stage_3_0=Label(new_window,text=str(sss_0),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_0.place(x=660,y=180)        
        stage_3_1=Label(new_window,text=str(round_sss4),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_1.place(x=660,y=220)    
        stage_3_2=Label(new_window,text=str(sss_2),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_2.place(x=660,y=260)        
        stage_3_3=Label(new_window,text=str(round_sss6),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_3.place(x=660,y=300)
        stage_3_4=Label(new_window,text=str(sss_1),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_4.place(x=660,y=340)        
        stage_3_5=Label(new_window,text=str(round_sss5),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_5.place(x=660,y=380)    
        stage_3_6=Label(new_window,text=str(sss_3),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_6.place(x=660,y=420)        
        stage_3_7=Label(new_window,text=str(round_sss7),font=('Arial black',18),bg='#393939',fg='#FAF848')
        stage_3_7.place(x=660,y=460)      
        
    Poster_1 = Label(new_window,text="___ 8 - POINT (DIF) FFT ___",font=("Arial Rounded MT Bold",22),bg='#393939',fg='white')
    Poster_1.place(x=250,y=20)
    Poster_11 = Label(new_window,text=" Enter your 'X(n)' Sequence here",font=('Calibri',18),bg='#393939',fg='white')
    Poster_11.place(x=220,y=60)
    Poster_111 = Label(new_window,text=" Enter the Sequence  ",font=('Calibri',18),bg='#393939',fg='white')
    Poster_111.place(x=130,y=100)
    
    #Sub-Application-4 Layout  
    num_0 = Label(new_window, text='X(0) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_0.place(x=30,y=180)
    x_0 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_0.place(x=90,y=180)    
    num_1 = Label(new_window, text='X(1) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_1.place(x=30,y=220)
    x_1 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_1.place(x=90,y=220)       
    num_2 = Label(new_window, text='X(2) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_2.place(x=30,y=260)
    x_2 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_2.place(x=90,y=260)    
    num_3 = Label(new_window, text='X(3) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_3.place(x=30,y=300)    
    x_3 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_3.place(x=90,y=300)    
    num_4 = Label(new_window, text='X(4) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_4.place(x=30,y=340)
    x_4 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_4.place(x=90,y=340)        
    num_5 = Label(new_window, text='X(5) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_5.place(x=30,y=380)
    x_5 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_5.place(x=90,y=380)      
    num_6 = Label(new_window, text='X(6) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_6.place(x=30,y=420)
    x_6 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_6.place(x=90,y=420)    
    num_7 = Label(new_window, text='X(7) = ', font=('Calibri',18),bg='#393939',fg='white')
    num_7.place(x=30,y=460)    
    x_7 = Entry(new_window,width=8,fg='black',font=('Calibri',16))
    x_7.place(x=90,y=460) 
    
    submit_button=Button(new_window,text='Submit Values',font=('Aachen',18),bg='#85FF6A',fg='black',relief=RAISED,command=submit)
    submit_button.place(x=30,y=520,width=300)
    
    quit_1=Button(new_window,text='Quit App',font=('Aachen',18),bg='#FA4B48',fg='black',relief=RAISED,command=new_window.destroy)
    quit_1.place(x=550,y=520,width=300)
    

 
#Main Application Layout        
Posterlabel = Label(root, text = "_______ Graphical Representation _______",font=("Arial Rounded MT Bold", 22),bg ='#393939',fg = 'white')
Posterlabel.place(x=250,y=20)

Optionlabel = Label(root, text = "|| Choose the Operation you want to Perform ||",font=("Calibri", 20),bg ='#393939',fg = 'white')
Optionlabel.place(x=270,y=70)

numlabel1 = Label(root, text='(1)', font=('Calibri',18),bg='#393939',fg='white')
numlabel1.place(x=50,y=180)
button1 = Button(root, text = "Sine function ",font=("Aachen", 18), bg ='#FF643B', fg = 'black',relief = RAISED,command=open1)
button1.place(x=90,y=180)

numlabel2 = Label(root, text='(2)', font=('Calibri',18),bg='#393939',fg='white')
numlabel2.place(x=50,y=270)
button2 = Button(root, text = "Cos function",font=("Aachen", 18), bg ='#3ED6F6', fg = 'black',relief = RAISED,command=open2)
button2.place(x=90,y=270)

numlabel3 = Label(root, text='(3)', font=('Calibri',18),bg='#393939',fg='white')
numlabel3.place(x=50,y=360)
button3 = Button(root, text = "Sine wave using IFFT",font=("Aachen", 18), bg ='#D78AF9', fg = 'black',relief = RAISED, command=open3)
button3.place(x=90,y=360)

numlabel4 = Label(root, text='(4)', font=('Calibri',18),bg='#393939',fg='white')
numlabel4.place(x=50,y=450)
button4 = Button(root, text = "Two Sine wave FFT  ",font=("Aachen", 18), bg ='#91F96D', fg = 'black',relief = RAISED, command=open4)
button4.place(x=90,y=450)

numlabel6 = Label(root, text='(5)', font=('Calibri',18),bg='#393939',fg='white')
numlabel6.place(x=50,y=540)
button6 = Button(root, text = "Sine function Sampling ",font=("Aachen", 18), bg ='#E79DBB', fg = 'black',relief = RAISED, command=open5)
button6.place(x=90,y=540)

numlabel5 = Label(root, text='(6)', font=('Calibri',18),bg='#393939',fg='white')
numlabel5.place(x=450,y=180)
button5 = Button(root, text = "4 - POINT (DIF) FFT   ",font=("Aachen", 18), bg ='#DFC742', fg = 'black',relief = RAISED,command= open6)
button5.place(x=490,y=180)

numlabel7 = Label(root, text='(7)', font=('Calibri',18),bg='#393939',fg='white')
numlabel7.place(x=450,y=270)
button7 = Button(root, text = "4 - Point (DIT) FFT",font=("Aachen", 18), bg ='#DFC742', fg = 'black',relief = RAISED,command=open7)
button7.place(x=490,y=270)

numlabel8 = Label(root, text='(8)', font=('Calibri',18),bg='#393939',fg='white')
numlabel8.place(x=450,y=360)
button8 = Button(root, text = "8 - POINT (DIT) FFT",font=("Aachen", 18), bg ='#C2B9F5', fg = 'black',relief = RAISED, command=open8)
button8.place(x=490,y=360)

numlabel9 = Label(root, text='(9)', font=('Calibri',18),bg='#393939',fg='white')
numlabel9.place(x=450,y=450)
button9 = Button(root, text = "8 - POINT (DIF) FFT  ",font=("Aachen", 18), bg ='#C2B9F5', fg = 'black',relief = RAISED, command=open9)
button9.place(x=490,y=450)


exitbutton = Button(root, text = "Exit Application",font=("Aachen", 18), bg ='#A0C2C2', fg = 'black',relief = RAISED,command=main_exit)
exitbutton.place(x=580,y=680,width=250)
root.mainloop()


