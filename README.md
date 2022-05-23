# Nifi란??
- Apache Nifi는 시스템 간 데이터 전달을 효율적으로 처리, 관리, 모니터링 하기에 최적화 된 시스템임. 대량의 데이터 수집, 처리가능
- Dataflow를 쉽게 구성이 가능하며, 시스템 간의 데이터 이동과 내용을 볼 수 있는 UI제공
- 강력한 자원과 권한 관리를 통해 Multi-tenant(단일로 여러 소프트웨어에 공급하는 것)지원
- 데이터 어느 시스템으로 왔는지 추적 가능
- NiFi 시스템 간 통신 지원(site to site)

# Nifi 구성요소
<img width="985" alt="1" src="https://user-images.githubusercontent.com/49854618/162189316-4f3ec36c-ea75-49fd-9345-b1a423b5ad56.png">   

- FlowFile, Processor, Connection, Controller이 대게 네 가지로 이루어짐
- FlowFile - NiFi가 인식하는 데이터 단위
    - 일반적인 데이터 Content/Attributes로 나뉨
    - Content는 데이터 자체를 말함
    - Attribute는 데이터와 관련된 정보를 키/값 쌍으로 표현 한 것이다.
- Processor - FlowFile을 수집, 변형, 저장하는 기능
    - 처리 이후에 또다른 FlowFile을 만들어 낼수도 있다.
    - Processor는 여러개가 병렬적으로 동작 할 수 있다.
- Conector - Processor와 Processor를 연결 및 FlowFile을 전달하는 역할
    - FlowFile의 Queue를 의미함
    - 우선순위 조정 및 backpressure를 설정해 부하를 조절 할 수 있다.
- Flow Controller - 각 프로세스간의 연결, 그 사이에 오가는 FlowFile에 대해서 관리

# Nifi 아키텍처
<img width="581" alt="2" src="https://user-images.githubusercontent.com/49854618/162189400-5efa582e-fe3c-4005-a758-0fa35d1fb111.png">   

- web server - UI 웹 서버를 통해 제공, 개발자 혹은 관리자는 이를 이용해 DataFlow개발, 제어 모니터링 가능
- Flow Controller - Processor 가 어느 간격 또는 시점에 실행 되는지 스케쥴링을 담당
- Extension - NiFi가 제공하는 기본 Processor들 이외에 개발자가 Process를 개발해 확장이 가능
- Flow Controller - Write-Aheade-Log로 FlowFile의 속성과 상태값을 저장하는 곳, 시스템 장애시 데이터가 유실 되지 않도록 주의
- Content Repository - FlowFile의 데이터(Content)가 저장되며, 여러 디렉토리에 분석 저장이 가능 대용량 데이터 처리에 용의
- Provenance Repository - 데이터의 처리 단계별로 FlowFile 데이터를 보관하는 곳으로, 여러 디스크를 지원한다. 이 때 각 데이터는 인덱스 검색 할 수 있다.
 

# ZooKeeper 연동
<img width="786" alt="3" src="https://user-images.githubusercontent.com/49854618/162189456-47bc1d73-4f8e-41a0-8b5b-32d1c4aa1c3c.png">   

- Cluster Coordinator  - 각 NiFi서버들의 정보를 관리, DataFlow의 추가, 수정, 삭제 등의 변경을 클러스터에 등록된 NiFi노드들에 복제 해준다.
- Primary Node - 여러 노드에서 Processor가 실행 되지 않고, 특정 단일 노드에서만 실행하고자 할 때 사용하는 대표 노드
- ZooKeeper Server - 위와 같은 역할은 ZooKeeperServer에서 자동으로 선출 되며, NiFi1.0부터 Zero-MasterClustering 이 적용되어 클러스터 내에 NiFi 노드들 중 한대가 자동으로 Cluster Coordinator와 Primary Node가 된다.


# Nifi 설치 하고 구동해보기 
- apache nifi 홈페이지 접속 후 zip 파일 다운로드
<img width="1313" alt="apache nifi" src="https://user-images.githubusercontent.com/49854618/162451929-84e96d16-6427-412e-a5de-7a3d950dffe6.png">
- 개인이 사용할 폴더 생성 및 압축 해제
<img width="907" alt="downNifi" src="https://user-images.githubusercontent.com/49854618/162452038-c1b75b23-64ae-42f4-ae25-c8731771c72a.png">

- 처음 압충 해제 시 폴더 구조

```bash
기본 프로젝트 생성 시 파일구조
nifi
├── bin             - batch파일 이나 구동하는 shell파일 폴더
├── conf            - 기본정보가 있는 폴더 nifi.properties등
├── docs            - web ui html 및 doc관련 내용 폴더
├── extensions      - 확장프로그램 저장소 
├── lib             - nifi관련 nar, jar파일 폴더
├── LICENSE
├── NOTICE
└── README
```
- 서버 구동 - 생성폴더주소/bin/nifi.sh start (백그라운드 실행)
<img width="488" alt="startServer" src="https://user-images.githubusercontent.com/49854618/162452241-4b12ef7e-f943-4f86-8c41-95d905b274f3.png">

- https://localhost:8443/nifi로 접속
<img width="1436" alt="startingPage" src="https://user-images.githubusercontent.com/49854618/162452347-811f678b-80d3-4323-8102-ab7a953c6da4.png">

- 서버 구동후 파일 폴더 구조
<img width="917" alt="서버시작후 파일 바뀐것" src="https://user-images.githubusercontent.com/49854618/162452307-dcfb224d-1a37-4953-a3ef-4edd9edcbbf7.png">

```bash
서버 구동 후 폴더 구조
nifi
├── bin                     - batch파일 이나 구동하는 shell파일 폴더
├── conf                    - 기본정보가 있는 폴더 nifi.properties등
├── content_repository      - flowfile에서 사용하는 content 저장소
├── database_repository
├── docs                    - web ui html 및 doc관련 내용 폴더
├── extensions              - 확장프로그램 저장소 
├── flowfile_repository     - nifi에서 생성한 dataflow 저장소
├── lib                     - nifi관련 nar, jar파일 폴더
├── logs                    - nifi 서버 구동 시 생성되는 user와 app로그 등이 여기 있음 (generated user id, password가 여기 존재)
├── provenance_repository   - dataflow에서 사용하는 content중 검증된 내용이 여기에 저장되고, 사용됨
├── run                     - 서버 구동 정보
├── state                   
├── work                     
│   ├── docs                - nifi processor에서 사용하는 components들이 있는 폴더
│   ├── jetty             
│   ├── nar                 - 위에 docs에서 사용하는 compoenets들 nar파일 있는 폴더
├── LICENSE
├── NOTICE
└── README
```
- 서버 상태 확인 - 생성폴더주소/bin/nifi.sh status
<img width="489" alt="runningServer" src="https://user-images.githubusercontent.com/49854618/162452407-1f94b811-3c6b-4a1c-826c-241d6c3aeaef.png">

- 서버 중지 - 생성폴더주소/bin/nifi.sh stop
<img width="484" alt="stopServer" src="https://user-images.githubusercontent.com/49854618/162452435-81ea45df-dfee-45f0-a57c-e7194f24947d.png">

- 서버 중지 - 생성폴더주소/bin/nifi.sh run (포그라운드 서버 구동 방식)
- 사용자 만들기 - bin/nifi.sh set-single-user-credentials <Username> <Password 12자 이상>

# Nifi 웹 페이지
- 기본 페이지 구성   
<img width="1434" alt="스크린샷 2022-04-06 오후 5 58 04" src="https://user-images.githubusercontent.com/49854618/162451176-25a10c7c-455d-4b82-9b4f-331fdee41123.png">

- Components 툴바   
<img width="501" alt="스크린샷 2022-04-06 오후 6 03 56" src="https://user-images.githubusercontent.com/49854618/162451207-4f128da7-91b1-453d-8a82-6738b7d66016.png">

- 드래그 앤 드랍으로 컴포넌트 사용가능
- 상태 표시줄 - 구동 되고 있는, 멈춘, 오류가 있는 프로세서들 표시
- Navigation - 작업 공간에 있는 내용 모형으로 파악 가능
- Component 작업 패널 - 선택한 컴포넌트들 구동 및 작동 멈춤 등등의 기능 사용 가능 multi select 가능
- Flow Tree - processor group 및 flow 간 트리 작업 표시
- 메뉴 - component summary, counter, controller setting 등 전체적인 작업 관리 가능한 탭

# NiFi 실습  
- [GetFile, Putfile을 이용한 간단한 데이터 이관하는 패턴 만들어보기](https://magpienote.tistory.com/142)
- [Csv to Json 데이터 변형해보기(Controller 활용해보기)](https://magpienote.tistory.com/143)
- [DBConnector Controller 만들기](https://magpienote.tistory.com/152)
- [FlowFile의 Attribute와 Content 알아보기](https://magpienote.tistory.com/153)
- [RouteOnAttribute Processor 알아보기](https://magpienote.tistory.com/154)
- ExecuteStreamCommand Processor 알아보기(Flow 도중 Bash, Script NIFI에서 실행하기)
- [template을 이용하여 백업하기](https://magpienote.tistory.com/161)


