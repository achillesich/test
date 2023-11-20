import requests

def get_200():
    url = 'http://localhost:8080/api/hola'
    
    try:
        # Realizar la solicitud GET
        response = requests.get(url)
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            print('Solicitud GET exitosa!')
            print('Contenido de la respuesta:')
            print(response.text)
        else:
            print(f'Error en la solicitud. Código de estado: {response.status_code}')
            
    except requests.exceptions.RequestException as e:
        print(f'Error en la solicitud: {e}')

if __name__ == '__main__':
    while True:
        print("SELECT FRONTEND OPTIONS")
        print("OPTION 1 -  GET")
        print("OPTION 2 -  EXIT")
        print()
        opt =int( input("OPT :"))
        print()
        
        if opt == 1:
            get_200()
        if opt ==2:
            print("BYE BYE")
            break
        