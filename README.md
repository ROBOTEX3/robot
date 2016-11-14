# robot
the project that controls the robot

## Coding Style
- indent: space
- size: 4

## Architecture
`Core.py` is the main process which manages some modules and apps. Basically, each module receives commands through standard input.

Here is the available modules.

| module | function |
|:--:|:--|
| camera | face recognition |
| motor | motor controling |
| voice | voice recognition |

When you implement your app, you can use `app/library/client.py`　for process communication with the above modules.
