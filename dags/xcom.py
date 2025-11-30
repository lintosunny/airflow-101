from airflow.sdk import dag, Context, task
from typing import Dict, Any

# with single value
@dag
def xcom_dag_single():

    @task
    def t1() -> int:
        val = 43 
        return val

    @task
    def t2(val: int):
        print(val)

    val = t1()
    t2(val) 

xcom_dag_single()


# with more than one value
@dag
def xcom_dag_multiple():

    @task
    def t1() -> Dict[str, Any]:
        my_val = 43 
        my_sentence = "Hello, world!"
        return {
            "my_val": my_val,
            "my_sentence": my_sentence
        }

    @task
    def t2(data: Dict[str, Any]):
        print(data['my_val'])
        print(data['my_sentence'])

    val = t1()
    t2(val) 

xcom_dag_multiple()