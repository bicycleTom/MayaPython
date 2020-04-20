import maya.cmds as cmds
import mtoa.aovs as aovs

def main():

	#avaialbe aovs in maya
	BUILTIN_AOVS = ['P', 'Z', 'N', 'opacity', 'motionvector', 'Pref', 'raycount', 'cputime', 'ID', 'RGBA', 'direct', 'indirect', 'emission', 'background', 'diffuse', 'specular',
 'transmission', 'sss', 'volume', 'albedo', 'diffuse_direct', 'diffuse_indirect', 'diffuse_albedo', 'specular_direct', 'specular_indirect', 'specular_albedo', 'coat',
 'coat_direct', 'coat_indirect', 'coat_albedo', 'sheen', 'sheen_direct', 'sheen_indirect', 'sheen_albedo', 'transmission_direct', 'transmission_indirect',
 'transmission_albedo', 'sss_direct', 'sss_indirect', 'sss_albedo', 'volume_direct', 'volume_indirect', 'volume_albedo', 'volume_opacity', 'volume_Z',
 'shadow_matte', 'AA_inv_density']

 	#avaialbe aovs in maya
	LIGHTING_AOVS = ['RGBA', 'direct', 'indirect', 'emission', 'diffuse', 'specular', 'transmission', 'sss', 'volume', 'diffuse_direct', 'diffuse_indirect', 'diffuse_albedo',
 'specular_direct', 'specular_indirect', 'specular_albedo', 'coat', 'coat_direct', 'coat_indirect', 'coat_albedo', 'transmission_direct', 'transmission_indirect',
 'transmission_albedo', 'sss_direct', 'sss_indirect', 'sss_albedo', 'volume_direct', 'volume_indirect', 'volume_albedo', 'shadow_matte', 'sheen', 'sheen_direct',
 'sheen_indirect', 'sheen_albedo']

 	#3rd party aovs
 	EXTRA_AOVS = ['crypto_asset', 'crypto_material', 'crypto_object']

 	#deliverable aovs for comp
 	PRODUCTION_AOVS = ['RGBA', 'diffuse', 'diffuse_indirect', 'specular', 'specular_direct', 'specular_indirect', 'N', 'P', 'Pref', 'Z']

 	EXISTING_AOVS = []
 	for aov in aovs.getAOVNodes(names=False):
 		EXISTING_AOVS.append(str(aov))
 	EXISTING_AOVS = [aov.replace('aiAOV_', '') for aov in EXISTING_AOVS]

 	NEW_AOVS = list(set(PRODUCTION_AOVS) - set(EXISTING_AOVS))
 	#print NEW_AOVS

 	for item in NEW_AOVS:
 		addAOV = aovs.AOVInterface().addAOV(item)