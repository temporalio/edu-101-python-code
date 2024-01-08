# Exercise 3: Farewell Workflow
During this exercise, you will create an Activity method,
register it with the Worker, and modify a Workflow to execute it.

Before continuing, kill any Worker instances still running from any
previous exercises (you can do this by pressing Ctrl-C in the terminals 
where they are running.

As with other exercises, you should make your changes in the `practice` 
directory. Look for "TODO" comments, which will provide hints about what
you'll need to change. If you get stuck and need additional hints, or 
if you want to check your work, look at the completed example in the
`solution` directory. 

## Part A: Write an Activity Method
The `translate.py` file contains a method (`greet_in_spanish`) that uses a 
microservice to get a customized greeting in Spanish. This file also contains 
a utility method (`call_service`) that the Activity uses to call the microservice. 

1. Open the `translate.py` file (located in the `practice` subdirectory) in the editor
2. Create a new Activity that will get a custom farewell message from the microservice.
   1. Copy the `greet_in_spanish` method
   2. Rename the new method (use any valid name you like)
   3. Change `get-spanish-greeting` in this new method to `get-spanish-farewell`
   4. Save your changes to this file

## Part B: Register the Activity Method
1. Open the `worker.py` file (located in the `practice` subdirectory) in the editor
2. Modify the lines that registers your new Activity with the Worker (hint: you'll use the
   name you used for the new method in an earlier step).
3. Save your changes to this file


## Part C: Modify the Workflow to Execute Your New Activity
1. Open the `greeting.py` file (located in the `practice` subdirectory) in the editor
2. Look for the TODO message, uncomment the lines below it, and then change those lines
   to execute the Activity method you created
3. Save your changes to this file


## Part D: Start the Microservice and Run the Workflow
All commands below must be run from the `practice` subdirectory.

**Note: You will use multiple terminals to execute this step. All terminals
must have the virtual environment from Exercise #1 active in order to successfully
execute the code.**

1. Start the microservice by running `python microservice.py` in a terminal
2. In another terminal, start your Worker by running `python worker.py`
3. In a third terminal, execute your Workflow by running `python starter.py Donna` 
    (replacing `Donna` with your own name)

If there is time remaining, experiment with Activity failures and retries 
by stopping the microservice (press Ctrl-C in its terminal) and re-running 
the Workflow. Look at the Web UI to see the status of the Workflow and its
Activities. After a few seconds, restart the microservice by running the
same command used to start it earlier. You should find that the Workflow
will now complete successfully following the next Activity retry.
