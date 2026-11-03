# Lab5-3D-from-stereo
Python code and lab sheet for lab class 5 on stereo. Details on how to run the code are below and the lab tasks can be found in the lab sheet IPCV-Stereo-Lab1-26-27.pdf.

If you are on a Linux system like Ubuntu:

<ol>
  <li> Down load a copy of LabI-v1.py or LabI-v2.py. Both have the same functionality but may be OS dependent. Try v1 first and then v2. v2 recommended for MacOS. If neither work, contact a TA.

  <li> Install a virtual environment using conda: <tt> conda create -n ipcv python=3.8</tt>

  <li> Activate the virtual environment: <tt> conda activate ipcv</tt>

  <li> Install opencv: <tt> pip install opencv-python</tt> or <tt> conda install -c menpo opencv </tt>

  <li> Install open3d: <tt> pip install open3d==0.16.0</tt> or <tt> conda install -c open3d-admin open3d</tt>

  <li> Run the simulator: <tt> python LabI-v1.py</tt> (if error, then try <tt> python LabI-v2.py</tt>)
  </ol>

You may want to use the following recommended versions for certain packages if you are not using a Linux system:

- For Mac user, we recommend Python is 3.8 or 3.9, numpy 1.21.5 and Open3D 0.16.0

- For Windows user, we recommend Python 3.8, numpy 1.23.3 and Open3D 0.11.2


## Troubleshooting

If open3d==0.16.0 doesn't work, try install older version, e.g. <tt>pip install open3d==0.14.1</tt>.

On Mac, you might need to install LLVM's OpenMP runtime library `brew install libomp`
If you face the problem regrading libomp please try 'brew reinstall libomp'.

Please check the version of python == 3.8 or 3.9 first and make sure your anaconda environment works. If not and your python is under $(pyenv root)/versions/ , please remove .pyenv and reinstall homebrew, as well. Please see link (https://stackoverflow.com/questions/51797189/how-to-uninstall-pyenvinstalled-by-homebrew-on-mac).

