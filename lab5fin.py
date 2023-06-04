import rospy
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import tkinter as tk
from roboticstoolbox import DHRobot, RevoluteDH
import math
import numpy as np
from roboticstoolbox import SerialLink
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from math import cos, sin
import time


motor1 = 0
motor2 = 0
motor3 = 0
motor4 = 0
motor5 = 0
gripper = "abierto"
Tiempo=0
estadorut=0




homes= [
    [0, 0, -90, 0, 30],
    [0, 0, -90, 0, 100]

  ]

J = [
    [-4.10155634423616,-72.07020951806109,-38.378850021774575,14.062479260426969, 30],
[-4.980461244651993,-77.63660195575721,-29.882767467911957,14.062479260426969, 30],
[-4.980461244651993,-90.82017845020246,-4.10155634423616,1.757809907553371, 30],
[-4.980461244651993,-90.82017845020246,-4.10155634423616,1.757809907553371, 100],
[-4.980461244651993,-77.63660195575721,-29.882767467911957,14.062479260426969, 100],
[-4.3945249289659865,-81.15222326496784,-2.6367149146909097,-16.992161692630646, 100],
[0, 0, -90, 0, 100],
   
[-4.10155634423616,-60.80847800222381,-90.23424384206375,95.70692208487448, 100],
[-4.10155634423616,-80.85925596089848,-67.96864677052258,40.441328428427894, 100],
[-4.10155634423616,-80.56628865682913,-75.29285669301319,64.45303229150113, 100],
[-4.10155634423616,-79.98035404869042,-84.37487727010911,71.77723538380256, 100],
[-4.10155634423616,-78.80847800222381,-90.23424384206375,74.70692208487448, 100],
[-3.8085881863931568,-75.58582399708254,-95.21470167162116,75.8787913011519, 100],
[-2.6367149146909097,-76.46473273947979,-98.14438837269307,81.4451905690372, 100],
[-0.2929683179255618,-77.63660195575721,-98.43735567676242,85.54674648638654, 100],
[1.4648416429886622,-78.80847800222381,-94.9217343675518,85.25377918231717, 100],
[2.3437465434044946,-80.27332135275977,-91.11314575427183,84.37487727010911, 100],
[2.05077817211808,-81.4451905690372,-88.18346588338909,82.03113200736507, 100],

[0, 0, -90, 0, 100],
[-4.3945249289659865,-81.15222326496784,-2.6367149146909097,30.992161692630646, 100],
[-4.980461244651993,-77.63660195575721,-29.882767467911957,30.062479260426969, 100],
[-4.980461244651993,-90.82017845020246,-4.10155634423616,20.757809907553371, 100],
[-4.980461244651993,-90.82017845020246,-4.10155634423616,1.757809907553371, 30],
[-4.980461244651993,-77.63660195575721,-29.882767467911957,14.062479260426969, 30],
[0, 0, -90, 0, 30]
  
]
Rectangulo = [
    [-4.10155634423616,-72.07020951806109,-38.378850021774575,14.062479260426969, 30],
[-4.980461244651993,-77.63660195575721,-29.882767467911957,14.062479260426969, 30],
[-4.980461244651993,-90.82017845020246,-4.10155634423616,1.757809907553371, 30],
[-4.980461244651993,-90.82017845020246,-4.10155634423616,1.757809907553371, 100],
[-4.980461244651993,-77.63660195575721,-29.882767467911957,14.062479260426969, 100],
[-4.3945249289659865,-81.15222326496784,-2.6367149146909097,-16.992161692630646, 100],
[0, 0, -90, 0, 100],

[  29.58980016,  -72.36317682, -113.378736,     95.50766898,   100],
[  27.53902221,  -73.82801334, -103.41781351,   89.0623678,  100],
[ 25.19527523, -76.17176544, -92.87095641,  82.91003392,  100],
[ 31.0546401,  -80.27332135, -76.46473274,  68.2616209,   100],
[ 38.08588272, -86.42565523, -57.71475698,  55.95694974,  100],
[ 41.89446792, -91.11314575, -44.5311839,   48.63273982,  100],
[ 47.46086718, -92.87095641, -50.97648849,  54.78507711,  100],
[ 52.44132843, -87.30455714, -64.45303229,  59.47256763,  100],
[ 49.80461245, -83.78893583, -77.05066735,  74.41395478,  100],
[ 44.5311839,  -81.15222326, -91.40611306,  89.6483024,   100],
[  34.86322871,  -80.85925596, -102.8318789,   102.53891159,   100],
[  29.58980016,  -72.36317682, -113.378736,     95.50766898,   100],

[0, 0, -90, 0, 100],
[-4.3945249289659865,-81.15222326496784,-2.6367149146909097,20.992161692630646, 100],
[-4.980461244651993,-77.63660195575721,-29.882767467911957,20.062479260426969, 100],
[-4.980461244651993,-90.82017845020246,-4.10155634423616,20.757809907553371, 100],
[-4.980461244651993,-90.82017845020246,-4.10155634423616,1.757809907553371, 30],
[-4.980461244651993,-77.63660195575721,-29.882767467911957,14.062479260426969, 30],
[0, 0, -90, 0, 30]
]
Triangulo = [
 [-4.10155634423616,-72.07020951806109,-38.378850021774575,14.062479260426969, 30],
[-4.980461244651993,-77.63660195575721,-29.882767467911957,14.062479260426969, 30],
[-4.980461244651993,-90.82017845020246,-4.10155634423616,1.757809907553371, 30],
[-4.980461244651993,-90.82017845020246,-4.10155634423616,1.757809907553371, 100],
[-4.980461244651993,-77.63660195575721,-29.882767467911957,14.062479260426969, 100],
[-4.3945249289659865,-81.15222326496784,-2.6367149146909097,-16.992161692630646, 100],
[0, 0, -90, 0, 100],

[-62.69522163689582,-69.7264574251279,-94.33579975941309,76.46473273947979, 100],
[-62.402254332826466,-78.80847800222381,-87.30455714099185,76.75770004354915, 100],
[-58.0077242812186,-82.03113200736507,-74.99988938894383,69.14052281698919, 100],
[-53.02726645166119,-89.9412765379944,-57.12882236901053,60.05850223989327, 100],
[-51.26945579705588,-75.8787913011519,-91.11314575427183,71.77723538380256, 100],
[-62.69522163689582,-69.7264574251279,-94.33579975941309,76.46473273947979, 100],

[0, 0, -90, 0, 100],
[-4.3945249289659865,-81.15222326496784,-2.6367149146909097,20.992161692630646, 100],
[-4.980461244651993,-77.63660195575721,-29.882767467911957,20.062479260426969, 100],
[-4.980461244651993,-90.82017845020246,-4.10155634423616,20.757809907553371, 100],
[-4.980461244651993,-90.82017845020246,-4.10155634423616,1.757809907553371, 30],
[-4.980461244651993,-77.63660195575721,-29.882767467911957,14.062479260426969, 30],
[0, 0, -90, 0, 30]
]

Workspace = [
[0, 0, -90, 0, 30],
    [0, 0, -90, 0, 100],
    [0, 0, -90, 0, 100],
    [0, 0, -90, 0, 95],

[ 67.38271216, -90.23424384, -39.84368996,  38.96478463,  100],
[-73.24207873, -90.23424384, -39.84368996,  38.96478463,  100],
[ -77.92956926,  -73.24207873, -117.77326605,  102.53891159,   100],
[ 80.585824,  -73.24207873, -117.77326605,  102.53891159,   100],

[0, 0, -90, 0, 95]
]



def callback(data):
    rospy.loginfo(data.position)
    motor1 = data.position[0]
    motor2 = data.position[1]
    motor3 = data.position[2]
    motor4 = data.position[3]
    motor5 = data.position[4]

def listener_once():
    rospy.init_node('joint_listener', anonymous=True)
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)
  
    # Esperar un mensaje durante 5 segundos
    try:
        joint_state = rospy.wait_for_message("/dynamixel_workbench/joint_states", JointState, timeout=2)
        callback(joint_state)
    except rospy.ROSException:
        show_warning_window("No se recibió ningún mensaje después de 5 segundos.")
def show_warning_window(message):
    root = tk.Tk()
    root.withdraw()
    tk.messagebox.showwarning("Advertencia", message)

def show_warning_window(message):
    root = tk.Tk()
    root.withdraw()
    tk.messagebox.showwarning("Advertencia", message)

def ejecutar_codigo():
    # Llamar a listener_once() una vez
    listener_once()



def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)

    state = JointTrajectory()

    while not rospy.is_shutdown():
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()
        point.positions = np.radians([-25, -15, -90-20, 20, 0])
        point.time_from_start = rospy.Duration(0.1)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(2)
tiempo_inicio=0
def set_positions(positions_list):
    global pub
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
    estadorut=0
    for positions in positions_list:
        estadorut=1
        point = JointTrajectoryPoint()
        point.positions = np.radians(positions)
        point.time_from_start = rospy.Duration(0.1)
        state.points.append(point)
        tiempo_inicio = time.time()
    pub.publish(state)


def start_publisher():
    rospy.loginfo("Starting publisher")
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    joint_publisher()


#parada de emergencia  de stop
stop_flag = False
def emergency_stop():
    global stop_flag
    stop_flag = True




root = tk.Tk()
root.title("Controlador robot")


image_fondo = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/pngegg.png")
fondo = tk.Label(root, image=image_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)



def change_image(event, button, new_image):
    button.config(image=new_image)

frame_buttons = tk.Frame(root)
frame_buttons.pack(side=tk.TOP, padx=10, pady=10)

image_1 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/home.png")
image_2 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/j.png")
image_3 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/c.png")
image_4 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/casa.png")
image_5 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/ws.png")
image_WS = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/ws.png")



image_11 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/home1.png")
image_22 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/j.png")
image_33 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/c.png")
image_44 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/casa.png")
image_55 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/ws.png")


def actualizar_ultimo_boton(texto):
    label_ultimo_boton.config(text="Último botón oprimido: {}".format(texto))

button_1 = tk.Button(frame_buttons, image=image_1, text="Home", command=lambda: [set_positions(homes), actualizar_ultimo_boton("Home")], bd=0, highlightthickness=0, compound="top")
button_2 = tk.Button(frame_buttons, image=image_2, text="J", command=lambda: [set_positions(J), actualizar_ultimo_boton("J")], bd=0, highlightthickness=0, compound="top")
button_3 = tk.Button(frame_buttons, image=image_3, text="Rectángulo", command=lambda: [set_positions(Rectangulo), actualizar_ultimo_boton("Rectángulo")], bd=0, highlightthickness=0, compound="top")
button_4 = tk.Button(frame_buttons, image=image_4, text="Triángulo", command=lambda: [set_positions(Triangulo), actualizar_ultimo_boton("Triángulo")], bd=0, highlightthickness=0, compound="top")
button_WS = tk.Button(frame_buttons, image=image_4, text="Workspace", command=lambda: [set_positions(Workspace), actualizar_ultimo_boton("Workspace")], bd=0, highlightthickness=0, compound="top")

start_button = tk.Button(frame_buttons, text="Start", command=lambda: [start_publisher(), actualizar_ultimo_boton("Start")])


button_1.bind("<Enter>", lambda event: change_image(event, button_1, new_image=image_11))
button_1.bind("<Leave>", lambda event: change_image(event, button_1, new_image=image_1))

button_2.bind("<Enter>", lambda event: change_image(event, button_2, new_image=image_22))
button_2.bind("<Leave>", lambda event: change_image(event, button_2, new_image=image_2))

button_3.bind("<Enter>", lambda event: change_image(event, button_3, new_image=image_33))
button_3.bind("<Leave>", lambda event: change_image(event, button_3, new_image=image_3))

button_4.bind("<Enter>", lambda event: change_image(event, button_4, new_image=image_44))
button_4.bind("<Leave>", lambda event: change_image(event, button_4, new_image=image_4))

button_WS = tk.Button(frame_buttons, image=image_WS, text="Workspace", bd=0, highlightthickness=0, compound="top")


button_1.config(width=300, height=400)
button_2.config(width=300, height=400)
button_3.config(width=300, height=400)
button_4.config(width=300, height=400)

button_WS.config(width=300, height=400)
start_button.config(width=root.winfo_width(), height=5, bg="#edf8b0", activebackground="#f0ff18", foreground="#000000")


start_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
button_1.pack(side=tk.LEFT, padx=10, pady=10)
button_2.pack(side=tk.LEFT, padx=10, pady=10)
button_3.pack(side=tk.LEFT, padx=10, pady=10)
button_4.pack(side=tk.LEFT, padx=10, pady=10)
button_WS.pack(side=tk.LEFT, padx=10, pady=10)

start_button.pack()
start_button.lift() 


frame_container2 = tk.Frame(root)
frame_container2.pack(side=tk.LEFT, padx=10, pady=10, anchor=tk.W)

frame_extra2 = tk.LabelFrame(frame_container2, text="Último Rutina", font=("Arial", 14, "bold"))
frame_extra2.pack(side=tk.LEFT, padx=10, pady=10)

label_ultimo_boton = tk.Label(frame_extra2, text="Último Rutina:", anchor=tk.W, justify=tk.LEFT)
label_ultimo_boton.grid(row=0, column=0, padx=10, pady=5)

label_ultimo_boton2 = tk.Label(frame_extra2, text="¿terminó la rutina?", anchor=tk.W, justify=tk.LEFT)
label_ultimo_boton2.grid(row=1, column=0, padx=10, pady=5)


if estadorut == 1:
    termino = "si"
else:
    termino = "no"


label_ultimo_boton2.config(text=" ¿terminó la rutina? {}".format(termino))


frame_container = tk.Frame(root)
frame_container.pack(side=tk.LEFT, padx=10, pady=10)



frame_extra = tk.LabelFrame(frame_container, text="Integrantes del grupo")
frame_extra.pack(side=tk.LEFT, padx=10, pady=10)

image = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/unal.png")
label_imagen = tk.Label(frame_extra, image=image)
label_imagen.grid(row=0, column=0, padx=10, pady=10, rowspan=3)

label_texto1 = tk.Label(frame_extra, text="Valentina Cruz De Paula")
label_texto1.grid(row=0, column=1, padx=10, pady=10)

label_texto2 = tk.Label(frame_extra, text="Oscar Sergio Urrego Riaño")
label_texto2.grid(row=1, column=1, padx=10, pady=10)

label_texto3 = tk.Label(frame_extra, text="Jhon Nelson Cáceres Leal")
label_texto3.grid(row=2, column=1, padx=10, pady=10)



frame_data = tk.LabelFrame(frame_container, text="Datos de los motores")
frame_data.pack(side=tk.LEFT, padx=100, pady=10)

label_motor1 = tk.Label(frame_data, text="Motor 1: ")
label_motor1.pack(padx=10, pady=10)

label_motor2 = tk.Label(frame_data, text="Motor 2: ")
label_motor2.pack(padx=10, pady=10)

label_motor3 = tk.Label(frame_data, text="Motor 3: ")
label_motor3.pack(padx=10, pady=10)

label_motor4 = tk.Label(frame_data, text="Motor 4: ")
label_motor4.pack(padx=10, pady=10)

label_motor5 = tk.Label(frame_data, text="gripper: ")
label_motor5.pack(padx=10, pady=10)

#tiempo


tiempo_actual = time.time() 
Tiempo= tiempo_actual - tiempo_inicio


label_Tiempo= tk.Label(frame_data, text="Tiempo: ")
label_Tiempo.pack(padx=10, pady=10)



#cambiar nombres



#rutina finalizada



#con el siguiente fracmento se llama posicion
ejecutar_codigo()

if motor5 > 105:
    gripper = "Cerrado"
else:
    gripper = "Abierto"

 
def update_labels():
    label_motor1.config(text="Motor 1: {}".format(motor1))
    label_motor2.config(text="Motor 2: {}".format(motor2))
    label_motor3.config(text="Motor 3: {}".format(motor3))
    label_motor4.config(text="Motor 4: {}".format(motor4))
    label_motor5.config(text="gripper: {}".format(gripper))
    label_Tiempo.config(text="Tiempo: {}".format(Tiempo))


frame_buttonseES = tk.Frame(root)
frame_buttonseES.pack(side=tk.TOP, padx=10, pady=10)

image_6 = tk.PhotoImage(file="/home/jhon/Escritorio/fotos/emerg.png")

button_5ES = tk.Button(frame_buttonseES, image=image_6, text="EMERGENCY STOP", command=lambda: [set_positions(), actualizar_ultimo_boton("EMERGENCY STOP")], bd=0, highlightthickness=0, compound="top")
button_5ES.config(width=image_6.width(), height=image_6.height())
button_5ES.pack(side=tk.RIGHT, padx=10, pady=10)



update_labels()

root.mainloop()

