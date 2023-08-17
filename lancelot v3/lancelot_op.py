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
            T_layers = now_layers
            T_layers[0] = True

            if T_layers[1] == False:
                T_layers[1] = True
                T_layers = tuple(T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
                
                
            else:
                T_layers[1] = False
                T_layers = tuple(T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
                
                

            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}


class LCT3_OT_Stretch_Layer(Operator):
    bl_idname = "lct3.stretchlayer"
    bl_label = "Stretch"
    bl_description= "Stretch Layer"
 
    
    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            bpy.ops.object.mode_set(mode='POSE')
            # bpy.ops.armature.armature_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
            now_layers=obj.data.layers
            now_layers = list(now_layers)
            print(now_layers)
            T_layers = now_layers
            T_layers[0] = True

            if T_layers[18] == False:
                T_layers[18] = True
                T_layers = tuple(T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
                
                
            else:
                T_layers[18] = False
                T_layers = tuple(T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
                
                

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
            T_layers = now_layers
            T_layers[0] = True
            
            if T_layers[2] == False:
                T_layers[2] = True
                T_layers = tuple(T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
            else:
                T_layers[2] = False
                T_layers = tuple(T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)

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
            T_layers = now_layers
            T_layers[0] = True

            if T_layers[3] == False:
                T_layers[3] = True
                T_layers = tuple(T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
                
               
            else:
                T_layers[3] = False
                T_layers = tuple(T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
               

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
            T_layers = now_layers
            T_layers[0] = True

            if T_layers[16] == False:
                T_layers[16] = True
                T_layers = tuple(T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
              
            else:
                T_layers[16] = False
                T_layers = tuple(T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
                

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
            T_layers = now_layers
            T_layers[0] = True

            if T_layers[5] == False:
                T_layers[5] = True
                T_layers = tuple(T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
                
            else:
                T_layers[5] = False
                T_layers = tuple(T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
               

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
            T_layers = now_layers
            T_layers[0] = True
            
            if T_layers[6] == False:
                T_layers[6] = True
                T_layers = tuple(T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
                
            else:
                T_layers[6] = False
                T_layers = tuple(T_layers)
                bpy.ops.armature.armature_layers(layers=T_layers)
                

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


class LCT3_OT_Clear_all_bone_transform(Operator):
    bl_idname = "lct3.clear_all_bone_transform"
    bl_label = "Clear All Transforms"
    bl_description= "Clear all transform in selected armature, so they get back to original state"

    def execute(self, context):
        # Ensure an armature is selected
        if bpy.context.active_object and bpy.context.active_object.type == 'ARMATURE':
            armature = bpy.context.active_object
            
            # Clear pose transforms for all bones in the selected armature
            for bone in armature.pose.bones:
                # Store the original rotation mode
                original_rotation_mode = bone.rotation_mode
                
                bone.location.zero()
                bone.rotation_quaternion.identity()
                bone.rotation_euler.zero()
                bone.scale = (1, 1, 1)
                bone.rotation_axis_angle[0] = 0
                bone.rotation_axis_angle[1] = 1
                bone.rotation_axis_angle[2] = 0
                bone.rotation_axis_angle[3] = 0

                # Set the rotation mode back to its original value
                bone.rotation_mode = original_rotation_mode

            # Update the viewport
            bpy.context.view_layer.update()
        return {'FINISHED'}

class LCT3_OT_Clear_bone_group_transform(Operator):
    bl_idname = "lct3.clear_bone_group_transform"
    bl_label = "Clear Bone Group Transforms"
    bl_description= "Clear the transforms of bones in the same bone group as selected bone."

    def execute(self, context):

        def clear_pose_transforms_for_bone_group():
            # Check if the active object is an armature and has an active bone
            if bpy.context.active_object and bpy.context.active_object.type == 'ARMATURE' and bpy.context.active_pose_bone:
                armature = bpy.context.active_object
                active_bone = bpy.context.active_pose_bone
                
                # Get the bone group of the active bone
                bone_group = active_bone.bone_group

                if bone_group:
                    # Clear pose transforms for all bones in the bone group
                    for bone in armature.pose.bones:
                        if bone.bone_group == bone_group:
                            # Store the original rotation mode
                            original_rotation_mode = bone.rotation_mode
                            
                            bone.location.zero()
                            bone.rotation_quaternion.identity()
                            bone.rotation_euler.zero()
                            bone.scale = (1, 1, 1)
                            bone.rotation_axis_angle[0] = 0
                            bone.rotation_axis_angle[1] = 1
                            bone.rotation_axis_angle[2] = 0
                            bone.rotation_axis_angle[3] = 0

                            # Set the rotation mode back to its original value
                            bone.rotation_mode = original_rotation_mode

                    # Update the viewport
                    bpy.context.view_layer.update()
                else:
                    print("The selected bone is not in a bone group.")

        clear_pose_transforms_for_bone_group()
        return {'FINISHED'}

class LCT3_OT_Clear_bone_layer_transform(Operator):
    bl_idname = "lct3.clear_bone_layer_transform"
    bl_label = "Clear Bone Layer Transforms"
    bl_description= "Clear the transforms of bones in the same layer as selected bone."

    def execute(self, context):

        def clear_pose_transforms_for_armature_layer():
            # Check if the active object is an armature and has an active bone
            if bpy.context.active_object and bpy.context.active_object.type == 'ARMATURE' and bpy.context.active_pose_bone:
                armature = bpy.context.active_object
                active_bone = bpy.context.active_pose_bone
                
                # Get the armature layer of the active bone
                armature_layer = active_bone.bone.layers

                # Clear pose transforms for all bones in the same armature layer
                for bone in armature.pose.bones:
                    if any(x and y for x, y in zip(bone.bone.layers, armature_layer)):
                        # Store the original rotation mode
                        original_rotation_mode = bone.rotation_mode
                        
                        bone.location.zero()
                        bone.rotation_quaternion.identity()
                        bone.rotation_euler.zero()
                        bone.scale = (1, 1, 1)
                        bone.rotation_axis_angle[0] = 0
                        bone.rotation_axis_angle[1] = 1
                        bone.rotation_axis_angle[2] = 0
                        bone.rotation_axis_angle[3] = 0

                        # Set the rotation mode back to its original value
                        bone.rotation_mode = original_rotation_mode

                # Update the viewport
                bpy.context.view_layer.update()

        clear_pose_transforms_for_armature_layer()

        return {'FINISHED'}



class LCT3_OT_STR_Reset_Length(Operator):
    bl_idname = "lct3.reset_length"
    bl_label = "Stretch Length Reset"
    bl_description= "Stretch Length Reset"
 
    def execute (self,context):
        obj = context.object
        if bpy.context.object.type == 'ARMATURE':
            bpy.ops.object.mode_set(mode='POSE')
             # Iterate through the pose bones
            for bone in obj.pose.bones:
                # Iterate through the constraints of the bone
                for constraint in bone.constraints:
                    # Check if the constraint is of type "STRETCH_TO"
                    if constraint.type == 'STRETCH_TO':
                        # Reset the Stretch To constraint
                        constraint.rest_length = 0
            # Return to Object mode (optional)
            bpy.ops.object.mode_set(mode='OBJECT')
            return {'FINISHED'}
        else:
            def draw(self, context):
                self.layout.label(text="No Armature selected!")

            bpy.context.window_manager.popup_menu(draw, title="Error", icon='ERROR')
            return {'FINISHED'}
