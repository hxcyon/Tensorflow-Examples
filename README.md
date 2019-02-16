# Tensorflow-Examples

Before installing python package requirements, install conda and pip!
installing Conda in silent mode on macOS
'''
wget https://repo.continuum.io/miniconda/Miniconda3-3.7.0-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
'''
installing requirement.txt
'''
conda create --name tf python=3
source activate tf
pip install -r requirement.txt
'''
if installation does not work then, add a --user
'''
pip install --user -r requirement.txt
'''

