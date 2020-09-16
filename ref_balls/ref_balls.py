import maya.cmds as cmds
import maya.mel as mel
import mtoa.utils as mutils
import mtoa.core as core

def main():

    createMAC()


def createMAC(*args):
    #cmds.namespace(add='mac')
    #cmds.namespace(set=':mac')
    macbeth_data = [
        {
            "row": 1,
            "column": 1,
            "name": "Patch 01 Dark Skin",
            "base_color": (0.13574, 0.08508, 0.05844),
        },
        {
            "row": 1,
            "column": 2,
            "name": "Patch 02 Light Skin",
            "base_color": (0.44727, 0.29639, 0.22607),
        },
        {
            "row": 1,
            "column": 3,
            "name": "Patch 03 Blue Sky",
            "base_color": (0.14404, 0.18530, 0.30762),
        },
        {
            "row": 1,
            "column": 4,
            "name": "Patch 04 Foliage",
            "base_color": (0.11804, 0.14587, 0.06372),
        },
        {
            "row": 1,
            "column": 5,
            "name": "Patch 05 Blue Flower",
            "base_color": (0.23254, 0.21704, 0.39697),
        },
        {
            "row": 1,
            "column": 6,
            "name": "Patch 06 Bluish Green",
            "base_color": (0.26196, 0.47803, 0.41626),
        },
        {
            "row": 2,
            "column": 1,
            "name": "Patch 07 Orange",
            "base_color": (0.52686, 0.23767, 0.06519),
        },
        {
            "row": 2,
            "column": 2,
            "name": "Patch 08 Purplish Blue",
            "base_color": (0.08972, 0.10303, 0.34717),
        },
        {
            "row": 2,
            "column": 3,
            "name": "Patch 09 Moderate Red",
            "base_color": (0.37646, 0.11469, 0.11987),
        },
        {
            "row": 2,
            "column": 4,
            "name": "Patch 10 Purple",
            "base_color": (0.08813, 0.04837, 0.12622),
        },
        {
            "row": 2,
            "column": 5,
            "name": "Patch 11 Yellow Green",
            "base_color": (0.37329, 0.47803, 0.10223),
        },
        {
            "row": 2,
            "column": 6,
            "name": "Patch 12 Orange Yellow",
            "base_color": (0.59424, 0.38135, 0.07593),
        },
        {
            "row": 3,
            "column": 1,
            "name": "Patch 13 Blue",
            "base_color": (0.04327, 0.04965, 0.25073),
        },
        {
            "row": 3,
            "column": 2,
            "name": "Patch 14 Green",
            "base_color": (0.12939, 0.27075, 0.08832),
        },
        {
            "row": 3,
            "column": 3,
            "name": "Patch 15 Red",
            "base_color": (0.28809, 0.06543, 0.04855),
        },
        {
            "row": 3,
            "column": 4,
            "name": "Patch 16 Yellow",
            "base_color": (0.70947, 0.58350, 0.08929),
        },
        {
            "row": 3,
            "column": 5,
            "name": "Patch 17 Magenta",
            "base_color": (0.36133, 0.11279, 0.26929),
        },
        {
            "row": 3,
            "column": 6,
            "name": "Patch 18 Cyan",
            "base_color": (0.07062, 0.21643, 0.35132),
        },
        {
            "row": 4,
            "column": 1,
            "name": "Patch 19 White 9.5 005D",
            "base_color": (0.87891, 0.88379, 0.84131),
        },
        {
            "row": 4,
            "column": 2,
            "name": "Patch 20 Neutral 8 023D",
            "base_color": (0.58691, 0.59131, 0.58545),
        },
        {
            "row": 4,
            "column": 3,
            "name": "Patch 21 Neutral 6.5 044D",
            "base_color": (0.36133, 0.36646, 0.36523),
        },
        {
            "row": 4,
            "column": 4,
            "name": "Patch 22 Neutral 5 070D",
            "base_color": (0.19031, 0.19080, 0.18994),
        },
        {
            "row": 4,
            "column": 5,
            "name": "Patch 23 Neutral 3.5 1.05D",
            "base_color": (0.08710, 0.08856, 0.08960),
        },
        {
            "row": 4,
            "column": 6,
            "name": "Patch 24 Black 2 1.5D",
            "base_color": (0.03146, 0.03149, 0.03220),
        },
    ]

    MACgroup = cmds.group(name = 'ref_balls_grp', empty=True)
    #patchGroupFlat = cmds.group(name = 'macbethPatchesFlat_grp', empty=True)
    #MACflat = cmds.group(name = 'macbethFlat_grp', empty=True)
    MACctrlGrp = cmds.group(name = 'balls_macbeth_grp', empty=True)
    cmds.parent(MACctrlGrp, MACgroup)
    #cmds.parent(MACflat, MACctrlGrp)
    #cmds.parent(patchGroupFlat, MACflat)
    MACshaded = cmds.group(name = 'macbeth_grp', empty=True)
    patchGroupShaded = cmds.group(name = 'patches_grp', empty=True)
    cmds.parent(MACshaded, MACctrlGrp)
    cmds.parent(patchGroupShaded, MACshaded)
    Sphgroup = cmds.group(name = 'balls_grp', empty=True)
    cmds.parent(Sphgroup, MACctrlGrp)
    mtp = 4.5

    #checker body shaded
    chckBodyShaded = cmds.polyCube(name="checkerBodyShaded", width=28, height=19, depth=0.5,createUVs=4, ch=False)
    #cmds.setAttr(chckBodyShaded[0] + ".translateZ",15.15)
    #cmds.setAttr(chckBodyShaded[0] + ".translateY",-31.944)
    cmds.setAttr(chckBodyShaded[0] + ".translateX",19.9379)
    cmds.setAttr(chckBodyShaded[0] + ".translateZ",-0.5)
    cmds.makeIdentity(chckBodyShaded[0], translate=True, apply=True)
    cmds.move(0,0,0, chckBodyShaded[0] + ".scalePivot", chckBodyShaded[0] + ".rotatePivot", absolute=True)
    cmds.parent(chckBodyShaded[0], MACshaded)
    #checker body shader shaded
    chckShdShaded = cmds.shadingNode('aiStandardSurface', asShader=True, name="aiMacbethBodyShaded")
    cmds.setAttr(chckShdShaded + ".base", 1)
    cmds.setAttr(chckShdShaded + ".baseColor", 0,0,0, type='double3')
    cmds.setAttr(chckShdShaded + ".specular", 0.0)
    cmds.setAttr(chckShdShaded + ".specularRoughness", 0.5)
    cmds.select(chckBodyShaded[0])
    cmds.hyperShade(assign=chckShdShaded)

    #spheres
    #chrome
    chrome = cmds.polySphere(name="chromeSphere", radius=9,createUVs=2,ch=False)
    cmds.setAttr(chrome[0] + ".translateX",-24.9936)
    cmds.setAttr(chrome[0] + ".translateY",0.0043)
    cmds.setAttr(chrome[0] + '.aiSubdivType', 1)
    cmds.setAttr(chrome[0] + '.aiSubdivIterations', 3)
    cmds.makeIdentity(chrome[0], translate=True, apply=True)
    cmds.move(0,0,0, chrome[0] + ".scalePivot", chrome[0] + ".rotatePivot", absolute=True)
    cmds.parent(chrome[0], Sphgroup)
    chromeShd = cmds.shadingNode('aiStandardSurface', asShader=True, name="aiChrome")
    cmds.setAttr(chromeShd + ".base", 1)
    cmds.setAttr(chromeShd + ".baseColor", 0.75,0.75,0.75, type='double3')
    cmds.setAttr(chromeShd + ".metalness", 1)
    cmds.setAttr(chromeShd + ".specular", 1)
    cmds.setAttr(chromeShd + ".specularRoughness", 0)
    cmds.select(chrome[0])
    cmds.hyperShade(assign=chromeShd)
    #gray
    gray = cmds.polySphere(name="graySphere", radius=9,createUVs=2,ch=False)
    cmds.setAttr(gray[0] + ".translateX",-5.0762)
    cmds.setAttr(gray[0] + ".translateY",0.0043)
    cmds.setAttr(gray[0] + '.aiSubdivType', 1)
    cmds.setAttr(gray[0] + '.aiSubdivIterations', 3)
    cmds.makeIdentity(gray[0], translate=True, apply=True)
    cmds.move(0,0,0, gray[0] + ".scalePivot", gray[0] + ".rotatePivot", absolute=True)
    cmds.parent(gray[0], Sphgroup)
    grayShd = cmds.shadingNode('aiStandardSurface', asShader=True, name="aiGray")
    cmds.setAttr(grayShd + ".base", 1)
    cmds.setAttr(grayShd + ".baseColor", 0.18,0.18,0.18, type='double3')
    cmds.setAttr(grayShd + ".specular", 0)
    cmds.setAttr(grayShd + ".specularRoughness", 0.7)
    cmds.select(gray[0])
    cmds.hyperShade(assign=grayShd)

    dispOver = [gray, chrome, chckBodyShaded]
    for each in dispOver:
        doSel = cmds.ls(each)
        cmds.setAttr(each[0] + ".overrideEnabled", 1)
        cmds.setAttr(each[0] + ".overrideDisplayType", 2)

    #PATCHES SHADED
    for each in macbeth_data:
            #geo
            patchShaded = cmds.polyCube(name=(each["name"] + "Shaded"), width=4.2, height=4.2, depth=0.3, createUVs=4, axis=[0,1,0],ch=False)
            patchShadedDOsel = cmds.ls(patchShaded)
            cmds.setAttr(patchShaded[0] + ".translateX", (each["column"])*mtp)
            cmds.setAttr(patchShaded[0] + ".translateY", (each["row"])*-mtp)
            xpos = cmds.getAttr(patchShaded[0] + ".translateX")
            ypos = cmds.getAttr(patchShaded[0] + ".translateY")
            cmds.setAttr(patchShaded[0] + ".translateX",xpos-15.75+19.9379)
            cmds.setAttr(patchShaded[0] + ".translateY",ypos+11.25)
            cmds.makeIdentity(patchShaded[0], translate=True, apply=True)
            cmds.move(0,0,0, patchShaded[0] + ".scalePivot", patchShaded[0] + ".rotatePivot", absolute=True)
            cmds.setAttr(patchShaded[0] + ".receiveShadows",0)
            cmds.setAttr(patchShaded[0] + ".motionBlur",0)
            cmds.setAttr(patchShaded[0] + ".castsShadows",0)
            cmds.setAttr(patchShaded[0] + ".visibleInRefractions",0)
            cmds.setAttr(patchShaded[0] + ".visibleInReflections",0)
            cmds.setAttr(patchShaded[0] + ".aiVisibleInDiffuseReflection",0)
            cmds.setAttr(patchShaded[0] + ".aiVisibleInSpecularReflection",0)
            cmds.setAttr(patchShaded[0] + ".aiVisibleInDiffuseTransmission",0)
            cmds.setAttr(patchShaded[0] + ".aiVisibleInSpecularTransmission",0)
            cmds.setAttr(patchShaded[0] + ".aiVisibleInVolume",0)
            cmds.setAttr(patchShaded[0] + ".aiSelfShadows",0)
            cmds.setAttr(patchShadedDOsel[0] + ".overrideEnabled", 1)
            cmds.setAttr(patchShadedDOsel[0] + ".overrideDisplayType", 2)
            cmds.setAttr(patchShaded[0] + ".translateX", keyable=False, lock=True)
            cmds.setAttr(patchShaded[0] + ".translateY", keyable=False, lock=True)
            cmds.setAttr(patchShaded[0] + ".translateZ", keyable=False, lock=True)
            cmds.setAttr(patchShaded[0] + ".rotateX", keyable=False, lock=True)
            cmds.setAttr(patchShaded[0] + ".rotateY", keyable=False, lock=True)
            cmds.setAttr(patchShaded[0] + ".rotateZ", keyable=False, lock=True)
            cmds.parent(patchShaded[0], patchGroupShaded)

            #shader
            patchBscShdShaded = cmds.shadingNode('aiStandardSurface', asShader=True, name="ai" + (each["name"] + "Shaded"))
            cmds.setAttr(patchBscShdShaded + ".base", 1)
            cmds.setAttr(patchBscShdShaded + ".baseColor", each["base_color"][0], each["base_color"][1], each["base_color"][2], type='double3')
            cmds.setAttr(patchBscShdShaded + ".specular", 0)
            cmds.setAttr(patchBscShdShaded + ".specularRoughness", 0.7)
            cmds.select(patchShaded[0])
            cmds.hyperShade(assign=patchBscShdShaded)

    #macbeth control curve and constraints
    #macCtrl = cmds.curve(name="Macbeth_ctrl", degree=1, point=[(-17, -2, 0), (-17, 57, 0), (17, 57, 0), (17, -2, 0), (-17, -2, 0)] )
    #macLoc = cmds.spaceLocator(name = "mac_loc", position = [0,0,0])

    #cmds.parent(macCtrl, MACgroup)
    #cmds.parent(macLoc, MACgroup)
    #cmds.setAttr(macCtrl + ".translateY", 2)
    #cmds.makeIdentity(macCtrl, translate=True, apply=True)
    #cmds.move(0,0,0, macCtrl + ".scalePivot", macCtrl + ".rotatePivot", absolute=True)

    #cmds.parentConstraint(macCtrl, MACctrlGrp, maintainOffset=True, weight=1)
    #cmds.scaleConstraint(macCtrl, MACctrlGrp, maintainOffset=True, weight=1)
    #cmds.setAttr(macCtrl + ".translateX", -170)

    #CREATE A MAC SCALING
    if cmds.namespace(exists=":dk_Ldv") == True:
        scale = cmds.getAttr("dk_Ldv:ldvGlobal_ctrl.scaleX")
        cmds.parentConstraint(macLoc[0], macCtrl, maintainOffset=True, weight=1)
        cmds.setAttr(macLoc[0] + ".scaleX", scale)
        cmds.setAttr(macCtrl + ".scaleX", scale)
        cmds.setAttr(macCtrl + ".scaleY", scale)
        cmds.setAttr(macCtrl + ".scaleZ", scale)

    #lock attr
    MACgrplist = [MACctrlGrp, MACshaded, patchGroupShaded, Sphgroup, chckBodyShaded[0], chrome[0], gray[0] ]
    for each in MACgrplist:
        cmds.setAttr(each + ".translateX", keyable=False, lock=True)
        cmds.setAttr(each + ".translateY", keyable=False, lock=True)
        cmds.setAttr(each + ".translateZ", keyable=False, lock=True)
        cmds.setAttr(each + ".rotateX", keyable=False, lock=True)
        cmds.setAttr(each + ".rotateY", keyable=False, lock=True)
        cmds.setAttr(each + ".rotateZ", keyable=False, lock=True)

    #Arnold attributes
    attrList = [chckBodyShaded[0], chrome[0], gray[0] ]
    for each in attrList:
        cmds.setAttr(each + ".receiveShadows",0)
        cmds.setAttr(each + ".motionBlur",0)
        cmds.setAttr(each + ".castsShadows",0)
        cmds.setAttr(each + ".visibleInRefractions",0)
        cmds.setAttr(each + ".visibleInReflections",0)
        cmds.setAttr(each + ".aiVisibleInDiffuseReflection",0)
        cmds.setAttr(each + ".aiVisibleInSpecularReflection",0)
        cmds.setAttr(each + ".aiVisibleInDiffuseTransmission",0)
        cmds.setAttr(each + ".aiVisibleInSpecularTransmission",0)
        cmds.setAttr(each + ".aiVisibleInVolume",0)
        cmds.setAttr(each + ".aiSelfShadows",0)

    cmds.namespace(set=':')
    cmds.select(clear=True)