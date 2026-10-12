# Lab 4: The Face Detection Challenge

> We run our labs with [Python 3.6+](https://www.python.org/downloads/).
> For Windows, you might want to use [Conda](https://www.anaconda.com/products/distribution).

## Using the lab sheet

> You can also follow the instructions below using [the lab sheet](Lab4sheet.pdf).

## Overview

This lab will ask you to run and understand the usage of the Viola-Jones detector as provided by OpenCV. In particular, you will experiment with the pre-built off-the-shelf frontal face detector and apply it so some example images. This lets you gain experience on how and how well this classical detection framework can operate in practice.

## Task 1: The Viola-Jones Object Detector

- Study `face.py`
- We provide XML file `frontalface.xml`, which contains a strong classifier trained using AdaBoost for detecting frontal human faces.
- Run detector using:
	`python face.py -n images/face1.jpg`
- The program outputs the number of faces found to the console and the resulting detections are finally visualised in the produced output image called `detected.jpg`.
- Play around parameters of Viola-Jones object detector to achieve better performance.
- Some images might need pre-processing.

<details>
    <summary>Hint</summary>

`faces = model.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=1, flags=0, minSize=(10,10), maxSize=(300,300))`

</details>

## Task 2: Ground Truth

- We prepare ground truth in form of bounding box `(x,y,width,height)` coordinates for all valid frontal faces and store these annotations in `groundtruth.txt`.
- In `face.py`, modify `readGroundtruth` to produce bounding boxes of the ground truth.
- Then test the detector’s performance (with the given parameters as provided by `face.py`) on six given example images: `face1.jpg`, `face2.jpg`, `face3.jpg`, `face4.jpg`, `face5.jpg` and `face6.jpg`.
- Produce the six result images with
  * bounding boxes of the ground truth (in red)
  * and actually detected instances (in green)
  * drawn around frontal faces

## Task 3: IOU, TPR, F1-SCORE

- Implement some code using a manually fixed threshold on the Intersection-Over-Union (IOU) between bounding boxes to judge which faces given the ground truth were successfully detected.
- Calculate the TPR (true positive rate) for all test images, that is the fraction of successfully detected faces out of all valid faces in an image.
- You may see some practical difficulties in assessing the TPR meaningfully, think why it is always possible to achieve a TPR of 100% on any detection task.
- Implement a small piece of code to calculate the F1-score of your face detection system for all test images given the ground truth. Why this metric is more accurately and meaningfully?

<details>
    <summary>Hint1</summary>

IOU is a Jaccard coefficient measuring similarity between the predicted and ground truth annotation. It is defined as the size of the intersection divided by the size of the union of the predicted and ground truth annotation.

$$ J(A,B) = \frac{|A \cap  B|}{|A \cup  B|} $$

</details>

<details>
    <summary>Hint2</summary>

The predicted box is set as true prediction when its IOU > threshold. This threshold is generally 0.5. However it depends on the applications.

</details>

<details>
    <summary>Hint3</summary>

$$\text{F1-score} \ \ F_1 = 2 \frac{\text{precision} \cdot \text{recall}}{\text{precision} + \text{recall}}  $$

</details>
