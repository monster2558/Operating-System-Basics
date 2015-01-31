# Operating-System-Basics

Operating system basics using Python. I will be addressing the following points through program: 

1- memory map (where exactly in memory do you load parts of your OS; where will it reside)
2- how your scheduler would work (process and/or thread aware, priorities). Perhaps a diagram with queues for different     priorities; also a diagram for process states in different queues (Ready, blocked, waiting for msg, running,             executing, interrupted, etc)
3- how to do interprocess communication (mailboxes, mutexes, atomicity, synchronous vs asynchronous communication, format    of message envelopes {sender process id, receiver process id, message type, message})
4- how to handle kernel vs user modes
5- memory allocation algorithms - you will write your own malloc/free operator (how do you keep track when user allocates    memory dynamically? will you use a buddy tree algo? linked list? stack? etc)
6- how to handle interrupts (also context switch goes in here - how will you save all registers and restore them: you       have one stack you need to keep track of where you are on it)
7- standard processes: keyboard process, monitor output, timing,
8- how to add timing services
9- how to load user processes and run them
to add preemption or not
10-add hotkeys (useful to debug your OS esp. in case it freezes, you can add hot keys to inspect memory)
   testing your OS

