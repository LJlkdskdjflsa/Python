# Async Python

## Introduction
This note is made After watching [this](https://www.youtube.com/watch?v=Xbl7XjFYsN4&list=PLhNSoGM2ik6SIkVGXWBwerucXjgP1rHmB) series tutorial
This note Contains:
- [ ] The Async Ecosystem
- [ ] The Event Loop
- [ ] Using Coroutines
- [ ] How Coroutines work Under the hood
- [ ] Batteries including
- [ ] An Example Web Application
- [ ] Interacting with the Blocking Word
- [ ] Error Handling, Testing and Debugging

## The Async Ecosystem
### Why should you use asyncio
Latency -> bad user experience

In traditional single threaded applications (it's like a one line highway the speed in depending on the slowest car)
Solve -> Build multiple highways

In Programming -> Run Multiple thread in the background

### Multiple Threads Problem
the multiple thread are using the same storage
so it is unsafe to use multiple threads and change the value in side the thread

Solve -> using lock to prevent data from being modified
But -> the lock is not available always and lock is not fair (the first thread get and other threads need to wait until it finished)
Lock cost price! the more lock slower program and gets more memory 
And the most worst case is Dead Lock

### The Goal of AsyncIO

- maximize the usage of single thread
  - by handling I/O asynchronously
  - by enabling concurrent code using coroutine

## The Event Loop
- What is Event Loop
- Using the AsyncIO event loop: a high-level view
- Reactors and Proactors
- Available event loop implementations in AsyncIO
- configuring an AsyncIO event loop
- a peek under the hood
- uvloop: the Ultra fast asyncio event loop.

uvloop