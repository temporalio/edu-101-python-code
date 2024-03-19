# Exercise 1: Hello Workflow
During this exercise, you will
* Review the business logic of the provided Workflow Definition to understand its behavior
* Modify the Worker initialization code to specify a task queue name
* Run the Worker initialization code to start the Worker process
* Execute the Workflow from the command line, specifying your name as input

Make your changes to the code in the `practice` subdirectory (look for TODO 
comments that will guide you to where you should make changes to the code). 
If you need a hint or want to verify your changes, look at the complete version 
in the `solution` subdirectory.

## Part A: Create a Virtual Environment and Install the Necessary Dependencies

### If you are using the GitPod enviornment provided by the course you can skip this step!

1. Open a terminal window in the environment and change directories to the root directory of the
`edu-101-python-code` repository
2. Run the following command to create a virtual environment

```
$ python -m venv env
```

3. Activate the virtual environment

```
$ source env/bin/activate
```

Once the environment is active you should see `(env)` prepended to your bash prompt similar
to below

```
(env) $
```

4. Install the necessary packages into the virtual environment

```
python -m pip install -r requirements.txt
```

5. Navigate back to the practice directory

```
cd exercises/hello-workflow/practice/
```


## Part B: Review the Workflow Business Logic

1. Open the `greeting.py` file (located in the `practice` subdirectory) in the editor
2. Review the input parameters, business logic, and return value. 

## Part C: Specify a Task Queue Name for the Worker

1. Open the `worker.py` file (located in the `practice` subdirectory) in the editor
2. Specify `greeting-tasks` as the name of the task queue
3. Save your changes


## Part D: Start the Worker

2. Run the following command in the terminal window to start the Worker

```
$ python worker.py
```

## Part E: Start the Workflow from the Command Line

1. Open another terminal window in the environment and change to the `practice` subdirectory for this exercise
2. Run the following command, replacing `Mason` with your first name. Be sure to retain the same quoting shown here when you run the command:

```
$ temporal workflow start \
    --type GreetSomeone \
    --task-queue greeting-tasks \
    --workflow-id my-first-workflow \
    --input '"Mason"' 
```

Note that this command starts the Workflow, but it does not wait for it to complete or show the result. 
If you have time, continue with the optional part of the exercise below to see how to view the result using `temporal`.

## Part F (Optional): Display the Result
You can run the following command to display the result of a Workflow Execution: 

```
temporal workflow show --workflow-id my-first-workflow
```

It is also possible, and often more convenient, to view this information using the Web UI. You will 
have a chance to do this in the next exercise.


### This is the end of the exercise.




