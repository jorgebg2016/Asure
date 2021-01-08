

const request = new XMLHttpRequest()
request.open('POST', 'http://127.0.0.1:5005/login')
request.send(JSON.stringify({
  username: 'jorgebg2016',
  password: '123456789'
}))
request.onload = () => {
  console.log(JSON.parse(request.response))
}