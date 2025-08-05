"""
전통적인 DAG 생성 방식 (Classic Approach)
- DAG 객체를 직접 생성 (어떤 작업들을 어떤 순서로 실행할지 표현한 흐름도)
- 각 태스크를 개별 오퍼레이터로 생성
- 명시적인 의존성 설정 필요
"""

from airflow import DAG # DAG 생성 클래스
# operator: DAG내에서 실제로 실행되는 태스크의 종류를 정의
from airflow.operators.python import PythonOperator # 파이썬 함수 실행하는 task 만들 때 사용
from airflow.operators.bash import BashOperator # bash command (터미널 명령어)를 실행하는 task를 만들 때 사용
from datetime import datetime, timedelta

# 기본 설정 정의: DAG내 모든 태스크에 공통으로 적용될 기본 설정
default_args = {
    'owner': 'airflow_student', #DAG 소유자
    'depends_on_past': False, # 이전 실행이 성공해야 이번 실행을 할지 여부
    'start_date': datetime(2025, 1, 1), # DAG 실행을 시작할 날짜
    'email_on_failure': False,
    'email_on_retry': False,
    
    # 태스크가 실패했을 때 재시도 횟수와 간격
    'retries': 1, 
    'retry_delay': timedelta(minutes=5),
}

# DAG 인스턴스 생성 (전통적인 방식)
dag = DAG(
    'example_simple_dag',  # DAG ID
    default_args=default_args,
    description='전통적인 방식으로 만든 간단한 데이터 처리 DAG',
    schedule='@daily', # 하루에 한 번 실행
    catchup=False,  # 과거 날짜에 대한 백필 비활성화 (과거 날짜의 작업은 실행하지 않음)
    tags=['example', 'traditional', 'beginner'], # DAG를 분류할 수 있는 태그
)

# Python 함수 정의 (실제 작업 내용)
def extract_data(**context): # 데이터를 가져오는 시뮬레이션
    """데이터 추출 시뮬레이션"""
    print(f"데이터를 추출하는 중... (실행 날짜: {context['ds']})")
    return "추출된 데이터"


def transform_data(**context): # 이전 Task 결과(Xcom)을 불러와서 가공하는 시뮬레이션
    """데이터 변환 시뮬레이션"""
    print("데이터를 변환하는 중...")
    # XCom에서 이전 태스크의 결과 가져오기
    extracted_data = context['task_instance'].xcom_pull(task_ids='extract')
    print(f"받은 데이터: {extracted_data}")
    return "변환된 데이터"

"""
Xcom: cross communication의 약자로 airflow task간 데이터를 주고 받을 일이 있는데 이 부분을 해결하기 위해 나옴
- Task에서 연산이나 필요한 데이터가 각각의 task마다 변경이 될 때가 있는데 이런 경우에 데이터를 처리하기 위해 주로 사용됨
- Airflow는 TaskInstance간 데이터를 공유하지 않기 떄문에 Xcome을 이용하여 """


def load_data(**context):
    """데이터 적재 시뮬레이션"""
    print("데이터를 적재하는 중...")
    transformed_data = context['task_instance'].xcom_pull(task_ids='transform')
    print(f"적재할 데이터: {transformed_data}")
    print("데이터 파이프라인 완료!")


# 태스크 생성 (전통적인 방식 - 각각 개별 오퍼레이터)
start_task = BashOperator(
    task_id='start',
    bash_command='echo "전통적인 DAG 시작!"',
    dag=dag,
)

extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load_data,
    dag=dag,
)

end_task = BashOperator(
    task_id='end',
    bash_command='echo "전통적인 DAG 완료!"',
    dag=dag,
)

# 태스크 간의 의존성 설정 (전통적인 방식)
start_task >> extract_task >> transform_task >> load_task >> end_task