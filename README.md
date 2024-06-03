# Stock Price Prediction Using Time Series Images

In this project, we will predict the price of a stock using time series images. For the proof of concept, I have chosen a timeframe of 6 months, i.e., the images of a stock's time series will span the previous six months from the date of capture.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [Contact](#contact)

## Installation

Follow these steps to replicate the project results on your system.

**Note**: To collect the images, I have prepared a hardcoded Python script named `file.py`. Open a browser (preferably Chrome) on your device and keep it open in the background. 
Write the names of stocks you wish to use for training in the file `shares.txt`, one per line, and save it.Select the time period from 1D, 5D, 1M, 6M, YTD, 1Y, 5Y, and Max, and search for the price of any arbitrary stock. Take a screenshot of the button corresponding to the time period of your choice.

![6M Button](https://github.com/Rahil-Maniar/Stock-Price-Predictor/assets/136798310/02d50264-0adc-4a98-be96-72ff33154f49)

For the scope of this project, I have taken the screenshot of the 6M button, circled in yellow. The script will press that button after searching for the stock and before taking the screenshot. The area encapsulated in yellow will be the region of the screenshot. This may not necessarily produce a time series image depending on the stock and the coordinates of the screenshot. Adjust these coordinates as per your requirement in `file.py`. Depending on the browser, you may want to replicate the procedure for a small sample and ensure that it works before implementing it on the entire dataset. Hence, try pasting the names of three random stocks and dry run `file.py` in the command line to check the images saved in the `Images` folder.

1. Paste the names of stocks you wish to use for training in `shares.txt`, one per line.
2. Change the `file_path` and `button_image_path` inside `file.py` to the path where you wish the screenshots to be saved and to the path of the image of the button to be clicked, respectively, before executing `file.py`.
3. Change the `left_dir` and `right_dir` inside `split.py` to the folders named "left" and "right," respectively, before executing `split.py`.
4. To extract test images, follow steps 2 through 4, change `file_path` to the folder "TestImages," and instead of `split.py`, run `split_test.py`.
5. Compress the folders "left" and "right," and access the notebook `Stock_Market_Prediction_Using_Time_Series_Images.ipynb`.
6. Follow the instructions in the notebook.

(The file `s1.txt` is to store the list of stocks used, one per line. If there are any redundant stocks in `s1.txt`, run `duplicate_entries_check.py`, which will only keep the first instance of the redundant stocks in `s1_cleaned.txt`.)

## Features
- Automated image capture of stock time series data.
- Image processing and classification.
- Stock price prediction using encoder-decoder architecture.

## Contributing

1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeature).
3. Commit your changes (git commit -m 'Add some feature').
3. Push to the branch (git push origin feature/YourFeature).
4. Open a Pull Request.

## Contact

- Rahil Maniar - rahilmaniar18@gmail.com
- Project Link: https://github.com/Rahil-Maniar/Stock-Price-Predictor
  
```bash
# Clone the repository
git clone https://github.com/Rahil-Maniar/Stock-Price-Predictor.git

# Navigate to the project directory
cd Stock-Price-Predictor
