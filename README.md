<h1> myPy Repo </h1>

<h4>The scope of the repository</h4>
<p>This repository will contain my python scripts and likely material that I am using to learn Python.</p>

<h4>Trouble getting jupyter notebook to work</h4>
<p>This passage describes problems I had to run jupyter notebook on a Windows10 PC. The last line of the error message was:
  File "C:\PYTHON\lib\asyncio\events.py", line 501, in add_reader
    raise NotImplementedError
NotImplementedError
The solution to this problem can be found at https://stackoverflow.com/questions/58422817/jupyter-notebook-with-python-3-8-notimplementederror/58430041#58430041 
and is to insert:

```{
import sys

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
}
```

into the file at: ~/Python/Lib/site-packages/tornado/platform/asyncio.py
below the main imports.</p>