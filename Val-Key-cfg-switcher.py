import requests
import tkinter as tk

def swapToHead():
    res = requests.get("https://cdn.discordapp.com/attachments/774512668307882006/775719349503000586/Head.dll")
    if(res.status_code == 200):
        with open(steamPath + "crashhandler.dll", "wb") as fDLL:
            for chunk in res.iter_content(chunk_size=128):
                fDLL.write(chunk)


def swapToHeadL():
    res = requests.get("https://cdn.discordapp.com/attachments/774512668307882006/775719347384877106/Head_low_fov.dll")
    if(res.status_code == 200):
        with open(steamPath + "crashhandler.dll", "wb") as fDLL:
            for chunk in res.iter_content(chunk_size=128):
                fDLL.write(chunk)

def swapToNeck():
    res = requests.get("https://cdn.discordapp.com/attachments/774512668307882006/775719341126975488/Neck.dll")
    if(res.status_code == 200):
        with open(steamPath + "crashhandler.dll", "wb") as fDLL:
            for chunk in res.iter_content(chunk_size=128):
                fDLL.write(chunk)

def swapToNeckL():
    res = requests.get("https://cdn.discordapp.com/attachments/774512668307882006/775719349142814740/Neck_low_fov.dll")
    if(res.status_code == 200):
        with open(steamPath + "crashhandler.dll", "wb") as fDLL:
            for chunk in res.iter_content(chunk_size=128):
                fDLL.write(chunk)

def swapToBody():
    res = requests.get("https://cdn.discordapp.com/attachments/774512668307882006/775719328045072384/Body.dll")
    if(res.status_code == 200):
        with open(steamPath + "crashhandler.dll", "wb") as fDLL:
            for chunk in res.iter_content(chunk_size=128):
                fDLL.write(chunk)

def swapToBodyL():
    res = requests.get("https://cdn.discordapp.com/attachments/774512668307882006/775719349897134140/Body_low_fov.dll")
    if(res.status_code == 200):
        with open(steamPath + "crashhandler.dll", "wb") as fDLL:
            for chunk in res.iter_content(chunk_size=128):
                fDLL.write(chunk)

def reset():
    res = requests.get("https://cdn.discordapp.com/attachments/796397937981915181/797444148579926016/crashhandler.dll")
    if(res.status_code == 200):
        with open(steamPath + "crashhandler.dll", "wb") as fDLL:
            for chunk in res.iter_content(chunk_size=128):
                fDLL.write(chunk)

def minaruOG():
    res = requests.get("https://cdn.discordapp.com/attachments/762610358723674122/790077782993797150/crashhandler_-_Copy.dll")
    if(res.status_code == 200):
        with open(steamPath + "crashhandler.dll", "wb") as fDLL:
            for chunk in res.iter_content(chunk_size=128):
                fDLL.write(chunk)

def NeckLOG():
    res = requests.get("https://cdn.discordapp.com/attachments/762610358723674122/796153153006993468/NecklowfovOG.dll")
    if(res.status_code == 200):
        with open(steamPath + "crashhandler.dll", "wb") as fDLL:
            for chunk in res.iter_content(chunk_size=128):
                fDLL.write(chunk)


#read steam path

with open("steampath.txt", "r") as fSteamPath:
    global steamPath
    steamPath = fSteamPath.read()

#init tkinter & run window main
window = tk.Tk()

lblGeneric = tk.Label(text="Generic Configs:")
lblOG = tk.Label(text="OG Configs:")
lblReset = tk.Label(text="Reset:")

btnHead = tk.Button(text="Head.dll", width=25, height=3, bg="white", fg="black", command=swapToHead)
btnHeadL = tk.Button(text="Head_low_fov.dll", width=25, height=3, bg="white", fg="black", command=swapToHeadL)
btnNeck = tk.Button(text="Neck.dll", width=25, height=3, bg="white", fg="black", command=swapToNeck)
btnNeckL = tk.Button(text="Neck_low_fov.dll", width=25, height=3, bg="white", fg="black", command=swapToNeckL)
btnBody = tk.Button(text="Body.dll", width=25, height=3, bg="white", fg="black", command=swapToBody)
btnBodyL = tk.Button(text="Body_low_fov.dll", width=25, height=3, bg="white", fg="black", command=swapToBodyL)
btnReset = tk.Button(text="Reset to steam crashhandler.dll", width=25, height=3, bg="white", fg="black", command=reset)
btnMinaruOG = tk.Button(text="Minaru AIMBOT OG config", width=25, height=3, bg="white", fg="black", command=minaruOG)
btnNeckLOG = tk.Button(text="Neck Low FOV OG config", width=25, height=3, bg="white", fg="black", command=NeckLOG)

lblGeneric.pack()
btnHead.pack()
btnHeadL.pack()
btnNeck.pack()
btnNeckL.pack()
btnBody.pack()
btnBodyL.pack()
lblOG.pack()
btnMinaruOG.pack()
btnNeckLOG.pack()
lblReset.pack()
btnReset.pack()


window.mainloop()