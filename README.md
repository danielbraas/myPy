<h1> myPy Repo </h1>

<h2>The scope of the repository</h2>
<p>This repository will contain my python scripts and likely material that I am using to learn Python.</p>
    raise NotImplementedError

<h3>Trouble getting jupyter notebook to work</h3>
<p>This passage describes problems I had to run jupyter notebook on a Windows10 PC. 
The last line of the error message was:

```
 File "C:\PYTHON\lib\asyncio\events.py", line 501, in add_reader
 NotImplementedError
```

The solution to this problem can be found [here](https://stackoverflow.com/questions/58422817/jupyter-notebook-with-python-3-8-notimplementederror/58430041#58430041)
and is to insert:


```
import sys

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```

into the file at: `~/Python/Lib/site-packages/tornado/platform/asyncio.py`
below the main imports.</p>
<tr>
<h3>Changing the starting directory for Jupyter Notebooks</h3>
<p>
The solution to this problem was discussed on Stack Overflow [here](https://stackoverflow.com/questions/35254852/how-to-change-the-jupyter-start-up-folder)
 
Open `cmd` (or Anaconda Prompt) and run `jupyter notebook --generate-config`.

This writes a file to `C:\Users\username\.jupyter\jupyter_notebook_config.py`.
Browse to the file location and open it in an Editor

Search for the following line in the file: `#c.NotebookApp.notebook_dir = ''`

Replace by `c.NotebookApp.notebook_dir = '/the/path/to/home/folder/'`
</p>
<hr>
<h3>Changing Jupyter Notebook Color Theme</h3>
<p>Install `jupyterthemes` using and then set theme:
 
 ``` 
 pip install jupyterthemes
 jt -t monokai
 ```
 
 If you want to further change to colors navigate to the `C:\path-to-python\Lib\site-packages\jupyterthemes\styles`
 folder, open the `.less` file you want to manipulate with a text editor and go nuts. </p>
<tr>
<h3>How to update all Python packages on Windows</h3>
<p> This was taken from: `https://www.activestate.com/resources/quick-reads/how-to-update-all-python-packages/`</p>
```
pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}
```

<h3>Useful Add-Ins when using VSCode</h3>
<li>Material Icon</li>

<hr>

