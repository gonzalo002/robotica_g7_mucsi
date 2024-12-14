import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import time
import signal

# Variable global para almacenar el proceso de RViz
rviz_process = None

def launch_rviz_in_frame(frame_id):
    global rviz_process
    try:
        # Lanza RViz en un proceso separado
        rviz_process = subprocess.Popen(['rviz'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(2)  # Da tiempo para que la ventana de RViz aparezca

        # Usa xwininfo para obtener la ventana de RViz
        try:
            win_info = subprocess.check_output(['xwininfo', '-name', 'default.rviz - RViz']).decode('utf-8')
        except subprocess.CalledProcessError as e:
            print(f"Error al buscar ventana: {e.output.decode('utf-8')}")

        # Extrae el ID de la ventana de RViz
        for line in win_info.splitlines():
            if "Window id" in line:
                rviz_window_id = line.split()[3]
                break

        # Redirige la ventana al frame de Tkinter
        subprocess.run(['xdotool', 'windowreparent', rviz_window_id, str(frame_id)])

        # Ajusta el tamaño de la ventana de RViz dentro del marco
        subprocess.run(['xdotool', 'windowsize', rviz_window_id, '800', '500'])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo incrustar RViz: {e}")

def close_rviz():
    global rviz_process
    if rviz_process:
        try:
            # Envia una señal de terminación al proceso de RViz
            rviz_process.terminate()
            rviz_process.wait()  # Espera a que el proceso termine
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cerrar RViz: {e}")
    else:
        messagebox.showwarning("Advertencia", "RViz no está abierto.")

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("Interfaz HMI con RViz")
root.geometry("800x600")

# Crear un marco para RViz
frame_rviz = tk.Frame(root, width=800, height=500, bg="black")
frame_rviz.pack(pady=10)

# Obtén el ID de la ventana del marco de Tkinter
root.update_idletasks()
frame_id = frame_rviz.winfo_id()

# Botón para lanzar RViz incrustado
launch_button = tk.Button(root, text="Abrir RViz", command=lambda: launch_rviz_in_frame(frame_id))
launch_button.pack(pady=10)

# Botón para cerrar RViz
close_button = tk.Button(root, text="Cerrar RViz", command=close_rviz)
close_button.pack(pady=10)

# Asegurarse de que la ventana se redibuje correctamente
root.mainloop()
