# Editing a Camera Track in Blender

There are a number of ways we can edit camera movement and direction along a spline in Blender.

The main properties that are of interest are changing movement speed and viewing direction. We'll go through each of them one by one:

## Editing movement speed:

If we want the camera to slow down or speed up at certain moments, we can keyframe the "Offset Factor" property within the "Follow Path" constraint.

Let's say we want to slow the camera down between frames 87 to 130. At the camera's normal speed, the "Offset Factor" will be 0.275 at frame 87. We'll keyframe the camera's location at this frame (by hovering over the "Offset Factor" value and pressing "I"), to ensure that the camera approximately follows its "normal" path before frame 87:

<figure><img src="../.gitbook/assets/image (49).png" alt="" width="563"><figcaption></figcaption></figure>

We'll now go to frame 130. Right now, the "Offset Factor" at this frame is 0.467. Since we want the camera to slow down during this interval, we need to choose a number less than 0.467 to indicate we want the camera to be at an earlier position than its "normal" speed. Still, it should be greater than 0.275 (our previous keyframe) so that the camera is not going backwards. Let's make it 0.300 for now:

<figure><img src="../.gitbook/assets/image (51).png" alt="" width="563"><figcaption></figcaption></figure>

If we now play the animation, we'll see the camera slow down between these frames (87 to 100). Note that we're also going to see the camera slow down right before our desired slow interval (and speed up right after). This is a result of Blender automatically smoothing keyframes. If we want to change how Blender smooths our camera's movement we can switch to the "Graph Editor" interface:

<figure><img src="../.gitbook/assets/image (52).png" alt="" width="563"><figcaption></figcaption></figure>

From here, we'll press the "Normalize" button at the top to better view the curves:

<figure><img src="../.gitbook/assets/image (53).png" alt="" width="563"><figcaption></figcaption></figure>

We can now see the smoothing of our keyframes. If we want to change it, we can select the points we'd like to be changed using shift+click or dragging a selection box, then pressing "T" to change the interpolation:

<figure><img src="../.gitbook/assets/image (54).png" alt="" width="563"><figcaption></figcaption></figure>

We'll see the selected interpolation in our environment playback as well as the graph below.

The same principles of keyframing can be used to speed up the camera at certain frame intervals. Furthermore, instead of making our intervals based on time, we can make them based on location along the curve. For instance, if we wanted the latter half of our camera's movement along the curve to be slower, we could move our keyframe of the "Offset Factor" of 1 to frame 300 instead of 250 and keyframe and "Offset Factor" of 0.5 at frame 125.&#x20;

Once you understand how keyframing works, the possibilities for customization are endless.

## Editing camera direction:

Another application of keyframes is to the camera direction, or what object the camera is focusing on.

At times, we might have more than one object that we want to focus on during an animation. For this, we'll modify the "Track To" constraint, and its "Influence" property. This property is essentially the strength of our tracking: how strong will the influence of this constraint be.

With this in mind, we'll use this environment as an example:

<figure><img src="../.gitbook/assets/image (41).png" alt="" width="563"><figcaption></figcaption></figure>

Let's say we want to switch from tracking the bottom cube to the top one. To do this, we'll first need to add another "Track To" constraint, with our target being the second object:

<figure><img src="../.gitbook/assets/image (42).png" alt="" width="563"><figcaption></figcaption></figure>

Notice how we now see two blue dashed lines from our camera to the two objects. We can now keyframe the "Influence" attribute for each constraint. Let's say that around half-way through the animation, we want the camera to switch between the top cube to the bottom. We'll start our keyframing on frame 1, where we'll make the influence of the "Track To" constraint of the bottom cube 0 and the top cube 1:

<figure><img src="../.gitbook/assets/image (43).png" alt="" width="563"><figcaption></figcaption></figure>

Next, we'll go to frame 100 and keyframe the same "Influences" so that between frames 1 and 100, we're still tracking the top cube. Then, at frame 120, we'll switch the "Influences" so that the top cube is being tracked by the camera:

<figure><img src="../.gitbook/assets/image (44).png" alt="" width="563"><figcaption></figcaption></figure>

From this point to the end of the animation, this dynamic will hold. If we scrub through the animation, we should see the desired camera effect of it switching from the top cube to the bottom cube.

This is really the extent to which we can control tracking in Blender via the "Track To" constraint. If we want something more custom, we must get rid of all the "Track To" constraints entirely, and manually rotate and position the camera to show certain objects along our path. This would be done by keyframing within the "Object Properties" menu:

<figure><img src="../.gitbook/assets/image (45).png" alt="" width="375"><figcaption></figcaption></figure>
