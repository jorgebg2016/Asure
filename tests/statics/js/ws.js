

const ws = new WebSocket('ws://127.0.0.1:5005')

ws.onopen = ()=>{
  console.log('Connectado')
  ws.send('Ola Server!')
}
ws.onmessage = (event)=> {
  console.log(event)
}
