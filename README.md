# AccuKnox Assessment Answers
### Question 1
By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
### Solution
By default, Django signals are executed synchronously. This means that when a signal is triggered, the connected signal handler (receiver function) runs in the same thread and blocks execution until it completes.
#### Proof with a Code Snippet:
We'll create a simple Django model with a post_save signal. If signals were asynchronous, the main thread would continue execution without waiting for the signal handler. But since signals are synchronous, execution will pause until the signal handler finishes.

<a href="https://github.com/JayarajVp/AccuKnox_codes/blob/main/new/signals_app/question1.py"> Link to solution code</a></br>
<a href="https://github.com/JayarajVp/AccuKnox_codes/blob/main/Output/Question%201"> link to output</a>

### Question 2
Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
### Solution
Django signals run in the same thread as the caller by default. This means that the execution of the main process is blocked until the signal handler completes.
#### Proof with a Code Snippet
We'll use Python's threading module to compare the thread IDs of:
1) The main execution thread (which saves a model instance).
2) The signal handler function.

<a href="https://github.com/JayarajVp/AccuKnox_codes/blob/main/new/signals_app/question2.py"> Link to solution code </a></br>
<a href="https://github.com/JayarajVp/AccuKnox_codes/blob/main/Output/Question2"> link to output </a>

### Question 3
By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
### Solution
By default, Django signals do not run in the same database transaction as the caller. Signals execute immediately after the database operation, but they are not automatically part of the transaction block. This means that even if the main transaction is rolled back, the signal’s changes may still persist.
#### Proof with a Code Snippet
We'll use transaction.get_connection().in_atomic_block to check:
1) Whether the main transaction is active when saving a model.
2) Whether the signal runs inside the same transaction.

<a href="https://github.com/JayarajVp/AccuKnox_codes/blob/main/new/signals_app/question3.py"> Link to solution code </a></br>
<a href="https://github.com/JayarajVp/AccuKnox_codes/blob/main/Output/Question3"> link to output </a> 

### Question 4
Topic: Custom Classes in Python
Description: You are tasked with creating a Rectangle class with the following requirements:
An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

### Solution 
When a class implements the __iter__ method, it allows instances of the class to be iterable. This means that objects of the class can be looped over using a for loop or converted into an iterator.
### Proof with a Code Snippet

<a href="https://github.com/JayarajVp/AccuKnox_codes/blob/main/new/signals_app/rectangle.py"> Link to solution code </a></br>
<a href="https://github.com/JayarajVp/AccuKnox_codes/blob/main/Output/Question4"> link to output </a> 
