# delaunay_visualization
Visualizes Delaunay triangulation with animation. Uses scipy.spatial and matplotlib. Checks Delaunay property. Helpful for understanding triangulation concepts.

How it works
Random point generation: Generates a random set of points.
Delaunay triangulation: Calculates the Delaunay triangulation using SciPy's Delaunay class.
Visualization: Uses Matplotlib to create an animation, visualizing each triangle and checking the Delaunay property.
Delaunay property: Verifies if a triangle satisfies the Delaunay property (no other points inside the circumcircle).
Customization
Number of points: Adjust the num_points parameter in the DelaunayVisualizer class to change the number of random points.
Animation speed: Modify the interval parameter in the FuncAnimation call to control the animation speed.
Contributing
Feel free to contribute to this project by:

Reporting issues: Open an issue on GitHub to report bugs or suggest improvements.
Creating pull requests: Submit pull requests with your code changes.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Inspired by ...
Thanks to ... for their contributions.
