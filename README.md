# AccuKnox Assessment Answers
### Question 1
By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
### solution
By default, Django signals are executed synchronously. This means that when a signal is triggered, the connected signal handler (receiver function) runs in the same thread and blocks execution until it completes.
#### Proof with a Code Snippet:
We'll create a simple Django model with a post_save signal. If signals were asynchronous, the main thread would continue execution without waiting for the signal handler. But since signals are synchronous, execution will pause until the signal handler finishes.

<a href="https://github.com/JayarajVp/AccuKnox_codes/blob/main/new/signals_app/question1.py"> Link to solution code</a></br>
<a href="https://github.com/JayarajVp/AccuKnox_codes/blob/main/Output/Question%201"> link to output</a>

### Question 2
Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
### soultion
Django signals run in the same thread as the caller by default. This means that the execution of the main process is blocked until the signal handler completes.
#### Proof with a Code Snippet
We'll use Python's threading module to compare the thread IDs of:
1) The main execution thread (which saves a model instance).
2) The signal handler function.

<a href="https://github.com/JayarajVp/AccuKnox_codes/blob/main/new/signals_app/question2.py"> Link to solution code </a>
<a href=""> link to output </a>

