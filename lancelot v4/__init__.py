# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Lancelot v4",
    "author" : "SirCruX Studios",
    "description" : "",
    "blender" : (4, 0, 0),
    "version" : (4, 0, 2),
    "location" : "",
    "warning" : "",
    "category" : "Rigging"
}

import os
import bpy

from . lancelot_op import LCT3_OT_FK_Layer, LCT3_OT_IK_Layer, LCT3_OT_MOCAP_Layer, LCT3_OT_MOCAP_RAW_Layer, LCT3_OT_FINGERS_Layer, LCT3_OT_Select_L_Fingers, LCT3_OT_EYES_Layer, LCT3_OT_Select_R_Fingers, LCT3_OT_Clear_bone_transform, LCT3_OT_Clear_all_bone_transform, LCT3_OT_STR_Reset_Length, LCT3_OT_Stretch_Layer

from . lancelot_panel import LCT3_PT_Panel_Main, LCT3_PT_Panel_Root_Spine, LCT3_PT_Panel_Limbs, LCT3_PT_Panel_Layers, LCT3_PT_Panel_Select, LCT3_PT_Panel_Char_Options, LCT3_PT_Panel_Mocap_Col

classes = (LCT3_PT_Panel_Main, LCT3_PT_Panel_Layers, LCT3_PT_Panel_Select, LCT3_PT_Panel_Limbs,  LCT3_PT_Panel_Root_Spine, LCT3_PT_Panel_Char_Options, LCT3_PT_Panel_Mocap_Col, LCT3_OT_FK_Layer, LCT3_OT_IK_Layer, LCT3_OT_MOCAP_Layer, LCT3_OT_MOCAP_RAW_Layer, LCT3_OT_FINGERS_Layer, LCT3_OT_EYES_Layer, LCT3_OT_Clear_bone_transform, LCT3_OT_Select_L_Fingers, LCT3_OT_Select_R_Fingers,  LCT3_OT_Clear_all_bone_transform, LCT3_OT_STR_Reset_Length, LCT3_OT_Stretch_Layer)



def register():
    print("ABRIR REGISTER")
    


    print("FORA DO FOR")

    for c in classes:
        bpy.utils.register_class(c)
    #bpy.utils.register_class(LCT3_PT_Panel)

    

def unregister():
    # for pcoll in preview_collections.values():
    #     bpy.utils.previews.remove(pcoll)
    # preview_collections.clear()
    
    for c in classes:
        bpy.utils.unregister_class(c)
    #bpy.utils.unregister_class(LCT3_PT_Panel)
        
