# Command Line Interface
# CLI : Command Line Interface
## 문법 및 활용
### 1. CLI에서 `'.'`의 역할
- `.`: 현재 디렉토리
- `..`: 현재의 상위 디렉토리 (부모 폴더)

### 2. 기초 문법
1. 폴더 생성 
    ``` bash
    touch {folder_name}
    ```

    ```bash
    mkdir {folder_name}
    ```
    **단, 이때 folder name은 공백 포함 금지, 한글 사용 금지, 영어대소문자와 `_`만 사용**

2. 목록 출력
    ```bash
    ls -a
    ```
3. 위치 이동
    ```bash
    cd ..
    mkdir 02_git_adv
    ```
    - 결과: 상위 파일로 이동 후, 02_git_adv라는 폴더를 생성

    ```bash
    cd 02_git_adv
    ```
    - 결과: 02_git_adv로 이동

    ```bash
    cd ../01_git/
    ```
    - 결과: 상위 폴더로 이동 후 01_git 폴더로 이동
 
    - **자동완성: `tab` 활용**

4. 현재 위치 열기
    ```bash
    start .
    ```
    - 결과: 현재 위치를 열어줌

5. 파일 삭제
    ```bash
    rm {file_name}
    ```
    - 주의: rm 명령어를 사용하면 휴지통에 남지 않는다 -> **XX 복구 불가 XX**

    ```bash
    rm some {file_name} 
    ```
    - 여러개 동시에 삭제 가능

6. 폴더 삭제
    ```bash
    rm -r {folder_name}/ 
    ```
    - 폴더 삭제는 파일 삭제 문법과 다름

### 3. 절대경로와 상대경로
- 절대경로: Root 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것   
    - ex. 대한민국 대전광역시 유성구 봉명동 .... 000호
- 상대경로: 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
    - ex. 봉명동 000호
