from TestsTask.YaAPI import YadUpload

yad_token = 'AQAAAAAz3kTiAADLW4hKEMZnP0khv6FXKxCYVJ4'


class Test:

    def setup_class(cls):
        print('create user')

    def setUp(self):
        print('setup')
        # проверка отсутствия папки

    def test_check_not_existing_folder(self):
        assert 404 == YadUpload().check_created_folder('test_folder')
        # проверка создания папки

    def test_put_back_up_folder(self):
        assert 201 == YadUpload().put_back_up_folder('test_folder')
        # проверка наличия папки

    def test_existing_folder(self):
        assert 200 == YadUpload().check_created_folder('test_folder')
        # проверка создания папки с тем же именем

    def test_create_existing(self):
        assert 409 != YadUpload().check_created_folder('test_folder')

    def teardown(self):
        print('teardown')

    def teardown_class(cls):
        print('teardown class')
