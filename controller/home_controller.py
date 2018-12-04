from controller import controller_blueprint as controller
from services import HomeService

@controller.route('/home', methods=['GET'])
def home():
    return HomeService.test()
