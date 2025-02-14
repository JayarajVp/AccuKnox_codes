# AccuKnox Assessment Answers
### Question 1
By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
### solution
By default, Django signals are executed synchronously. This means that when a signal is triggered, the connected signal handler (receiver function) runs in the same thread and blocks execution until it completes.
#### Proof with a Code Snippet:
We'll create a simple Django model with a post_save signal. If signals were asynchronous, the main thread would continue execution without waiting for the signal handler. But since signals are synchronous, execution will pause until the signal handler finishes.

<a hurf=""> Link to solution code</a>
