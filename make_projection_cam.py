import pymel.core as pm
frame = pm.currentTime(query=True)
frame = str(frame)
selected = pm.ls(selection=True)

def cam_projection(selected):
    if not selected:
        pm.informBox(title="ERROR", message="Please Select Shot/Render Camera", ok="OK")
        return None
    else:
        pm.duplicate(ic=False, name="proj_cam_fr" + frame)
        return None
        
def projection_shader():
    pm.shadingNode("surfaceShader", asShader = True, n = 'projection_fr' + frame)
        
cam_projection(selected)
