import bpy
import pandas as pd #only needed if reading points from a csv
import numpy as np

def constructCurve(coords_list):
    #new 3D curve
    curve_data = bpy.data.curves.new(name='BezierCurve', type='CURVE')
    curve_data.dimensions = '3D'

    #new spline from curve, with X points
    spline = curve_data.splines.new(type='BEZIER')
    spline.bezier_points.add(len(coords_list)-1)

    #set/add points to the spline: for each point/i in the points list
    for i, point in enumerate(coords_list):
        #set a temp variable to reference one of the points in the spline
        bp = spline.bezier_points[i]
        #set that reference to the points we provided in the csv
        bp.co = point
        #set both the left and right handles to be "auto" to generate a spline
        bp.handle_left_type = 'AUTO'
        bp.handle_right_type = 'AUTO'

    #new object from curve
    curve_obj = bpy.data.objects.new('BezierCurve', curve_data)
    #add the object to the scene
    bpy.context.collection.objects.link(curve_obj)

    #to make sure everything ran properly
    print('Added curve to environment')
    
def cameraTrack():
    #make a new camera
    cam = bpy.data.cameras.new("Tracking Camera")
    #make an object from that camera
    camera_obj = bpy.data.objects.new('Tracking Camera',cam)
    #add the camera object to the scene
    bpy.context.collection.objects.link(camera_obj)
    #make the camera object the current active selection, so we can edit its constraints
    bpy.context.view_layer.objects.active = camera_obj
    
    #add a follow path contraint
    bpy.ops.object.constraint_add(type='FOLLOW_PATH')
    #set the target to be the curve we created through constructCurve()
    camera_obj.constraints["Follow Path"].target = bpy.data.objects["BezierCurve"]
    #using a fixed location so that we can manually change the speed of the camera
    #at certain locations
    camera_obj.constraints["Follow Path"].use_fixed_location = True
    #set up to animate the camera across the path through keyframes we'll define later
    bpy.ops.constraint.followpath_path_animate(constraint="Follow Path", owner='OBJECT')
    
    #add a track_to contraint to make the camera look at a certain object the whole time
    bpy.ops.object.constraint_add(type='TRACK_TO')
    #we want the target to be the default "Cube" object
    camera_obj.constraints["Track To"].target = bpy.data.objects["Cube"]
    
    #get the constraint we want to edit for easier syntax
    constraint = camera_obj.constraints.get("Follow Path")
    #set the offset_factor to 0 and insert a keyframe for this property change at frame 1
    #the offset_factor is a percentage for how far along the path the camera is
    constraint.offset_factor = 0
    constraint.keyframe_insert(data_path="offset_factor", frame=1)
    #set the offset_factor to 1 and insert a keyframe for this property change at the last frame in the scene
    constraint.offset_factor = 1
    constraint.keyframe_insert(data_path="offset_factor", frame=bpy.context.scene.frame_end)
    
    #to make sure everything ran properly
    print('Added camera track')
    

###########
#can use this line if writing points within python, otherwise use the next two
coords_list = ([0,-5,2],[-3.5,0,1],[0,1,0],[2,3,-1],[2,7,-1],[0.5,6,0])

#read the csv containing our points
#coords_list = pd.read_csv('/Users/xxxxxx/Downloads/points.csv', header=None)

#convert the csv to a list so that it can be read by our constructCurve function
#coords_list = coords_list.values.tolist()

#construct the curve with our points
constructCurve(coords_list)
#track the camera to the curve
cameraTrack()

#to make sure everything ran properly
print('Finished script') 
