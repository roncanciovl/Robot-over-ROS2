# Robot-over-ROS2
Robot implementation using Robot Operating System V2

PUblisher/subscriber nodes
HOLA 
Test on branches
HOLA alo123

pruebita lolo
alosito el mejor
\n  \\ AmigoblesssOG
pruebita otra 2

Test on branches


## Setup

Ref: https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html

1. Create a workspace folder in home
2. Create a new folder named src inside your workspace 
3. Go to home in a terminal: 

```shell script
cd ~
```

4. Go to src folder in your workspace. Change my_name_ws accordingly

```shell script
cd my_name_ws/src/
```

Clone without folder instructions> https://stackoverflow.com/questions/17581379/git-clone-without-project-folder 

command example: 
```shell script
git clone https://github.com/roncanciovl/Robot-over-ROS2.git .
```

4. Resolve dependencies according to your distro
```shell script
cd ..
rosdep install -i --from-path src --rosdistro foxy -y
```
Return: All required rosdeps installed successfully

This may requiere before

```shell script
sudo rosdep init
```
```shell script
rosdep update
```

5. Open VSCode, got to the menu and select file, an then select open folder and select our workspace in home. This show our workspace in the VScode explorer

6. In a terminal go to your workspace 

```shell script
colcon build
```

7. Sourve the overlay according to your distro

```shell script
source /opt/ros/foxy/setup.bash
```
8.

```shell script
. install/local_setup.bash
```


## Virtual Environment Setup in Linux

https://docs.ros.org/en/foxy/How-To-Guides/Using-Python-Packages.html

```shell script
sudo apt install python3-pip
```

```shell script
sudo apt install python3-virtualenv
```
### Make a virtual env and activate it

From your workspace directory run this command

```shell script
virtualenv -p python3 ./venv
```
```shell script
source ./venv/bin/activate
```

Make sure that colcon doesn’t try to build the venv
```shell script
touch ./venv/COLCON_IGNORE
```


Next, install the Python packages that you want in your virtual environment:

if any requirement file is in the src folder, then install them for command line

```shell script
pip install -r src/requirements.txt
```

Now you can build your workspace and run your python node that depends on packages installed in your virtual environment.



## Source Control Recommendations


2. For new features, create a new branch. Name it according to the feature. You may add it to the github repo.





BUENOS DIAS :)
ADIOS 
hola willy
HOla reyes

Feliz cumpleaños willy :)
