import keyboard
from admin import DownloadData
from admin import PerformanceList
from admin import Clear

isrunning = True;
while isrunning:
    print("0-Salir")
    print("1-Actualizar información")
    print("2-Obtener lista de rendimientos")

    keyboard.read_key()
    
    if keyboard.is_pressed("0"):
        break;

    if keyboard.is_pressed("1"):
        DownloadData();

    if keyboard.is_pressed("2"):
        PerformanceList();
    
    Clear()