from airflow.sdk import dag, task 

@dag 
def branch():

    @task 
    def a() -> int:
        return 1 
    
    @task.branch 
    def b(val):
        if val == 1:
            return ["equal_1", "run_if_1"]
        return "not_1"
    
    @task 
    def equal_1(val):
        print(f"val -> {val}")

    @task 
    def run_if_1(val):
        print(f"val -> {val} ----")

    @task 
    def not_1(val):
        print(f"val -> {val}")

    val = a() 
    b(val) >> [equal_1(val), run_if_1(val), not_1(val)]

branch()