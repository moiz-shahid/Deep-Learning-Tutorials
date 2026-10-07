# Tutorial 04 - Data Augmentation using PyTorch

## Objective

The objective of this tutorial is to understand data augmentation and how it can be used to increase the size and variability of an image dataset.

The implementation is performed using **PyTorch and torchvision**.

## Data Augmentation

Data augmentation generates modified versions of existing images while preserving their main content. It can be useful when a large amount of training data is not available.

## Augmentation Techniques

The following augmentation techniques were applied:

- Random Rotation
- Shear Transformation
- Random Zoom
- Horizontal Flip
- Brightness Adjustment

## Implementation

A single JPEG image was uploaded from the computer.

Using `torchvision.transforms`, an augmentation pipeline was created with:

- `RandomRotation`
- `RandomAffine`
- `RandomHorizontalFlip`
- `ColorJitter`

The augmentation pipeline was repeatedly applied to the original image to generate different variations.

## Task

The task was to:

1. Take a single JPEG image from the computer.
2. Apply different image augmentation operations.
3. Generate 40 augmented versions of the original image.
4. Save all 40 augmented images in a folder.
5. Visualize sample augmented images.

## Output

A total of **40 augmented images** were successfully generated and saved.

The generated images contain different combinations of rotation, shear, zoom, horizontal flipping, and brightness variation.

## Tools and Libraries

- Python
- PyTorch
- torchvision
- PIL
- Matplotlib
- Google Colab

## Author

**Moiz Shahid**
