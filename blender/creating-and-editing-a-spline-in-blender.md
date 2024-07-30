# Creating and Editing a Spline in Blender

If Python doesn't fit your desires, we can also make a spline exclusively using the Blender interface, without defaulting to a Python script of 3D points.

## Adding a spline:

To add a spline object to the Blender environment, we can press shift+A or click the "add" button near the top left of the screen:

<figure><img src="../.gitbook/assets/image (7).png" alt="" width="92"><figcaption></figcaption></figure>

Within this menu, hover over the "curve" option, and select the "Bezier" option. We'll see the object added in the middle of the screen. If you don't see it because it might be because it's being covered by another object. To improve visibility, while the curve is selected, press S and drag the cursor to the outside of the environment. You should see the curve being scaled up in real-time:

<figure><img src="../.gitbook/assets/image (8).png" alt="" width="375"><figcaption></figcaption></figure>

## Editing points:

To edit individual points along the spline, we need to switch into edit mode. We can do this by selecting the curve and pressing tab or switching to edit mode through the menu at the top left:

<figure><img src="../.gitbook/assets/image (9).png" alt="" width="336"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (10).png" alt="" width="375"><figcaption></figcaption></figure>

Within the edit mode, there are three main tools we can use to edit our curve. Once we're done using these tools, we can press tab to switch back into object mode.

#### Extrude

Extruding points (adding points to the line) is very simple, and we can do this by pressing E on the keyboard, while a point is selected. From here, you can drag around the cursor to place our new point in the curve.

We can also apply a change (extrusion, movement, or rotation, which are below) to multiple points at once by selecting them one at a time (holding shift and selecting) or dragging our mouse across the screen to generate a selection box.

If you click, the point will be placed.

Note that if you want to move the point only along one axis, we can press E for extrude and then X, Y, or Z for whatever axis we want to move along. For instance:

<figure><img src="../.gitbook/assets/image (15).png" alt="" width="375"><figcaption></figcaption></figure>

Note that while we're moving the point, we can data on how much movement we're causing in the top left, via a vector that shows the difference (D) in the point's original location as compared to where it is now.

<figure><img src="../.gitbook/assets/image (16).png" alt="" width="290"><figcaption></figcaption></figure>

If we want to cancel the edit, we can just press esc.

#### Move

Moving points is very similar to extruding them. Within edit mode, click on one or more points and press G. Now, similarly to when we were extruding points, we can move a point around and click to release and finalize the movement.

Once again, notice the difference vector in the top left and note that we can move the point in only one direction by pressing G and then the axis we're moving along (X, Y, or Z):

<figure><img src="../.gitbook/assets/image (17).png" alt="" width="375"><figcaption></figcaption></figure>

If we want to cancel the edit, we can just press esc.

#### Rotate

As you might expect, rotating the points is almost exactly light extruding and moving them. Again, in edit mode, with a point(s) selected, we can press R to rotate a point in place:

<figure><img src="../.gitbook/assets/image (18).png" alt="" width="375"><figcaption></figcaption></figure>

Clicking the mouse will finalize the rotation. The difference vector is once again visible in the top left, and we can rotate along only one axis by pressing R and then the axis we'd like to rotate along.

If we want to cancel the edit, we can just press esc.

Note that extrusions, movements, and rotates can also be made via the edit menu on the left of the interface, through interacting through this menu is not as intuitive and much slower.

<figure><img src="../.gitbook/assets/image (19).png" alt="" width="24"><figcaption></figcaption></figure>

## Extra edits of curves:

While the above should be enough for most situations, sometimes we still want more customization.&#x20;

#### Interpolation

There's four of handle types that we can choose from to customize our curve:

<figure><img src="../.gitbook/assets/image (20).png" alt="" width="375"><figcaption></figcaption></figure>

By default, Blender makes the interpolation between curves 'Aligned' (though their purple looks more like red). We can change this within edit mode by selecting a point or number of points and pressing V, and selecting the type we'd like. For example:

<figure><img src="../.gitbook/assets/image (22).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (24).png" alt="" width="311"><figcaption></figcaption></figure>

#### Drawing A Spline

We can draw in a spline object if we'd like. To do so, simply select a spline object (or add one into the scene), and Tab into Edit Mode. Then, select the "Draw" option from the left menu:

<figure><img src="../.gitbook/assets/image (58).png" alt="" width="102"><figcaption></figcaption></figure>

From there, you'll see a pen object appear when you hover over the 3D viewport. You can draw in a spline object by simply dragging your cursor across the screen. Once you let go of the cursor, a new spline will appear - but it's still connected to the object you used to go into Edit Mode. To separate it, simply press P and select "Separate" (with the new spline points selected). Now you'll have two separate spline objects, one of which was drawn in:

<figure><img src="../.gitbook/assets/image (60).png" alt="" width="375"><figcaption></figcaption></figure>

#### Editing the whole object

If we'd just like to move all points or scale the curve, we can easily do this through object mode.&#x20;

From object mode, just follow the same techniques we used to move the singular points: press G (and optionally press X, Y, or Z to move along an axis). The same goes for scale, except that we're now pressing S (then optionally X, Y, or Z).

<figure><img src="../.gitbook/assets/image (25).png" alt="" width="375"><figcaption></figcaption></figure>
