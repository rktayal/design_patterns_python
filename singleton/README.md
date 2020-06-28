### Singleton Pattern
It's a creational pattern, meaning it's used to create objects. In this 
case, just one object. Singleton can be used to ensure that a class has exactly
one instance. This is handy when you need to control access to limited resource
such as a hardware device, set of buffer pools, or connection pools for web client.

Let's consider a logging subsystem for some application. events, errors, messages must
be logged to a file, perhaps for auditing or debugging. While there can be only one
instance controlling the log, that means we need to control access. This is a classic example
of singleton pattern. 

In the classic singleton pattern, singleton objects are not instantiated like other objects. 
The class definition provides a static instance method to use to access the one instance. 

Downsides of Singleton
 - Voilates the Single Responsibility Principle. They do two things. They look 
   for their own instantiation, then hold and process that state. 
 - They also have non standard class access. To get an instance, you've to know
   class is a Singleton, and use the instance method. 
 - Harder to test, since Singletons are tightly coupled with the objects that use
   them, it is hard to swap them out with mocks for unit testing.
 - Singletons carry global state, like that log file reference in logger class. In
   a sense, that's no better than globals generally, which have well-known testing 
   and maintainence problem. 
 - Also, because the class carries state, it is harder to sub-class or use for other 
   purposes.

A metaclass is a class's class. Therefore, an instance of metaclass is Class itself.

Singleton provides controlled access to a single instance by disallowing the creation of 
new ones, and this is also done lazily, the first time an instance is required. 
Though it is itself a global object, it reduces the overall size of the global namespace. 
It is subclassible for extended uses. 

