import bpy

from bpy.types import Operator




class LCT3_OT_FK_Layer(Operator):
    bl_idname = "lct3.fklayer"
    bl_label = "FK"
    bl_description= "Fk Controls for Traditional Animation"
 
    
    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            bpy.ops.object.mode_set(mode='POSE')
            # bpy.ops.armature.armature_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            now_layers=obj.data.layers
            now_layers = list(now_layers)
            print(now_layers)
            
            
            if obj["LT FK"] == 0:
                T_layers = now_layers
                print( "now to T",T_layers)
                T_layers[1] = True
                print ("invert",T_layers)
                T_layers = tuple(T_layers)
                print( "to tuple",T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
                print("transform")
                obj["LT FK"] = 1
            else:
                T_layers = now_layers
                print( "now to T")
                T_layers[1] = False
                print ("invert")
                T_layers = tuple(T_layers)
                print( "to tuple")
                bpy.ops.armature.armature_layers(layers=T_layers)
                print("transform")
                obj["LT FK"] = 0

            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}





class LCT3_OT_IK_Layer(Operator):
    bl_idname = "lct3.iklayer"
    bl_label = "IK"
    bl_description= "Ik controls for Traditional Animation"

     
    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            bpy.ops.object.mode_set(mode='POSE')
            # bpy.ops.armature.armature_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            now_layers=obj.data.layers
            now_layers = list(now_layers)
            print(now_layers)
            
            
            if obj["LT IK"] == 0:
                T_layers = now_layers
                print( "now to T",T_layers)
                T_layers[2] = True
                print ("invert",T_layers)
                T_layers = tuple(T_layers)
                print( "to tuple",T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
                print("transform")
                obj["LT IK"] = 1
            else:
                T_layers = now_layers
                print( "now to T")
                T_layers[2] = False
                print ("invert")
                T_layers = tuple(T_layers)
                print( "to tuple")
                bpy.ops.armature.armature_layers(layers=T_layers)
                print("transform")
                obj["LT IK"] = 0

            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}

  

class LCT3_OT_MOCAP_Layer(Operator):
    bl_idname = "lct3.mocaplayer"
    bl_label = "MOCAP"
    bl_description= "Control Mocap Handles, used for refining Mocap (Keyframes should be added, when manipulating the handles"

    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            bpy.ops.object.mode_set(mode='POSE')
            # bpy.ops.armature.armature_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            now_layers=obj.data.layers
            now_layers = list(now_layers)
            print(now_layers)
            
            
            if obj["LT MOCAP"] == 0:
                T_layers = now_layers
                print( "now to T",T_layers)
                T_layers[3] = True
                print ("invert",T_layers)
                T_layers = tuple(T_layers)
                print( "to tuple",T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
                print("transform")
                obj["LT MOCAP"] = 1
            else:
                T_layers = now_layers
                print( "now to T")
                T_layers[3] = False
                print ("invert")
                T_layers = tuple(T_layers)
                print( "to tuple")
                bpy.ops.armature.armature_layers(layers=T_layers)
                print("transform")
                obj["LT MOCAP"] = 0

            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}



class LCT3_OT_MOCAP_RAW_Layer(Operator):
    bl_idname = "lct3.mocaprawlayer"
    bl_label = "MOCAP RAW"
    bl_description= "Raw Mocap Animation, Used for reference"

    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            bpy.ops.object.mode_set(mode='POSE')
            # bpy.ops.armature.armature_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            now_layers=obj.data.layers
            now_layers = list(now_layers)
            print(now_layers)
            
            
            if obj["LT MOCAP RAW"] == 0:
                T_layers = now_layers
                print( "now to T",T_layers)
                T_layers[16] = True
                print ("invert",T_layers)
                T_layers = tuple(T_layers)
                print( "to tuple",T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
                print("transform")
                obj["LT MOCAP RAW"] = 1
            else:
                T_layers = now_layers
                print( "now to T")
                T_layers[16] = False
                print ("invert")
                T_layers = tuple(T_layers)
                print( "to tuple")
                bpy.ops.armature.armature_layers(layers=T_layers)
                print("transform")
                obj["LT MOCAP RAW"] = 0

            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}

class LCT3_OT_FINGERS_Layer(Operator):
    bl_idname = "lct3.fingerslayer"
    bl_label = "FINGERS LAYER"
    bl_description= "FK Finger Controls"

    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            bpy.ops.object.mode_set(mode='POSE')
            # bpy.ops.armature.armature_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            now_layers=obj.data.layers
            now_layers = list(now_layers)
            print(now_layers)
            
            
            if obj["LT FINGERS"] == 0:
                T_layers = now_layers
                print( "now to T",T_layers)
                T_layers[5] = True
                print ("invert",T_layers)
                T_layers = tuple(T_layers)
                print( "to tuple",T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
                print("transform")
                obj["LT FINGERS"] = 1
            else:
                T_layers = now_layers
                print( "now to T")
                T_layers[5] = False
                print ("invert")
                T_layers = tuple(T_layers)
                print( "to tuple")
                bpy.ops.armature.armature_layers(layers=T_layers)
                print("transform")
                obj["LT FINGERS"] = 0

            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}

class LCT3_OT_EYES_Layer(Operator):
    bl_idname = "lct3.eyeslayer"
    bl_label = "EYES LAYER"
    bl_description= "Eye Controls"

    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            bpy.ops.object.mode_set(mode='POSE')
            # bpy.ops.armature.armature_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            now_layers=obj.data.layers
            now_layers = list(now_layers)
            print(now_layers)
            
            
            if obj["LT EYES"] == 0:
                T_layers = now_layers
                print( "now to T",T_layers)
                T_layers[6] = True
                print ("invert",T_layers)
                T_layers = tuple(T_layers)
                print( "to tuple",T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
                print("transform")
                obj["LT EYES"] = 1
            else:
                T_layers = now_layers
                print( "now to T")
                T_layers[6] = False
                print ("invert")
                T_layers = tuple(T_layers)
                print( "to tuple")
                bpy.ops.armature.armature_layers(layers=T_layers)
                print("transform")
                obj["LT EYES"] = 0

            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}


class LCT3_OT_Select_L_Fingers(Operator):
    bl_idname = "lct3.fk_l_fingers"
    bl_label = "Select Left Hand Fingers"
    bl_description= "Select all controls for fingers in Left Hand"

    def execute (self,context):
        if bpy.context.object.type == 'ARMATURE':
            obj = context.object
            #get to pose mode
            bpy.ops.object.mode_set(mode='POSE')
            #deselect previous bone group
            bpy.ops.pose.group_deselect()
            #select bone group in menu
            bone_groups = obj.pose.bone_groups
            bone_groups.active = bone_groups["FK FINGERS L"]
            
            #select bones in active bone group
            bpy.ops.pose.group_select()
            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}

class LCT3_OT_Select_R_Fingers(Operator):
    bl_idname = "lct3.fk_r_fingers"
    bl_label = "Select Right Hand Fingers"
    bl_description= "Select all controls for fingers in Right Hand"

    def execute (self,context):
        if bpy.context.object.type == 'ARMATURE':
            obj = context.object
            #get to pose mode
            bpy.ops.object.mode_set(mode='POSE')
            #deselect previous bone group
            bpy.ops.pose.group_deselect()
            #select bone group in menu
            bone_groups = obj.pose.bone_groups
            bone_groups.active = bone_groups["FK FINGERS R"]
            
            #display right layer
            #select bones in active bone group
            bpy.ops.pose.group_select()
            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}


class LCT3_OT_Clear_bone_transform(Operator):
    bl_idname = "lct3.clear_bone_transform"
    bl_label = "Clear Transforms"
    bl_description= "Clear transform of selected bones, so they get back to original state"

    def execute (self,context):
        if bpy.context.object.type == 'ARMATURE':
            print("hey")
            if bpy.context.selected_pose_bones is not None: 
                print("hey2")
                obj = context.object
                #get to pose mode
                bpy.ops.object.mode_set(mode='POSE')
                bpy.ops.pose.transforms_clear()
                print("hey3")
            else:
                def draw(self, context):
                    self.layout.label(text="No Bone selected!")

                bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')

            
            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}

class LCT3_OT_Set_Inverse_all(Operator):
    bl_idname = "lct3.set_inverse_all"
    bl_label = "Cleanup Controls"
    bl_description= "Sets inverse of 'Child of' Constraints in the Rig. It is useful when the Control Handles do not follow Hands, elbows, Knees, Head or Hips. (It should only be used before animating)"

    def execute (self,context):
        if bpy.context.object.type == 'ARMATURE':
            bpy.ops.object.mode_set(mode='POSE')
            ob = bpy.context.active_object
            #set pose mode
            
            # Take a copy of current layers 
            org_layers = ob.data.layers[:]

            # Show all layers
            for i in range(len(org_layers)):
                ob.data.layers[i] = True
            try:
            #Executa quando dá certo
                for b in ob.pose.bones:
                    for c in b.constraints: 
                        if c.type == "CHILD_OF":
                            context_py = bpy.context.copy()
                            context_py["constraint"] = c
                            ob.data.bones.active = b.bone
                            bpy.ops.constraint.childof_set_inverse(context_py, constraint="Child Of", owner='BONE')
                            
            except:
            #Executa quando não dá certo
                def draw(self, context):
                    self.layout.label(text="Error! Try Again!")

                bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
                bpy.ops.pose.select_all(action="DESELECT")
                for i in range(len(org_layers)):
                    ob.data.layers[i] = org_layers[i]
                    
                return {'FINISHED'}

            
             
            #Executa depois que dá certo

            #deseleciona
            bpy.ops.pose.select_all(action="DESELECT")

            # Reset back to orginal layer state
            for i in range(len(org_layers)):
                ob.data.layers[i] = org_layers[i]
            def draw(self, context):
                    self.layout.label(text="Cleanup done successfully!")
            bpy.context.window_manager.popup_menu(draw, title="Success", icon='CHECKBOX_HLT') 
            
            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}


