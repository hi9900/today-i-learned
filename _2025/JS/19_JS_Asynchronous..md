# JavaScript의 비동기 처리

## Single Thread 언어, JavaScript

- JavaScript는 한 번에 하나의 일만 수행할 수 있는 Single Thread 언어로 동시에 여러 작업을 처리할 수 없음

- 즉 JavaScript는 하나의 작업을 요청한 순서대로 처리할 수 밖에 없음

> Thread

  작업을 처리할 때 실제로 작업을 수행하는 주체로, multi-thread 라면 업무를 수행할 수 있는 주체가 여러개라는 의미

## JavaScript Runtime

- JavaScript 자체는 Single Thread이므로 비동기 처리를 할 수 있도록 도와주는 환경이 필요함

- 특정 언어가 동작할 수 있는 환경을 "런타임(Runtime)"이라 함

- JavaScript에서 비동기와 관련한 작업은 브라우저 또는 Node 환경에서 처리



## 비동기 처리 동작 방식

- 브라우저 환경에서의 비동기 동작은 아래와 같이 처리된다

  1. 모든 작업은 **Call Stack**(LIFO)으로 들어간 후 처리된다.

  2. 오래 걸리는 작업이 Call Stack으로 들어오면 **Web API**로 보내 별도로 처리하도록 한다.

  3. Web API에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가지 못하고 **Task Queue**(FIFO)에 순서대로 들어간다.

  4. **Event Loop**가 Call Stack이 비어있는 것을 계속 체크하고 Call Stack이 비어있다면, Task Queue에서 가장 오래된(가장 앞에 있는) 작업을 Call Stack으로 보낸다.

### 비동기 처리 동작 요소

1. JavaScript Engine의 Call Stack

  - 요청이 들어올 때마다 순차적으로 처리하는 Stack(LIFO)

  - 기본적인 JavaScript의 Single Thread 작업 처리

2. Web API

  - JavaScript 엔진이 아닌 브라우저에서 제공하는 runtime 환경

  - 시간이 소요되는 작업을 처리(setTimeout, DOM Event, AJAX 요청 등)

3. Task Queue

  - 비동기 처리된 Callback 함수가 대기하는 Queue(LIFO)

4. Event Loop

  - Call Stack과 Task Queue를 지속적으로 모니터링

  - Call Stack이 비어있는 지 확인 후 비어있다면, Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push

---

## 정리

- JavaScript는 한 번에 하나의 작업을 수행하는 Single Thread 언어로 동기적 처리를 하지만,

  브라우저 환겅에서는 Web API에서 처리된 작업이 지속적으로 Task Queue를 거쳐 Event Loop에 의해 Call Stack에 들어와 순차적으로 실행됨으로써 
  
  비동기 작업이 가능한 환경이 됨