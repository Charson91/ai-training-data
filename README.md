Case Study: AI training data generation

Objective: Develop a script that simulates taking a “snapshot” of an infinite
field of optimally packed circles. You will generate a synthetic dataset consisting
of images representing a specific window of this field and corresponding metadata
identifying the circles fully contained within that window.

Specific Problem Statement:
Imagine an infinite 2D plane filled with circles
of radius r arranged in an optimal packing configuration. A rectangular window
is placed at an arbitrary location on this plane. Your task is to:
• Determine the mathematical arrangement for the densest 2D circle packing
• Render the portion of the plane visible through a given window size
• Ensure the window placement feels random (the circles should not consis-
tently align with the corners or edges of the window)
• Export the visual result and the spatial data of the internal circles

Dataset Specifics: Create a dataset of 100 image (png) and respective metadata
(json) files with the following configurations:
• window width: 1.0
• window height: 0.8
• radius r ∼ U(0.01, 0.05) drawn randomly for each datum
• metadata file should at least contain domain width and height as well as
centres and radii for all circles fully within the domain
• images should plot all circles within the window in white (filled) on black
background, colouring all circles from the metadata file in a different colour

Presentation: Write the code in Python using only standard libraries, i.e.,
numpy, scipy and matplotlib. Create a git repository to manage the coding
history and try to make sure the code runs easily on other machines as well.
