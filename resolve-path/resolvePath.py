"""
You are given a file system represented as an object where keys are absolute paths 
and values are either null (real file/directory) or a string (a symlink pointing to 
another path). Write a function that resolves a given path to its real destination, 
following symlinks along the way. If a symlink chain forms a cycle, return null.
"""

fs = {
  "/a": "/b",
  "/b": "/c",
  "/c": None,
  "/loop1": "/loop2",
  "/loop2": "/loop1",
  "/real": None,
  "/alias": "/real",
}

def resolvePath(fs, absolutePath):
    seen = set()

    while fs.get(absolutePath) is not None:
        if absolutePath in seen:
            print("null")
            return
        seen.add(absolutePath)
        absolutePath = fs.get(absolutePath)
    
    print(absolutePath)

resolvePath(fs, "/a")       # /c
resolvePath(fs, "/alias")   # /real
resolvePath(fs, "/loop1")   # null
resolvePath(fs, "/real")    # /real