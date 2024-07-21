# Creating a Camera Track in Blender

With a spline in place, we can now place a camera along its path and animate it.

## Basic camera movement and tracking:

We're starting from this position, with a spline and and object we'd like the camera to track:

<figure><img src="../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

First, we'll get rid of any cameras that currently exist within the scene by selecting them and pressing X.

Then, we'll add in a new camera. We're doing this work around since any camera offset from the 0,0,0 position will continue into the movement along the spline. If our camera was 10m above the origin, then it would be 10m above the spline if we animated. Since we want the camera to be exactly on the spline, we need it to be exactly at the origin.&#x20;

Note that if having the camera offset is what we want, then we can just change the position of the camera relative to the curve via the Object Properties menu, after we've added the Follow Path constraint, which is what we're doing below.

We'll add a camera by pressing shift+A and selecting the camera:

<figure><img src="../.gitbook/assets/image (27).png" alt="" width="91"><figcaption></figcaption></figure>

With the camera selected, we can add some constraints to make it follow the curve. Navigate over to the constraint section of the object properties menu on the bottom right:

<figure><img src="../.gitbook/assets/image (28).png" alt="" width="130"><figcaption></figcaption></figure>

Select the "Add Object Constraint" menu and in this selection screen, click the "Follow Path" option in the fourth column under "Relationship".

<figure><img src="../.gitbook/assets/image (29).png" alt="" width="375"><figcaption></figcaption></figure>

Within this screen, we'll set the target to be our curve and we'll also click the "Fixed Position" option.

<figure><img src="../.gitbook/assets/image (30).png" alt="" width="375"><figcaption></figcaption></figure>

By enabling this option, we get to manually control our camera movement, which enables us to slow down the camera at certain moments and speed it up at others. With this feature enabled, the movement of our camera relies entirely on the "Offset Factor", which is essentially a number that corresponds to the percentage of the path that we've gone through (0 being 0% and 1 being 100%).

So, at the beginning of our animation, we should be 0% along our path and at the end we should be 100%. To give this information to Blender to process, we need to add keyframes to the "Offset Factor" parameter. We'll do this through the timeline editor, which is at the bottom of the screen.&#x20;

<figure><img src="../.gitbook/assets/image (31).png" alt="" width="563"><figcaption></figcaption></figure>

We'll move our scrubber to the first frame, indicated by the number to the left of the "start" tab on the right. Here, we'll keyframe the offset factor to be 0, which means we're 0% done with the animation.

We can keyframe an attribute by hovering over the number it corresponds to and pressing "I" or we can press the small circle to the right of the number:

<figure><img src="../.gitbook/assets/image (32).png" alt="" width="375"><figcaption></figcaption></figure>

Now we'll move to the end. Let's say our animation runs 250 frames, which is the length of the playback range. We'll move our scrubber to frame 250:

<figure><img src="../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>

And we'll repeat the same keyframing process of pressing "I" or clicking the circle, except we'll change the "Offset Factor" to 1 before we do it:

<figure><img src="../.gitbook/assets/image (34).png" alt="" width="375"><figcaption></figcaption></figure>

To verify that we've keyframed right we see that there are now two orange diamonds visible when we look at the timeline for the camera object, and if we were to play or scrub through the animation, we'll see the camera move along the spline.

<figure><img src="../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

Notice, however, that our camera isn't looking in the right direction:

<figure><img src="../.gitbook/assets/image (36).png" alt="" width="375"><figcaption></figcaption></figure>

To fix this, we need to add another constraint, this time, a "Track To" one. Within the same menu in which we added our "Follow Path" constraint, now select the "Track To" option.

<figure><img src="../.gitbook/assets/image (37).png" alt="" width="375"><figcaption></figcaption></figure>

We should now see this menu within the object properties interface:

<figure><img src="../.gitbook/assets/image (38).png" alt="" width="375"><figcaption></figcaption></figure>

Here, we'll now select the object we want the camera to track. For our example, we're tracking a cube, so we'll select that.

<figure><img src="../.gitbook/assets/image (39).png" alt="" width="375"><figcaption></figcaption></figure>

That's it! If we look through our animation, we should see the camera moving along the curve while locked in on the cube.

<figure><img src="../.gitbook/assets/image (40).png" alt="" width="563"><figcaption></figcaption></figure>

From here, we could directly export our movie. If we wanted to edit the camera movement more, we can do that through Blender. Click [here](editing-a-camera-track-in-blender.md) to learn how.
