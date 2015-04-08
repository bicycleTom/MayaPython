import pymel.core as pm
frame = pm.currentTime(query=True)
frame = str(frame)
selected = pm.ls(selection=True)

def cam_projection(selected):
    if not n in cam_projection:
        pm.informBox(title="ERROR", message="Please Select Shot/Render Camera", ok="OK")
    else:
        pm.duplicate(ic=False, name="proj_cam_fr" + frame)
        return None
        
cam_projection(selected)
