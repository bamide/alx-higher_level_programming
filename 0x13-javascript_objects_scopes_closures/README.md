Write an empty class Rectangle that defines a rectangle:

You must use the class notation for defining your class
guillaume@ubuntu:~/0x13$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Class: Rectangle]
guillaume@ubuntu:~/0x13$ 
Repo:

GitHub repository: alx-higher_level_programming
Directory: 0x13-javascript_objects_scopes_closures
File: 0-rectangle.js
