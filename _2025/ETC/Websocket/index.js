const express = require("express")
const { WebSocketServer } = require("ws")
const app = express()

app.use(express.static("front"))

app.listen(8000, () => {
  console.log(`Server listening on port 8000`)
})

// 웹소켓 서버 생성
const wss = new WebSocketServer({ port: 8001 })

// broadcast 메소드 추가
wss.broadcast = (message) => {
  wss.clients.forEach((client) => {
    client.send(message)
  })
}

wss.on("connection", (ws, request) => {
  // wss.broadcast 메소드를 할당하여, wss.clients.forEach로 시작하는 코드를 하나로 줄임
  ws.on("message", (data) => {
    wss.broadcast(data.toString())
  })

  ws.on("close", () => {
    wss.broadcast(`유저 연결 해제 [현재: ${wss.clients.size}명]`)
  })

  wss.clients.forEach((client) => {
    wss.broadcast(`새로운 유저 접속 [현재: ${wss.clients.size}명]`)
  })

  /*
  // 유저가 접속할 때 이를 모든 클라이언트에 알리고, 서버에도 로깅
  // 모든 클라이언트에 메세지를 보내는 것을 브로드캐스트(Broadcast)한다 라고 함
  wss.clients.forEach(client => {
    client.send(`새로운 유저 접속 [현재: ${wss.clients.size}명]`)
    // wss.clients는 리스트가 아닌 Set이므로 갯수를 샐 때 length 대신 size를 사용
  })

  // 유저 연결 끊겼을 때
  ws.on("close", () => {
    wss.clients.forEach((client) => {
      client.send(`유저 연결 해제 [현재: ${wss.clients.size}명]`)
    })
  })

  // 채팅
  ws.on("message", data => {
    wss.clients.forEach(client => {
      client.send(data.toString())
      // 클라이언트에서 전송되는 데이터를 서버에서 Blob으로 수신하므로 
      // toString() 메소드로 String으로 만들어야 함
    })
  })
*/
})


/*
// wss: 웹소켓 서버, ws: 연결된 클라이언트
// 웹소켓 서버 연결 이벤트 바인드
wss.on("connection", (ws, request) => {
  // request: 클라이언트로부터 전송된 http GET 리퀘스트 정보

  // 데이터 수신 이벤트 바인드
  ws.on("message", data => {
    console.log(`Received from client: ${data}`)
    ws.send(`Received ${data}`)   // 서버의 답장
  })

  // 연결 직후 해당 클라이언트로 데이터 전송
  ws.send(`Hello, ${request.socket.remoteAddress}`)   // 접속 환영 메시지
})
*/