import pymel.core as pm

frame = pm.currentTime(query=True)
frame_name = str(frame)
frame_num = str(int(pm.currentTime(query=True)))
selected = pm.ls(selection=True)

def cam_projection(selected):
    if not selected:
        pm.informBox(title="ERROR", message="Please Select Shot/Render Camera", ok="OK")
        return None
    else:
        pm.duplicate(ic=False, name="proj_cam_fr" + frame)
        return None
        
        
cam_projection(selected)

proj_cam = cam_projection
proj_cam = pm.listRelatives(c=True, ad=True, s=True)

def shader_projection(selected):
    if not selected:
        return None
    else:
        projection_shader = pm.shadingNode("surfaceShader", asShader = True, n = 'projectionShader_fr' + frame_name)
        filename = pm.shadingNode("file", asTexture = True)
        twoDTexture = pm.shadingNode("place2dTexture", asUtility = True)
        projection_utility = pm.shadingNode("projection", asUtility = True, n = "projection_utility_fr" + frame_name)
        
        proj_utility_name = str(projection_utility)
        
        pm.setAttr(filename.filterType, 0)
        pm.setAttr(projection_utility.projType, 8)
        pm.setAttr(projection_utility.fitType, 0)
        
        pm.connectAttr(proj_cam[0].message, projection_utility.linkedCamera)
        pm.connectAttr(projection_utility.outColor, projection_shader.outColor, f = True)
        pm.connectAttr(filename.outColor, projection_utility.image, f = True)
                
        pm.connectAttr(twoDTexture.coverage, filename.coverage, f = True)
        pm.connectAttr(twoDTexture.translateFrame, filename.translateFrame, f = True)
        pm.connectAttr(twoDTexture.rotateFrame, filename.rotateFrame, f = True)
        pm.connectAttr(twoDTexture.mirrorU, filename.mirrorU, f = True)
        pm.connectAttr(twoDTexture.mirrorV, filename.mirrorV, f = True)
        pm.connectAttr(twoDTexture.stagger, filename.stagger, f = True)
        pm.connectAttr(twoDTexture.wrapU, filename.wrapU, f = True)
        pm.connectAttr(twoDTexture.wrapV, filename.wrapV, f = True)
        pm.connectAttr(twoDTexture.repeatUV, filename.repeatUV, f = True)
        pm.connectAttr(twoDTexture.offset, filename.offset, f = True)
        pm.connectAttr(twoDTexture.rotateUV, filename.rotateUV, f = True)
        pm.connectAttr(twoDTexture.noiseUV, filename.noiseUV, f = True)
        pm.connectAttr(twoDTexture.vertexUvOne, filename.vertexUvOne, f = True)
        pm.connectAttr(twoDTexture.vertexUvTwo, filename.vertexUvTwo, f = True)
        pm.connectAttr(twoDTexture.vertexUvThree, filename.vertexUvThree, f = True)
        pm.connectAttr(twoDTexture.vertexCameraOne, filename.vertexCameraOne, f = True)
        pm.connectAttr(twoDTexture.outUV, filename.uv, f = True)
        pm.connectAttr(twoDTexture.outUvFilterSize, filename.uvFilterSize, f= True)

        return None

shader_projection(selected)
