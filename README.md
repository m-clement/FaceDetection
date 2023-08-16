# Face Detection using OpenCV

This script detects faces in an image using OpenCV and the Haar cascades classifier. Detected faces are highlighted with rectangles, and the processed image is saved with detected faces.

## Prerequisites
- Python 3.x
- OpenCV library. 

  **Installation**:
  - For macOS:
    ```
    pip3 install opencv-python
    ```
  - For Windows:
    ```
    pip install opencv-python
    ```

## How to Use
1. Place your input image as `test.jpg` in the same directory as the script.
2. Run the script.
3. The script will process the image, detect faces, and display the image with rectangles around detected faces.
4. The processed image will be saved as `face_detected.jpg`.

## Features
- Uses Haar cascades for efficient face detection.
- Provides a visual representation of detected faces by drawing rectangles around them.

## Future Improvements
- Allow users to specify the input and output image filenames.
- Integrate with a graphical user interface for a more interactive experience.
