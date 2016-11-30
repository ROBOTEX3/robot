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
| sensor | distance sensing |

When you implement your app, you can use `app/library/client.py`　for process communication with the above modules.

## Simulator
Finally, we made perfect simulator which can execute applications.

### Available modules
- distance sensor
- motor

Don't worry about any errors if you use other modules because they will be just mocked.

### Install
You have to install Node.js before executing following codes.

```
$ cd simulator
$ npm install
$ npm install -g gulp
```

That's it!

### Simulate
```
$ gulp js
$ node index.js
```
Then you access to `localhost:3000/view` on the browser like Chrome. Now you see the simulation environment.
```
$ cd ..
$ python Core.py test
```
You've done!
