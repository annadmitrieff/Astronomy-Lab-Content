In this lab, students will apply Python scripts to utilize DS9 and Ginga to perform image analyses on sequenced photos of variable stars. 

`imagexam.py` uses DS9 to semi-automate the process of creating a radial profile, performing a Gaussian fit, and conducting a quick aperture photometry session using the 'exam' feature of DS9.

`radprof.py` uses Ginga to create a plot of the brightness curve of a specified coordinate in a specified photo.

To download these resources, open your command prompt/terminal and execute the following command. This will clone the repository to your home directory, enabling local access to all content included:

```
git clone https://github.com/annadmitrieff/Astronomy-Lab-Content.git
```
To conduct an image exam using the sample code for DS9, execute the following in your command prompt/terminal:
```
python3 imagexam.py
```
To create a brightness curve using the sample code for Ginga, execute the following in your command prompt/terminal:
```
python radprof.py
```

