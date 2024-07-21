import bpy
import pandas as pd
import numpy as np

def constructCurve(coords_list):
    #new 3D curve
    curve_data = bpy.data.curves.new(name='BezierCurve', type='CURVE')
    curve_data.dimensions = '3D'

    #new spline from curve
    spline = curve_data.splines.new(type='BEZIER')
    spline.bezier_points.add(len(coords_list)-1)

    #add points to spline
    for i, point in enumerate(coords_list):
        bp = spline.bezier_points[i]
        bp.co = point
        bp.handle_left_type = 'AUTO'
        bp.handle_right_type = 'AUTO'

    #new object from curve
    curve_obj = bpy.data.objects.new('BezierCurve', curve_data)
    bpy.context.collection.objects.link(curve_obj)

    #to make sure everything ran properly
    print('Added curve to environment')
    
    #change points via:
    #spline.bezier_points[0].co = [5, 5, 5] 
    #read points via print(spline.bezier_points[0].co)
    
def getPoints():
    curve = bpy.data.objects['BezierCurve'].data.splines[0].bezier_points
    
    points = []
    for point in curve:
        points.append(point.co)
    
    points = np.vstack(points)
    print(points)
    #pd.DataFrame(points).to_csv('/Users/nc7172/Downloads/points-edited.csv')
    
    print('Got points')

def cameraTrack():
    #add a camera to this scene and select it
    cam = bpy.data.cameras.new("Tracking Camera")
    camera_obj = bpy.data.objects.new('Tracking Camera',cam)
    bpy.context.collection.objects.link(camera_obj)
    bpy.context.view_layer.objects.active = camera_obj
    
    #add a follow path contraint
    bpy.ops.object.constraint_add(type='FOLLOW_PATH')
    camera_obj.constraints["Follow Path"].target = bpy.data.objects["BezierCurve"]
    camera_obj.constraints["Follow Path"].use_fixed_location = True
    bpy.ops.constraint.followpath_path_animate(constraint="Follow Path", owner='OBJECT')
    
    #add a track to contraint
    bpy.ops.object.constraint_add(type='TRACK_TO')
    camera_obj.constraints["Track To"].target = bpy.data.objects["Earth"]
    
    #keyframe the standard structure
    constraint = camera_obj.constraints.get("Follow Path")
    constraint.offset_factor = 0
    constraint.keyframe_insert(data_path="offset_factor", frame=1)
    constraint.offset_factor = 1
    constraint.keyframe_insert(data_path="offset_factor", frame=bpy.context.scene.frame_end)
    
    print('Added camera track')
    

###########

coords_list = pd.read_csv('/Users/nc7172/Downloads/points.csv', header=None)
coords_list = coords_list.values.tolist()
#print(coords_list)

constructCurve(coords_list)
cameraTrack()
getPoints()

print('Finished script') 