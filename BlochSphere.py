import qiskit
from qiskit.visualization import visualize_transition
import numpy as np
import tkinter
from qiskit import QuantumCircuit
from tkinter import LEFT, END, DISABLED, NORMAL
import warnings
warnings.filterwarnings('ignore')


# Define window
root = tkinter.Tk()
root.title('Quantum Glasses')

#set the icon
icon = tkinter.PhotoImage(file="logo3.png")
# Set it as the window icon.
root.iconphoto(True, icon)
root.geometry('450x430')
root.resizable(0,0)

# Define the colors and fonts
background = '#2c94c8'
buttons = '#834558'
special_buttons='#bc3454'
button_font= ('Arial',18)
display_font= ('Arial',32)

# Define the frames
display_frame = tkinter.LabelFrame(root)
button_frame= tkinter.LabelFrame(root,bg='black')
display_frame.pack()
button_frame.pack(fill='both',expand=True)

# Initialise the Quantum Circuit
def initialize_circuit():
    """
    Intialize the Quantum Circuit
    
    """
    global circuit
    circuit = QuantumCircuit(1)

initialize_circuit()
theta = 0

#Display the gate pressed
def display_gate(gate_input):
    """
    Displays the corresponding gate pressed for operation
    if no of gate pressed exceed 10 all buttons gets disabled
    """
    display.insert(END,gate_input)
    # Check if numberof operations has reached 10 then disable all the buttons
    input_gates = display.get()
    num_gates = len(input_gates)
    list_input_gates = list(input_gates)
    search_word = ['R','D']
    
    count_cdouble_valued_gates = [list_input_gates.count(i) for i in search_word]
    num_gates -= sum(count_cdouble_valued_gates)
    
    if num_gates ==10:
        gates = [x_button,y_button,z_button,Rx_button,Ry_button,Rz_button,s_button,sd_button,t_button,td_button,Hedmard]
        for gate in gates:
            gate.configure(state=DISABLED)

def change_theta(num,window,circuit,key):
    """"
    Changes the global variable theta and destroy the window
    """
    global theta
    theta = num*np.pi
    if key == 'x':
        circuit.rx(theta,0)
        theta= 0
    elif key == 'y':
        circuit.ry(theta,0)
        theta= 0
    else :
        circuit.rz(theta,0)
        theta=0 
    window.destroy()


def user_input(circuit, key):
    """
    Take the user input for rotation angle for parametrized
    rotaion gates Rx, Ry and Rz
    """
    # Intialize and defines the properties of window
    get_input = tkinter.Tk()
    get_input.title = (' Get Theta')
    get_input.geometry = ('360x160')
    get_input.resizable(0,0)
    
    val1 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=('Arial',10),text= 'PI/4',command=lambda:change_theta(0.25,get_input,circuit,key))
    val1.grid(row=0,column=0)
    
    val2 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=('Arial',10),text= 'PI/2',command=lambda:change_theta(0.50,get_input,circuit,key))
    val2.grid(row=0,column=1)
    
    val3 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=('Arial',10),text= 'PI',command=lambda:change_theta(1.00,get_input,circuit,key))
    val3.grid(row=0,column=2)
    
    val4 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=('Arial',10),text= '2*PI',command=lambda:change_theta(2.00,get_input,circuit,key))
    val4.grid(row=0,column=3)
    
    nval1 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=('Arial',10),text= '-PI/4',command=lambda:change_theta(-0.25,get_input,circuit,key))
    nval1.grid(row=1,column=0)
    
    nval2 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=('Arial',10),text= '-PI/2',command=lambda:change_theta(-0.50,get_input,circuit,key))
    nval2.grid(row=1,column=1)
    
    nval3 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=('Arial',10),text= '-PI',command=lambda:change_theta(-1.00,get_input,circuit,key))
    nval3.grid(row=1,column=2)
    
    nval4 = tkinter.Button(get_input,height=2,width=10,bg=buttons,font=('Arial',10),text= '-2*PI',command=lambda:change_theta(-2.00,get_input,circuit,key))
    nval4.grid(row=1,column=3)
    
    text_object = tkinter.Text(get_input, height=20,width=20,bg='light cyan')
    
    note = """"
    GIVE THE VALUE OF THETA 
    """
    text_object.grid(sticky='WE', columnspan=4)
    text_object.insert(END,note)

    get_input.mainloop()
    
# Error handling for visualization
def visualization_circuit(circuit,window):
    """"
    Visualize the single qubit rotation corresponding to applied gate in separate tkinter window
    Handles any possible visualtion error 
    """
    try:
        visualize_transition(circuit=circuit)
    except:
        qiskit.visualization.exceptions.VisualizationError: window.destroy()
                    

# Defines function of clear buttuon
def clear():
    """"
    Clear the display !
    Re- instialize the Quantum circuit for freash calculation
    check if buttons are disable, if so, then enables them
    """
    # Clear the display
    display.delete(0,END)
    
    #check if buttons are disable, if so, then enables them
    if x_button['state'] == DISABLED:
      gates = [x_button,y_button,z_button,Rx_button,Ry_button,Rz_button,s_button,sd_button,t_button,td_button,Hedmard] 
      for gate in gates :
          gate.config(state=NORMAL) 



# Define Functions of buttons
def about():
    """
    Displays the info about the Projects
    """
    info= tkinter.Tk()
    info.title('About')
    info.geometry('650x470')
    info.resizable(0,0)
    
    text= tkinter.Text(info,height=20,width=20)
    
    #Create label
    label = tkinter.Label(info,text ='About Quantum Glasses:')
    label.config(font= ('Arial',14))
    
    text_to_display = """
    About : Visualization tool for Single Qubit Bloch Sphere
    
    Created by : Chanchal Mandal
    Tool Used :  Python, Tkinter, Qiskit
    
    Info about the gates button and corresponding qiskit commands
    
    X = Flips the state of qubits                                  circuit.x()
    Y = Flips the state vector about Y axis                        circuit.y()
    Z = Flips the pkase by PI radians                              circuit.z()
    Rx = Parametrized rotation about X axis                        circuit.rx()
    Ry = Parametrized rotation about y axis                        circuit.ry()
    Rz = Parametrized rotation about z axis                        circuit.rz()
    S = Rotates the state vector about z axis by PI/2 radian       circuit.s()
    T = Rotates the state vector about z axis by PI/4 radian       circuit.t()
    Sd = Rotates the state vector about z axis by -PI/2 radian     circuit.sdg()
    Td = Rotates the state vector about z axis by -PI/4 radian     circuit.tdg()
    H = Creates the state of superposition                         circuit.h()
    
    For Rx, Ry and Rz
    theta(rotation angle) allowed in the app is in range [-2*PI.2*PI]
    
    In case of app visualization, the app closes automatically
    This shpws that visualization is not possible
    
    At a time, only 10 visulization are possible
    """
    label.pack()
    text.pack(fill='both', expand =True)
    
    text.insert(END,text_to_display)
    
    info.mainloop()


# define the display frame Layout
display = tkinter.Entry(display_frame,width=120,font= display_font,bg=background,borderwidth=10,justify= LEFT)
display.pack(padx=3,pady=4)

# Defines the first row buttons
x_button = tkinter.Button(button_frame,font=button_font,bg=buttons,text='X',command=lambda:[display_gate('x'),circuit.x(0)])
y_button = tkinter.Button(button_frame,font=button_font,bg=buttons,text='Y',command=lambda:[display_gate('y'),circuit.y(0)])
z_button = tkinter.Button(button_frame,font=button_font,bg=buttons,text='Z',command=lambda:[display_gate('z'),circuit.z(0)])
x_button.grid(row=0,column=0,ipadx=55,pady=1)
y_button.grid(row=0,column=1,ipadx=55,pady=1)
z_button.grid(row=0,column=2,ipadx=59,pady=1)

# define second row

Ry_button = tkinter.Button(button_frame, font= button_font,bg=buttons,text='RY',command=lambda:[display_gate('RX'),user_input(circuit,'x')])
Rz_button = tkinter.Button(button_frame, font= button_font,bg=buttons,text='RZ',command=lambda:[display_gate('RY'),user_input(circuit,'y')])
Rx_button = tkinter.Button(button_frame, font= button_font,bg=buttons,text='RX',command=lambda:[display_gate('RZ'),user_input(circuit,'z')])
Rx_button.grid(row=1,column=0,columnspan=1,sticky= 'WE',pady=1)
Ry_button.grid(row=1,column=1,columnspan=1,sticky= 'WE',pady=1)
Rz_button.grid(row=1,column=2,columnspan=1,sticky= 'WE',pady=1)

# Defint third row button
s_button = tkinter.Button(button_frame, font= button_font,bg=buttons,text='S',command=lambda:[display_gate('S'),circuit.s(0)])
sd_button = tkinter.Button(button_frame, font= button_font,bg=buttons,text='SD',command=lambda:[display_gate('SD'),circuit.sdg(0)])
Hedmard = tkinter.Button(button_frame, font= button_font,bg=buttons,text='H',command=lambda:[display_gate('H'),circuit.h(0)])
s_button.grid(row=2,column=0,columnspan=1,sticky= 'WE',pady=1)
sd_button.grid(row=2,column=1,sticky= 'WE',pady=1)
Hedmard.grid(row=2,column=2,rowspan=2,sticky= 'WENS',pady=1)

# define fourth row
t_button = tkinter.Button(button_frame, font= button_font,bg=buttons,text='T',command=lambda:[display_gate('T'),circuit.t(0)])
td_button = tkinter.Button(button_frame, font= button_font,bg=buttons,text='TD',command=lambda:[display_gate('TD'),circuit.tdg(0)])
t_button.grid(row=3,column=0,columnspan=1,sticky= 'WE',pady=1)
td_button.grid(row=3,column=1,columnspan=1,sticky= 'WE',pady=1)

# defint the quit and visualize button
quit = tkinter.Button(button_frame, font= button_font,bg=special_buttons,text='Quit', command= root.destroy)
visualize = tkinter.Button(button_frame, font= button_font,bg=special_buttons,text='Visualize',command= lambda:visualization_circuit(circuit,root))
quit.grid(row=4,column=0,columnspan=2,sticky= 'WE',pady=1)
visualize.grid(row=4,column=2,columnspan=1,sticky= 'WE',pady=1)

# Define the clear button
clear = tkinter.Button(button_frame, font= button_font,bg=special_buttons,text='Clear', command=clear)
clear.grid(row=5,column=0,columnspan=3,sticky= 'WE',pady=1)

#Define the about button
about = tkinter.Button(button_frame, font= button_font,bg=special_buttons,text='About', command= about)
about.grid(row=6,column=0,columnspan=3,sticky= 'WE',pady=1)

root.mainloop()
