# 3DFaceReconstructionFromMultipleImages
##Description
It was my bachelor thesis. Main goal was to construct someone's 3D face model from their multiple photos.
> This was so hard to implement because of variations of photo and hardware limits. 
___
Photos have 
1. Variations of poses
2. Variations of facial expressions
3. Some photo's quality is very low 
4. Contains multiple person
___

Used Surrey's Univercity's face model as normal model. [You can find here]:https://cvssp.org/faceweb/3dmm/facemodels/

___
Technologies used :

Python
1. OpenCV - Image processing /Denoising , Cropping , Sampling , Feature Extraction etc/
2. DLib   - Face pose estimation
3. MenpoFit - Fitting my model to normal model


## Usage

```python
from 3DModelConstructor import 3DModelConstructor

#Create an instance
constrctr = new 3DModelConstructor()

#Copy your photo paths here
photos = [
...
imagePathsHere
...

]

#And it will produce 3D model where the script.
constrctr.construct(photos);

```
