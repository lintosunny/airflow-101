from airflow.sdk import dag, task, task_group

@dag
def group():

    @task
    def a():
        return 41

    @task_group(default_args={
        "retries": 3
    })
    def my_group(val: int):
        
        # use diff variable names [val, my_val]
        @task
        def b(my_val: int):
            print(my_val + 100)
        
        # as a best practice keep 1 inner task group max
        @task_group(default_args={
            "retries": 2
        })
        def my_inner_group():

            @task
            def c():
                print("c")

            @task
            def d():
                print("d")

            c() >> d()

        b(val) >> my_inner_group()

    val = a()
    my_group(val)

group()