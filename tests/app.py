from asure import Asure, AsureBaseClassRoute, AsureBaseWebsocket
from asure import  AsueRequestObject, AsueRequestResponse, AsureWebsocket


app = Asure(templates_dir='templates', statics_dir='statics')


class Login(AsureBaseClassRoute):
    
    async def post(self, response :AsueRequestResponse, request :AsueRequestObject):      
        print(request.params.id)
        data = {
            'name': 'Jorge',
            'email': 'jorgebg2016@gmail.com'               
        }
        await response.send(data)
        
        
    async def get(self, response :AsueRequestResponse, request :AsueRequestObject):
        await response.renderize_html_page(template_name='login.html')
        

class Register(AsureBaseClassRoute):
    
    async def get(self, response :AsueRequestResponse, request :AsueRequestObject):
        print(request.get_json())
        await response.renderize_html_page(template_name='register.html')
        
        
class WebSocket(AsureBaseWebsocket):
    async def handler(self, websocket :AsureWebsocket):
        data = await websocket.recv()
        print(data)
        await websocket.send('Ola Client!')
        
        
           
app.add_resource(route_class=Login, route_path='/login')
app.add_resource(route_class=Register, route_path='/register')
app.add_resource(websocket_resource=WebSocket)


if __name__=='__main__':
    app.run('127.0.0.1', 5005)