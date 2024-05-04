# Fusion 360 Triangle Caculator Add-In

## Description

Given 3 values, calculate the remaining angles and lengths of a given triangle.  This method works for any triangle (right, obtuse, or acute) rather than just right triangles as in the standard a^2 + b^2 = c^2 which applies to Right triangles only.

In Fusion 360, it is useful for calculating the exact distance between Offset Planes when trying to Loft to Sketches an exact distance to achieve an exact Angle.

## Example

For example, if you wanted the Edge of a Base to have angle greater than 45° such as 70°:

Sketch 1:  A Cube Where Sides = 12mm
Sketch 2:  A Cube Where Sides = ??mm
Offset Plan: ??mm

Angle A = 90
Angle B = 70
Angle C = 20

Side a = 12.77 (Length of side in Sketch 2)
Side b = 12 mm (from Sketch 1)
Side c = 4.36mm (Distance Between Sketch 1 & Sketch 2)

Final Dimensions

Sketch 1:  A Cube Where Sides = 12mm
Sketch 2:  A Cube Where Sides = 12.77mm
Offset Plan: 4.36mm

[See Results on Online Triangle Ca;culator on Calculator.net](https://www.calculator.net/triangle-calculator.html?vc=&vx=12&vy=&va=90&vz=&vb=70&angleunits=d&x=Calculate)

## Links / Resources

* [Triangle Calculator Online](https://www.calculator.net/triangle-calculator.html?vc=&vx=5.863&vy=1.67&va=30&vz=&vb=90&angleunits=d&x=99&y=25)
* [Fusion API:  Creating a Script or Add-in](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-9701BBA7-EC0E-4016-A9C8-964AA4838954)
* [Wikipedia:  Acute and obtuse triangles](https://en.wikipedia.org/wiki/Acute_and_obtuse_triangles)
* [Wikpedia: Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem#Other_proofs_of_the_theorem)